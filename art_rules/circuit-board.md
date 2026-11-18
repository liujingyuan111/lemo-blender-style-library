# 电路板 · 原文美术章节

来源：Lemo-Opuscar by Lemomo (LemoLab)。原文：[STYLE.md](https://github.com/lemomo-ai/lemo-opuscar/blob/00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4/styles/circuit-board/STYLE.md)。

固定提交：`00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4`。原文 SHA-256：`3f5244726e732a8407355bebdec309942410104af32c956372ff4f1477a0cd9b`。

本页按章节摘录原作者的美术资料，保留所选章节原文；不是 Blender 原生实现，也不是已经通过的美术验收。原文中的示例、选项和建议保持原有含义，不自动升级为硬限制。某些原文章节顺带包含字幕、流程或声音提醒，它们仍是参考文字，不会加载为 Blender 约束。

文档许可：[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)，另有上游对自有／客户影片制作的额外许可，见[来源说明](../docs/SOURCE_NOTICE.md)。改动：只增加此说明并选择章节，所选原文未改写。

保留章节：1、2、3、4、6、9。

---

## 1. Essence, and what it is not

- A top-down board in every frame: copper pour with clearances cut around everything, traces with 0/45/90° runs and mitred corners, gold pads and vias, white monoline silkscreen. Nothing is drawn in perspective.
- Information moves as light on copper. The way the light moves *is* the explanation: a pulse, a stream, a rocking dash, a pad that flashes.
- Two scales on one board: whole regions (a map, a supply chain, a city) are drawn in the same language as single components, and the camera passes between them without changing medium.
- Only real things are drawn. Every trace, pad and label stands for something in the subject; empty copper is filled with what boards really have (stitching vias, via fences, solder-mask mottling), never with decorative routing.
- Not the library's Engineering Briefing Board (a whiteboard on which real photos are pinned and written over in marker): here there are no photos and no handwriting; the subject itself becomes copper, pads and silkscreen, and information travels as light along the traces. Not a blueprint (no white-on-blue linework, no paper), not a sci-fi HUD (no glass, no floating panels, no glowing UI chrome), not a 3D circuit "city" (no buildings rising, no perspective).

## 2. Materials & rendering

Layers bottom-up, all in board space under one world → screen camera:
1. **Laminate (FR-4):** dark green, a glass-weave basket texture in two crossfaded octaves so its on-screen size stays bounded at every zoom. Bottom-layer copper may show through faintly.
2. **Copper pour:** fills the board; everything is a **clearance** punched out of it (channels, lakes, sea, keep-outs around parts and traces). Rendered twice: a lighter rim pass with the plain clearance, then the fill pass with the clearance grown by ~1.6 px, so every copper edge gets a bevelled rim. A soft mottling texture sits only on the pour (solder mask is never perfectly flat).
3. **Traces:** rim colour stroke + narrower fill stroke, round caps; a channel of bare laminate runs on both sides (the clearance). Parallel traces keep the pour out of the gap between them when they are a pair.
4. **Exposed metal:** ENIG-gold pads (rect, round, square pin-1) with a sheen band on the top third and a dark drill hole; vias are gold rings with dark bores; bare copper (salmon with a vertical gradient and brushed streaks) only for one heavy, special part. Fiducials and mounting holes at board corners.
5. **Silkscreen:** off-white monoline strokes with a pinhole texture punched out, slightly blurred (0.35 px). Outlines, designators, polarity marks, component symbols, labels.
6. **Light:** an additive layer (glow) with two blurs (≈24 px and ≈5 px) under a sharp copy. Current, water, lit pads all live here.
7. **Screen space (once per frame):** a soft warm key light drifting from the upper left, shallow depth of field (a blurred copy faded in at the top and bottom bands, stronger in macro shots, weak or off where text must be read), out-of-focus motes of light drifting with parallax in front of the board, a vignette, film grain at mux. A window's light (a soft parallelogram with a mullion shadow) may fall on the board when the whole board is on a desk.
Level of detail: textures crossfade between octaves; small features (vias, designators, rims) fade out before they go sub-pixel, so zooms never shimmer. Nested boards (a module inside a board) are separate boards composited into their footprint, so a continuous zoom can cross six or more orders of magnitude without precision loss.

## 3. Colour logic

- Ground: green solder mask in three values (dark laminate, mid pour, light rim/trace). The film is green; never recolour the mask per scene.
- Metal: gold for pads and vias, one bare-copper accent at most.
- Ink: one off-white for all silkscreen.
- Light carries meaning and is the only saturated colour: **amber** for energy/current (with a near-white core), **silver-cyan** for a second kind of flow (water, data, goods) when the story has two. A third flow gets a third light colour only if it must be told apart; red is reserved for a fault and appears at most once.
- Dark (bare laminate, sea, holes) for what is absent.
Example: laminate #05190F, pour #1C6A44, rim #4AA977, gold #D9B25B, silk #F2EEE1, current (255,190,84), water (170,214,226).

## 4. Type & subtitles

- All type is silkscreen in one **monoline stroke font routed like traces** (0/45/90° strokes, chamfered corners, round caps), drawn in code. Chinese uses the same rules: every hanzi hand-routed on a 0/45/90° grid with the same stroke width as the Latin line beside it. Use simplified characters only and proof every glyph at large size before use.
- Text is world-anchored and **plotted stroke by stroke**; it stays on the board and is still there when the camera pulls back.
- Roles: labels (a Chinese line above a smaller English line, same stroke width), board-native text in one language (designators, voltages, timestamps, km, values), micro texture (pinyin tags, notes, REV/sheet lines) which may fade below reading size.
- Reading: a label must be fully in frame and stay there for its reading time (≥ 1.5 s + characters at 4.5/s CJK, 15/s Latin). Never let text sit in the depth-of-field bands; never cut text at the frame edge in a held shot. Title caps ≥ 60 px at 1080p.
- Moving camera: `readcheck.mjs` starts a label's clock when it is first fully in frame and stops it the first time it leaves, so a label that slides out during a ride or whip fails even if it comes back. Before plotting a label, check where the camera path takes it for its whole reading time: place it where the path keeps it in frame, print it once the camera settles, or let it be micro texture (under ~9 px tall it is not reported).
- Glyph coverage: the routed font draws only the characters it has. The demo's `hanzi.js` holds just the hanzi its film needed, and the Latin set is capitals, digits, common signs and a few lowercase letters (`a b d e k l m o p s u z`, enough for units like ms, km, kV). A missing character prints as `?` with no error. Check every label string against the font before building, write English labels in capitals (or add the lowercase you need), and route the hanzi you lack (§10, New hanzi).
- With a voice, every line gets a subtitle in the bottom safe area: a dark translucent plate, Chinese over English (an open-licence sans, e.g. Noto Sans SC, subset to the characters used; never a system font), 34 px / 24 px at 1080p. The board then prints only the voice's key words and numbers, never whole sentences. Keep picture text above the subtitle band.

## 6. Camera grammar

Straight-down camera always (rotation about the view axis allowed, small). Moves:

| Move | What it expresses | Can serve |
|---|---|---|
| Ride the pulse (camera locked to a moving head, head on a third) | following one thing through a system | a delivery route; a signal path; a single order through a process |
| Rise while following (zoom out during the ride until both ends are in frame) | the whole length becomes visible | a distance; a supply chain end to end; a timeline |
| Crash zoom onto a pad | arrival, impact | a deadline met; a package delivered; a test result |
| Locked macro hold | reading, comparing, verdict | two numbers side by side; a spec; a rule |
| Whip along a trace | jump to the next station | the next stage; skipping ahead |
| Matched cut on a centred symbol (same symbol, same screen size, the world around it changes scale) | the same step repeated at every level | step-downs; repeated approvals; hand-offs |
| Plunge through a hole / via, reverse out of another hole | entering a smaller world | into a device; into a building; into a file |
| Continuous pull-out across nested boards | everything was one board | the big picture after the detail; the system behind one object |

Framing rules: the lit subject sits on a third or dead centre for symbols; at least two layers of detail around it (background copper/vias/routes, foreground motes or depth-of-field blur); the board edge appears only when the whole board is the subject. Transitions: motion-into-motion and matched cuts; no fades, no wipes, no page turns.

## 9. Pitfalls of the medium

- **Flat pour.** A board that is all mid-green reads as an empty slide. Fill with real board texture: stitching vias that stay visible at map scale, fences along every clearance, mottling, micro silk, other unlit routes that exist in the subject.
- **Decorative routing.** Traces that mean nothing make viewers ask what they are. Draw only real routes; texture comes from vias and mask, not invented traces.
- **Lines crossing on one layer.** Two traces can't cross on the same copper: use a via to the bottom layer, or route around. A trace may cross a bare channel (a river, a street).
- **Overexposed light.** Wide traces with additive bloom turn into white bars. Cap glow widths and flash radii in pixels, keep the amber body and a thin core.
- **Text in the blur or under the frame edge.** Depth of field and the vignette eat the top and bottom bands: keep labels out of them, or turn the blur down in reading shots.
- **Too-fast holes.** A plunge into a hole under 0.6 s reads only as "darkness". Hold on the hole first, then plunge; come out of another hole the opposite way.
- **Precision.** Zooming a single coordinate system over many orders of magnitude breaks the canvas transform. Nest boards (each with moderate units) and convert cameras between levels in double precision.
- **Hanzi in a stroke font.** Automatic skeletons of fonts lose dots and strokes; route each character by hand and proof traditional/simplified forms (鹤 not 鶴, 换 not 換). A glyph that only works at small size (one component missing, two strokes merged) reads as another character on a title: proof it large (§10).
- **The board edge by accident.** When the camera's view comes near the board outline, `Board` switches to drawing the desk and clips to the board, so a close shot near the edge suddenly shows black desk. Keep the view well inside the outline (the check uses the frame's half-diagonal plus 4% of the board width), or make the board larger than the shot needs; show the edge only when the whole board is the subject.

