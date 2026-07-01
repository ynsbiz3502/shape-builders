#!/usr/bin/env python3
"""
Generate the eight "come to life" clips for Shape Builders with Google Gemini (Veo).

WHAT IT DOES
    Reads tools/prompts.json and, for each toy, asks Veo to render a short clip,
    then saves it to  videos/<slug>.mp4  where the game picks it up automatically.

REQUIREMENTS
    pip install google-genai
    A Google Gemini API key WITH Veo access:
        export GEMINI_API_KEY=xxxxxxxx        (macOS/Linux)
        setx GEMINI_API_KEY "xxxxxxxx"        (Windows, new shell after)

USAGE
    python tools/generate_videos.py                 # generate any clips that are missing
    python tools/generate_videos.py --force         # regenerate all eight
    python tools/generate_videos.py --only rocket house
    python tools/generate_videos.py --model veo-2.0-generate-001

NOTES
    * Veo is not instant — each clip takes ~1-3 minutes and costs a few dollars.
    * Model IDs and config fields change over time; if you hit an error, check
      https://ai.google.dev/gemini-api/docs/video and adjust --model / the config below.
    * Clips are ~4-8s. The game caps playback and also has a safety timeout,
      so slightly longer/shorter clips are fine.
"""

import argparse, json, os, sys, time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROMPTS = ROOT / "tools" / "prompts.json"
OUTDIR = ROOT / "videos"

DEFAULT_MODEL = "veo-3.0-fast-generate-preview"  # fall back to "veo-2.0-generate-001" if unavailable


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default=DEFAULT_MODEL)
    ap.add_argument("--force", action="store_true", help="regenerate clips that already exist")
    ap.add_argument("--only", nargs="*", default=None, help="only these slugs (e.g. rocket house)")
    ap.add_argument("--aspect", default="16:9", help="aspect ratio, e.g. 16:9 or 9:16")
    args = ap.parse_args()

    api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        sys.exit("ERROR: set GEMINI_API_KEY (a Veo-enabled Google Gemini API key) first.")

    try:
        from google import genai
        from google.genai import types
    except ImportError:
        sys.exit("ERROR: pip install google-genai")

    clips = json.loads(PROMPTS.read_text(encoding="utf-8"))["clips"]
    if args.only:
        clips = {k: v for k, v in clips.items() if k in set(args.only)}
    OUTDIR.mkdir(exist_ok=True)

    client = genai.Client(api_key=api_key)

    for slug, prompt in clips.items():
        out = OUTDIR / f"{slug}.mp4"
        if out.exists() and not args.force:
            print(f"[skip] {out.name} already exists")
            continue
        print(f"[gen ] {slug}: submitting to {args.model} ...")
        try:
            op = client.models.generate_videos(
                model=args.model,
                prompt=prompt,
                config=types.GenerateVideosConfig(
                    aspect_ratio=args.aspect,
                    number_of_videos=1,
                    # duration_seconds / person_generation may or may not be supported per model;
                    # remove or adjust if the API rejects them.
                ),
            )
            while not op.done:
                time.sleep(10)
                op = client.operations.get(op)
                print(f"       ...rendering {slug}")
            video = op.response.generated_videos[0].video
            client.files.download(file=video)   # ensure bytes are fetched
            video.save(str(out))
            print(f"[ok  ] wrote {out}")
        except Exception as e:
            print(f"[FAIL] {slug}: {e}")

    print("\nDone. Commit the videos/ folder and push — the game will play each clip on completion.")


if __name__ == "__main__":
    main()
