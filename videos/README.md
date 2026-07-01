# Toy "come to life" clips

Drop one short MP4 per toy here and the game plays it when that puzzle is completed
(instead of the built-in CSS animation). If a file is missing, the game automatically
falls back to the animation — so the game always works, with or without clips.

## Required filenames (must match exactly)
- `rocket.mp4`
- `house.mp4`
- `train.mp4`
- `car.mp4`
- `boat.mp4`
- `caterpillar.mp4`
- `flower.mp4`
- `ice-cream.mp4`

## Generating them with Gemini (Veo)
See [`../tools/generate_videos.py`](../tools/generate_videos.py) and
[`../tools/prompts.json`](../tools/prompts.json):

```bash
pip install google-genai
export GEMINI_API_KEY=your_veo_enabled_key
python tools/generate_videos.py
```

Keep clips short (~4–8s) and reasonably small (a few MB) so they load fast on tablets.
