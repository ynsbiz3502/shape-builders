# 🧩🚂 Shape Builders

A drag-and-drop shape puzzle for **preschoolers (ages 3–5)**, in the friendly, encouraging style of *The Learning Company / Reader Rabbit*.

**▶️ Play it here:** https://ynsbiz3502.github.io/shape-builders/

## What it does
- 🧩 **Build a toy from shapes.** Each round shows a dashed silhouette of a kid-toy — a rocket, house, train, car, boat, caterpillar, flower, or ice-cream cone — split into chunky shape pieces.
- 👆 **Drag each piece** from the tray up to its matching outline. Pieces snap into place with a generous, forgiving hit area (great for little hands and touchscreens).
- 🎉 **Come to life!** When the last piece clicks in, the finished toy comes to life, showers confetti — then a new puzzle loads. This plays a short **Gemini (Veo) video** of the toy if one is present in [`videos/`](videos/); otherwise it falls back to a built-in googly-eye wiggle animation, so the game always works.
- 🔊 **Sound & voice** — a friendly voice names each shape as you place it ("Triangle!", "Circle!") and cheers the finished toy ("You built the Rocket!"). Rising musical chimes reward every correct piece. *(All audio is generated in-browser — no files, works offline.)*
- ⭐ **Gamified dopamine** — progress dots fill as you build, stars rack up, a toy-counter grows, sparkles burst on every snap, and the matching outline glows to guide you.
- 😊 **Stress-free** — a piece only snaps to its own spot; drop it anywhere else and it gently floats back to the tray. No timers, no losing, endless play.

## Learning goals (Learning-Company style)
- **Shape recognition & names** (circle, square, triangle, rectangle…).
- Shape-to-outline **matching** and spatial reasoning.
- Fine-motor **drag control**, cause-and-effect, and color.

## Toy "come to life" videos (Gemini / Veo)
When a toy is completed the game plays a short clip of it coming to life — if the clip exists.
- Drop MP4s into [`videos/`](videos/) named `rocket.mp4`, `house.mp4`, `train.mp4`, `car.mp4`, `boat.mp4`, `caterpillar.mp4`, `flower.mp4`, `ice-cream.mp4`.
- Generate them with Gemini/Veo using [`tools/generate_videos.py`](tools/generate_videos.py) + [`tools/prompts.json`](tools/prompts.json) (needs a Veo-enabled `GEMINI_API_KEY`).
- **No clip? No problem** — the game automatically falls back to the built-in googly-eye wiggle animation, so it always works.

## Tech
- A single `index.html` — **no build step, no dependencies, no external assets** (videos optional).
- SVG shapes, Pointer Events for drag/drop, Web Audio for sound, SpeechSynthesis for voice, Web Animations for effects, HTML5 `<video>` for the optional toy clips.
- Hosted free on **GitHub Pages**.

Made with ❤️ for little builders.
