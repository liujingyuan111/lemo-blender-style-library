# 科幻情景喜剧卡通 · 原文美术章节

来源：Lemo-Opuscar by Lemomo (LemoLab)。原文：[STYLE.md](https://github.com/lemomo-ai/lemo-opuscar/blob/00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4/styles/scifi-toon/STYLE.md)。

固定提交：`00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4`。原文 SHA-256：`9a720a57ce50dc554e9237e698a979cdf7311527e6e6a0dad803278dfe8ad2ce`。

本页按章节摘录原作者的美术资料，保留所选章节原文；不是 Blender 原生实现，也不是已经通过的美术验收。原文中的示例、选项和建议保持原有含义，不自动升级为硬限制。某些原文章节顺带包含字幕、流程或声音提醒，它们仍是参考文字，不会加载为 Blender 约束。

文档许可：[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)，另有上游对自有／客户影片制作的额外许可，见[来源说明](../docs/SOURCE_NOTICE.md)。改动：只增加此说明并选择章节，所选原文未改写。

保留章节：1、2、3、4、6、9。

---

## 1. Essence, and what it is not

Hand-drawn-looking 2D TV animation for adults: **uniform thick dark outlines that boil**, **flat fills with hard-edged shadow shapes (no gradients)**, **big white eyes with tiny pupils**, **elastic mouths**, grotesque-but-cute creatures, and sci-fi hardware treated like household junk. The comedy is **dialogue-driven**: improvised-feeling talk, interruptions, awkward pauses, reaction shots, escalation, and a last-second reversal. The genre's engine is **a tiny, mundane goal pursued with absurdly large sci-fi means**: whoever could solve anything uses it for something petty, and someone else pays the emotional price.

Not a kids' cartoon (dry humour, long pauses), not anime (no sparkly eyes), not a vector explainer (lines boil).

**Copyright red lines (non-negotiable):**
- Never reproduce any existing show's characters, silhouettes or colour combos (e.g. a spiky-blue-haired old man in a lab coat + a kid in a yellow shirt), names, catchphrases, burp gags, logos, or the look of any existing portal gun.
- Invent your own cast, props and portal device. Never write the source show's name in the film or docs; one line "inspired by adult-swim-era sci-fi sitcom cartoons" is enough.

## 2. Materials & rendering

- **Line**: near-black (a slightly purple black reads best), ~7 px for characters and props, 4–6 px for background detail, round joins. **Line width is constant in screen space**: close-ups are "redrawn" at the same weight, never scaled up (transform points to screen, then stroke with an identity transform).
- **Line boil**: resample every outline in screen space (~7 px steps) and displace along the normal with low-frequency noise, amplitude ~1.7 px; cycle **3 boil drawings at 12 fps**. Everything boils, including held poses and backgrounds: a still frame is never dead.
- **Fill**: flat colours only. Shadows are hard-edged darker shapes clipped inside the fill (one per form, away from the light). Glows are 1–2 flat translucent rings, not gradients. Skies are **flat colour bands**.
- **Faces**: big white eyes (touching in 3/4 view), 4–5 px pupils, heavy lids for deadpan, eye bags. Parametric mouths (open, width, curl, skew) with interior, teeth, tongue. Brows carry the emotion.
- **Cast design**: silhouettes must read in solid black. Give each lead one absurd costume idea. Avoid white lab coat + spiky hair.
- **Creatures**: every world may get one creature that is disgusting *and* adorable; keep it non-verbal (sound effects) so the film stays a dialogue between the leads. Check that anything behind furniture still shows face and upper body.
- **The portal** (or whatever device moves between worlds): the only thing that glows. A lumpy rim with a thick outline, rotating spiral arms, a pale core, orbiting sparks, drips, a flat translucent wash over the scene while it's open. Open with a gentle overshoot (~12 %, back-ease ~0.3 s); a springy overshoot covers the actors.
- **Screen graphics**: a retro-terminal tag (VT323) typed in, coloured per world.

## 3. Colour logic

- **One palette per world**, 3–5 colours, maximally different from the previous world in hue *and* value, so the audience reads "we jumped" from colour alone.
- Line colour and eye white never change between worlds; everything else may.
- Glow colour belongs to the travel device only: nothing else in any world may use it.
- A deliberately bland palette (beige, brown) is itself a joke: use it for the world that is "suspiciously normal".
- Examples of a sequence of worlds: sage lab → magenta and lime jelly → orange and teal; or grey office → ultraviolet and gold → mint and coral → beige. Our demo's values are in DEMO.md.

## 4. Type & subtitles

- **Subtitles**: bottom centre, a rounded heavy sans (Baloo 2 ExtraBold ~50 px), white with a ~11 px black outline, so they look like the cartoon's own captions, with a small **speaker pill** in the character's colour (boiling outline) on the left. Lines over ~1300 px wrap to two lines. Overlapping lines stack; the older one dims to ~70 %.
- **Timing**: hold ≥ max(1.8 s, speech + 0.6 s) for narration; for rapid dialogue, `max(audio + 0.35 s, 0.9 s + chars / 17)`. Clip at world changes and **before a silent beat**, so the silence plays on a clean screen.
- **Title**: chunky display lettering popped in on 12 fps steps on a musical hit. Choose a period look that is not the source genre's logo: **avoid acid green, slime drips and wobbly bubble lettering** together, which reads as a specific show.
- Keep faces out of the subtitle band (bottom ~170 px) and the world tag clear of faces.

## 6. Camera grammar

A vocabulary, not a route. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Medium two-shot | the relationship; who reacts how | dialogue; a standoff; a deal |
| Hard cut to a close-up | an interruption, a face breaking | the cut-off line; the realisation; a lie |
| Insert extreme close-up of an object | the absurd detail | a reveal; the problem itself; the wrong result |
| Reaction close-up | the laugh lives on the face | after every absurd image |
| Tight close-up + short shake on one word | panic | the key word; an alarm; a scream |
| Rush zoom into the portal → swirl wipe | leaving a world | any jump between places, times or versions |
| Same framing repeated across worlds | only the world changes | a montage; a comparison; a list |
| Very slow push-in on a still two-shot | a cold silence | the pause after a reversal; a confession |
| Wide with the device and both leads in frame | the whole situation at once | a callback; a trap; a fresh start |
| Over-the-shoulder onto a screen | reading bad news | a message; a readout |
| Whip pan between two faces | overlapping argument | a fight; a bet; a double take |

Rule: every absurd image is followed by a **reaction close-up**. Transitions go through the travel device (swirl wipes) or hard cuts; no dissolves.

## 9. Pitfalls of the medium

- TTS reads hyphen stutters as words: write syllables ("buh, buh-broken"); respell words it mangles; pick names that survive a low voice.
- Whisper mis-hears very short clips unless padded with ~0.6 s of silence.
- A real interruption: generate the interrupted line *longer* than needed and truncate the audio where the other voice cuts in.
- A springy overshoot swallows the actors: gentle back-ease.
- Food and liquids need cues (surface detail, drips, steam) or they read as other objects.
- Square-wave synth cymbals alias into harsh 8–20 kHz fizz: band-passed noise plus a little FM.
- A sustained bass below ~40 Hz is rumble on laptop speakers: end an octave higher.
- A cut music cue without its reverb tail cut is not dead silence.
- `ffmpeg fps=1` contact sheets are offset up to 0.5 s: don't misdiagnose a shot boundary.

