# 文字闪切 · 原文美术章节

来源：Lemo-Opuscar by Lemomo (LemoLab)。原文：[STYLE.md](https://github.com/lemomo-ai/lemo-opuscar/blob/00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4/styles/text-flash-cuts/STYLE.md)。

固定提交：`00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4`。原文 SHA-256：`f69fa08818c5d41099abe29c8afdd0a9f3ef89746d379346dc9bf384adbd1299`。

本页按章节摘录原作者的美术资料，保留所选章节原文；不是 Blender 原生实现，也不是已经通过的美术验收。原文中的示例、选项和建议保持原有含义，不自动升级为硬限制。某些原文章节顺带包含字幕、流程或声音提醒，它们仍是参考文字，不会加载为 Blender 约束。

文档许可：[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)，另有上游对自有／客户影片制作的额外许可，见[来源说明](../docs/SOURCE_NOTICE.md)。改动：只增加此说明并选择章节，所选原文未改写。

保留章节：1、2、3、4、6、10。

---

## 1. Essence, and what it is not

Three layers, and the collision between them is the look:
- **Type as picture.** A word fills the frame, bleeds off an edge, or stands in a vertical column. Cards are dialogue, chapter titles and punctuation of the cut.
- **Symbolic architecture.** Stairs that never end, window grids, lockers, a one-point street: flat polygons, no props, no sky, no texture.
- **Flat characters in three states only**: black silhouette (far), flat cel colour (mid), fragment (an eye, a hand, a mouth corner) filling the frame.

It is not a lyric video (type is not synced to a song and never animates letter by letter), not a manga panel film (no speech balloons, no screentone), not a horror film (no gore, no blood; dread comes from cutting, silence and stillness), and not a slide deck (never centred text on a plain card followed by a page-turn).

## 2. Materials & rendering

- Characters: generated cel art, clean thin uniform black lines, completely flat fills with a single hard shadow tone, no gradients, no paper grain. Keyed from a chroma-green background into RGBA; any pure generated red is pulled to the film's red.
- Everything code-drawn is hard-edged polygons on Canvas 2D. No blur, no glow, no grain (mux grain 0). The only smear is the head-tilt ghosting (three 28 % copies of the head layer).
- Silhouettes are the same art filled with one colour (`source-in`), so a character can be black, white or red without new images.

## 3. Colour logic

| Name | Value | Use |
|---|---|---|
| Red | `#d4162b` | the protagonist's rail, card fields, rails of light, the main prop, accents |
| Black | `#0a0a0c` | walls, silhouettes, the second character's rail, the end card |
| Paper white | `#f2efe8` | treads, windows, card fields, type on black |
| Grey | `#8d8a84` | English lines only (on black or white) |

Secondary values only for depth inside geometry: `#d8d4cc`, `#26262a`, `#1b1b1f`. Skin and hair in generated art are the only other colours.
- **Inversion is red-black swapping, never RGB inversion** (RGB inversion makes cyan): grayscale → contrast(5) → invert → multiply red. White becomes black, black becomes red. Used as 1–6-frame accents on impacts, never as a look.
- Each speaker owns a field colour (for example: protagonist = red rail, black type; second character = black rail, white type). Keep it fixed through the film so the audience reads who speaks without voices.

## 4. Type

- Cards and titles: **Noto Serif SC 900** (heavy Mincho feel, OFL). Single glyphs 700–1100 px, allowed to bleed off the frame on flash cards; dialogue columns 120–170 px, never bleeding.
- Small vertical notes (episode numbers, speaker tags, counters): Noto Sans SC 900, 40–64 px.
- English: one line of **Cormorant Garamond Italic 600**, about a quarter of the Chinese size, grey on black or white, black on red.
- Vertical punctuation: 。and ，move to the top right of their cell; ？stays upright.
- Never centred on the frame. Type sits in a corner, on a rail at the edge, on an object (a letter), or bleeds.
- Two classes of text: **flash cards** (2–9 frames, deliberately below reading time, only ever repeat or fragment words that are also shown in full) and **held lines** (dialogue, a letter, the end card), each held for its full reading time and checked with `readcheck.mjs`.

## 6. Camera grammar

| Move | What it expresses | Can serve |
|---|---|---|
| Fast push into a one-point corridor, stairs or street, perfectly symmetric | inevitability, being drawn in | a summons; a chase; a countdown |
| Extreme offset: subject at one edge, half the frame empty | isolation, something missing | a back turned; waiting; absence |
| Hard push into one element of a grid (a locker, a window) | this one, out of many | a choice; a clue; a name on a list |
| Lateral track along an orthogonal wall | searching, passing time | a corridor; a facade; an archive |
| Beat-locked step push (the camera jumps one step per beat) | effort, climbing | ascent; levels; progress |
| Low angle from below a figure at the top of a space | power, the end of a path | a confrontation; a destination |
| Insert at 1:1 scale (an eye, a hand, a letter) held under a slow push | intimacy, threat | a reveal; a touch; a message |
| Multi-panel grid of one face cropped many ways | obsession, surveillance | a stalker; a crowd of selves; memory |
| Split frame: picture on one side, a speaker's rail on the other | dialogue without lips | a phone call; an interrogation; a confession |

Cut on beats. Transitions are cuts, 1–6 frames of inversion, a one-point tunnel rush, or a red slit opening on black. Never dissolves, wipes or page turns, and never a fully black frame between shots (use the slit).

## 10. Pitfalls of the medium

- RGB inversion turns red cyan → red-black swap (§3).
- A large head rotation shows a gap at the neck → only rotate far while the figure is a silhouette; in colour stay within 0.1 rad.
- A black silhouette in a black doorway disappears → doorways are white.
- A half-body image standing in a long shot "breaks at the waist" → generate a full-body back view for long shots.
- Flash cards counted as dialogue fail the reading check, and cutting away from a held line resets its clock → hold lines on rails or objects while the picture beside them cuts.
- Centred cards on plain fields read as slides → always bleed, offset, rail or object.
- Generated red (`#ff0000`-like) breaks the palette → pull saturated reds to `#d4162b` when preparing assets.
- Steady drones and pads fill the silences → gate everything but one sound before the peak.
- Very sharp hits plus loudness normalisation overshoot the peak → limit the mix before `mux.sh`.
- A subset font misses a new glyph and Canvas falls back to a system serif → build the subset from the source text (`tools/fonts.sh` collects every non-ASCII character in `main.js`).

