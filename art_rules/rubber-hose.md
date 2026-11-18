# 1930s 橡皮管卡通 · 原文美术章节

来源：Lemo-Opuscar by Lemomo (LemoLab)。原文：[STYLE.md](https://github.com/lemomo-ai/lemo-opuscar/blob/00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4/styles/rubber-hose/STYLE.md)。

固定提交：`00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4`。原文 SHA-256：`bf850f9cd22e68b2125fed00d1b9804e91479620b44420ba7ec50e570e472a94`。

本页按章节摘录原作者的美术资料，保留所选章节原文；不是 Blender 原生实现，也不是已经通过的美术验收。原文中的示例、选项和建议保持原有含义，不自动升级为硬限制。某些原文章节顺带包含字幕、流程或声音提醒，它们仍是参考文字，不会加载为 Blender 约束。

文档许可：[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)，另有上游对自有／客户影片制作的额外许可，见[来源说明](../docs/SOURCE_NOTICE.md)。改动：只增加此说明并选择章节，所选原文未改写。

保留章节：1、2、3、4、6、9。

---

## 1. Essence, and what it is not

Hand-inked black-and-white animation from the early sound era: characters with **rubber-hose limbs** (equal-width tubes, no elbows, no knees), **white four-finger gloves**, **pie eyes** (black oval pupils with a wedge cut out), huge round shoes, and bodies that squash and stretch like balloons. The backgrounds are soft grey watercolour paintings; the characters are flat white, grey and ink. Everything (furniture, machines, plants, the walls) **breathes in time with the music**. The film looks like a worn 35 mm print projected in a 4:3 gate: flicker, scratches, dust, gate weave, vignette.

Not a 1950s flat cartoon (no limited animation, no colour, no graphic backgrounds), not a silent film (the synchronised music is the engine), not a "retro filter" over modern animation (no joints, no rendered shading).

## 2. Materials & rendering

- **Frame**: 1920×1080 output with a **4:3 gate** (1440×1080 centred, black pillarbox), gate corners rounded (r ≈ 28 px), soft inner shadow on the gate edge.
- **Characters**: flat fills, one hard-edged form-shadow band (light grey) on the side away from an upper-left light, ink outline **constant in screen space** at any zoom (transform points first, then stroke; ~6 px at 1080p), light **line boil** (±1.2 px, 3 drawings cycling at 12 fps).
- **Anatomy kit**:
  - Limbs: noodle tubes of constant width (about 1/20 of the character's height), one smooth bend, round caps.
  - Gloves: palm + 3 fat fingers + thumb, flared cuff with a fold line, 3 stitch lines on the back. Outline the union only (stroke all parts thick first, then fill all).
  - Pie eyes: white oval, big black pupil (≈ 64 % × 74 % of the eye) with a wedge cut toward the upper right; blink with an eyelid in body colour and a lid line.
  - Mouths: smile with cheek ticks, open grin, "O", wavy (scared), pucker, tongue-out. Shoes: big black ovals with a white toe glint.
- **Object characters**: the face sits on the body; a **secondary feature carries the mood** (steam, a flame, a lampshade tilt, a spring). A box-shaped object is a real projected 3D shape seen slightly from above, the face mapped onto its front.
- **Backgrounds**: painted once into a cached canvas at 1.25–1.5× (push-ins stay crisp): flat wash + soft blotches (±5 %) + inner edge darkening + a thin dark-grey outline + paper grain. They never boil. Period motifs: patterned wallpaper, panelled furniture, checker floors, brick, clapboard.
- **Film damage** (composite pass, not the scene): low-frequency gate weave (±1.2 px) with a rare jump; flicker ±4 %; 0–3 drifting vertical scratches; 3–8 dust specks per frame; an occasional hair; strong vignette; a small jump on every cut; slight blur. Grain in ffmpeg (`mux.sh` grain **3**), not in the page.

## 3. Colour logic

- **Strictly greyscale**: about 6 grey steps plus a separate character white. No hue anywhere, not even in the film damage.
- **Characters own the extremes**: character whites and ink blacks are brighter and darker than anything in the background. Backgrounds live in the middle greys (walls around mid grey, furniture one or two steps darker). Add a mild contrast boost (≈ 1.1–1.15) in the final composite: 1930s prints are rich black and bright white, never flat grey.
- Form shadow is one light-grey band, never a gradient.
- Examples of the grey ramp's temperature: warm paper greys (our demo); cool silver-nitrate greys; a faint sepia print. Pick one and keep it for the whole film.

## 4. Type & subtitles

- **Subtitles are a period title card**: a small near-black plate with a white double-rule border and dot-and-ring corner ornaments; text in **IM Fell English SC** (~36 px), paper white. Drawn in the scene layer so it weaves and flickers with the film; pops on and off with no fades. Bottom by default, top when the action is low. One card may span two short voice clips; hold ≥ max(1.8 s, speech + 0.6 s).
- **Titles**: **Shrikhand** fat retro script, white face, heavy ink outline (~14 % of the cap height), ink drop shadow down-right; letters can hop in a travelling wave on the beat. Sub-lines in **Limelight** caps.

## 6. Camera grammar

A theatre camera: mostly locked, moving only to follow a runner or to land a gag. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Stage-wide, locked, eye level | A proscenium: the set is a stage and everyone on it performs | introducing a place; a group number; a routine |
| Hard cut to a face close-up | The reaction is the joke | a surprise; a taste; a realisation |
| Trucking pan beside a runner, eased start and stop | Pursuit, momentum | a chase; a race; a delivery |
| Medium follow shot (character ≈ 1/4–1/3 of the frame height) | Every step is a note | Mickey-moused climbing, dancing, working |
| Tilt with a fall or a rise | Gravity as rhythm | a tumble; a rocket; a lift |
| Slightly high angle, one unbroken shot | The hazard and the answer in one frame | a danger; a stretch; a rescue |
| Tabletop pan (flat characters in front of a model set turning in depth) | The world is a real place | a street; a carousel; a factory floor |
| Pull-back from a close-up to a packed medium-full | One feeling spreads to everyone | a celebration; a crowd joining in |
| Iris in / iris out (grabbable by a character) | The film is an object | a beginning; an ending; a scene change with a gag |

Framing: faces must read, so no far-wide shot for a gag or a musical moment. The destination prop enters frame before the gag lands. Arcs and leaps stay inside the gate at the current zoom. Transitions: iris, a hard cut on a beat, a title card rolling up like a window shade; no dissolves.

## 9. Pitfalls of the medium

- **Flat grey frames.** Push backgrounds to mid grey, keep pure white and ink for characters, add a contrast boost.
- **Wide shots kill gags**: a far shot makes characters tiny and Mickey-mousing unreadable. Use medium shots, and a packed medium-full for crowds.
- "Sad" brows drawn as "angry": define brows by inner / outer end (inner = near the nose), not by left / right.
- A limb drawn behind a body gets hidden by the silhouette (a handle, a tail): kick and reach outward past it.
- Painted characters collide with background props at some camera positions: check every shot's last frame.
- Smoke puffs in a row read as thought bubbles: scatter and grow them.
- Short voice clips make subtitles flash: merge consecutive lines into one card.

