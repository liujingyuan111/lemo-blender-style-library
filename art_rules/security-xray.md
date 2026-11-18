# 安检 X 光 · 原文美术章节

来源：Lemo-Opuscar by Lemomo (LemoLab)。原文：[STYLE.md](https://github.com/lemomo-ai/lemo-opuscar/blob/00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4/styles/security-xray/STYLE.md)。

固定提交：`00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4`。原文 SHA-256：`fef3d388f119c5e331093b20817b5fa312bb356ae1bacdab5098996fbe3f6321`。

本页按章节摘录原作者的美术资料，保留所选章节原文；不是 Blender 原生实现，也不是已经通过的美术验收。原文中的示例、选项和建议保持原有含义，不自动升级为硬限制。某些原文章节顺带包含字幕、流程或声音提醒，它们仍是参考文字，不会加载为 Blender 约束。

文档许可：[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)，另有上游对自有／客户影片制作的额外许可，见[来源说明](../docs/SOURCE_NOTICE.md)。改动：只增加此说明并选择章节，所选原文未改写。

保留章节：1、2、3、4、6、9。

---

## 1. Essence, and what it is not

- **Transmission, not rendering.** Every pixel is the path length of the X-ray through matter, split by material class. Overlaps change the colour (a cable over clothes turns green), walls glow at their edges, solid metal goes dark.
- **The colour code is the language.** Orange = organic (Zeff < 10), green = mixed or light inorganic (Zeff 10–18), blue = metal (Zeff > 18), black = nothing got through. The legend sits on screen; the audience learns it within seconds.
- **A machine with a person behind it.** The console chrome (lane, belt speed, clock, bag counter, material legend, function keys, status) is always readable; decisions arrive as operator actions on the screen. If there is a voice, it is that operator in the first person: few words, flat, saying only what the screen cannot (a conclusion, a dry aside), never reading out the rule or the numbers already on screen.
- **Things are understood by their insides**: the coil in a hair dryer, the strings of a guitar, the gears in a toy car, the spine of a book.
- **Real rules.** When the image is judged, the rule on screen is a real, sourced regulation.

Not Sci-fi Hologram HUD (no invented glowing chrome: the console is plain, functional, dark), not Exploded Teardown (objects are never taken apart or lit as solids), not Under the Microscope, not a medical scan film (luggage, belts, trays, a checkpoint), not a keynote (no slides, no centred title pages).

## 2. Materials & rendering

- **Thickness pass** (three.js): every mesh double-sided, depth test off, additive blending into a float target. A fragment writes `±distance × density × class`, minus for front faces, plus for back faces, so each pixel holds the path length through organic (R), inorganic (G) and metal (B). Hollow objects are an outer solid plus the same shape shrunk with negative density, which gives walls their real thickness.
- **Every solid must be closed.** An open tube or a missing cap leaves a hole that reads as a dark or bright fleck; cap tube ends, keep winding outward, never mirror with a negative scale (it flips the sign).
- **Dual-energy colouriser** (one full-screen shader): high and low energy attenuation from the three channels; their ratio picks the hue (orange → green → blue), the total sets brightness. Brightness rises with thickness, peaks, then falls towards black, so thick steel is dark blue and a solid block is black. Gradient edge enhancement (the machines' EDGE function), a fine detector grain and scanlines.
- **Two displays.** The screening image is opaque on a navy belt background (so black can read as black); the CT volume is additive glow on the dark reconstruction field. Both use the same material classes.
- **The scan.** A fixed curtain line; the bag moves through it; columns that have passed are in colour, the rest a pale grey preview. Material filters (organic strip, metal strip, high penetration) are wipes across the image.
- **Textures in object space**: weave for fabric, lumps for food, paper and foam, anchored to the object and measured in millimetres so they stay put when the camera zooms.
- **Around the screen**: a dark booth lit by the monitor; through the glass the apron at night (runway, taxiway and floodlights as soft bokeh) for time of day; the machine's tunnel exit and rollers. Everything outside the screen is 2D, parallaxed and out of focus.
- **Post**: bloom from the screen image only, vignette, light grain in the mux.

## 3. Colour logic

- The four material colours are reserved for X-ray matter. UI and annotations never use pure organic orange or metal blue as decoration.
- Neutral ground: near-black navy for the console, a slightly lighter navy for the empty belt.
- Operator colours, one meaning each: amber = flagged / under review, red = refused, green = cleared, pale blue = machine state (scanning, curtain, CT). One verdict colour per screen.
- Text is near-white on dark plates; dim blue-grey for secondary machine text.
- Time of day lives outside the screen: the sky behind the glass (night navy → dawn amber), the runway lights; the screen keeps its colours all night.
- Example (our demo): belt #080F1A, organic rgb(255,133,26), mixed rgb(115,235,51), metal rgb(46,122,255), amber rgb(255,178,58), refuse rgb(255,74,64), clear rgb(96,232,140).

## 4. Type & subtitles

Two voices in type, never mixed:

- **Machine voice**: a monospace (e.g. IBM Plex Mono, OFL), 15–22 px for chrome, 56–64 px for the clock and counter, about 32 px for the status word. **English only**, upper case for states and keys, as a real console would print it: legend (ORGANIC / MIXED / METAL / OPAQUE), status (SCANNING, REVIEW, CLEAR, BAG CHECK, UNCLEAR, STANDBY), view labels, the CT header.
- **Operator voice** (labels, rules, verdicts): a CJK sans (e.g. Noto Sans SC, OFL, subset to the characters used) at **34–44 px** on screen, bold, with the English line under it in the monospace at 17–22 px. One line per language. A label that cannot hold 34 px Chinese is written in the machine voice instead (English only).
- Labels attach to the object with a leader line or sit in a panel beside the image; verdicts are stamps (tick or cross, word, English line) that land after the hold.
- Every image carries its stamp (bag number, time): it keeps the clock visible in tight shots.
- Nothing the viewer must read under 18 px at 1080p; legends and chrome may go to 15 px. Sizes are on screen: when the outside camera pulls back (scale < 1), anything the viewer must read waits for the push in, or is set larger.
- **Subtitles** (when there is a voice) are the operator's log: a dark plate fixed to the frame's bottom left (not to the console, so it never moves with the camera), a thin white bar on its left edge, Chinese 36 px over English 24 px in the monospace, one line each. Keep panels, verdict stamps and judged objects out of that corner: panels sit top right of the image, the CT verdict bottom right. Cues less than about 0.6 s apart share one plate (the text changes, the plate resizes), so it never blinks off and on between lines.
- Holds: a judged frame shows object, rule, number and leaves 2.5 s before the verdict; verdicts stay ≥ 1.5 s; labels ≥ characters ÷ 4.5 + 1.5 s.

## 6. Camera grammar

Two cameras: one outside the screen (2D, over the booth and the monitor), one inside the X-ray (zoom on the image, or a CT orbit).

| Move | What it expresses | Can serve |
|---|---|---|
| Wide booth, window behind | place, time of day | an opening; the hour changing; an ending |
| Push from booth into the screen | attention narrowing | the next bag; a shift starting |
| Tight crop on part of the console | one object, one reading | a montage; a counter or clock |
| Operator zoom inside the image | suspicion | a flagged object |
| Locked frame with a panel | judging | a rule, a measurement, a verdict |
| CT orbit with push | seeing in 3D what the flat image hid | a reveal; a hidden mechanism; a living thing |
| Pull back to the window | consequence, time passing | dawn; the end of a run |

Subject at least a third of the view when it is judged; panels on the side away from the object; never cover the object with text.

Transitions come from the machine, never a hard jump in brightness:
- **Between bags: the scan sweep.** The next picture comes in behind a thin X-ray scan line moving the belt's way (right to left), the old picture held on the other side; short (about 0.2 s) on the beat in a montage, 0.3–0.6 s for a new judgment or a jump in time. No crossfades, no white flash frames.
- **Filters and rescans** are wipes of the same kind inside the image.
- **Into CT** a short digital tear, kept dim (the reconstruction settles out of noise; no frame much brighter than the CT that follows); out of CT a scan sweep back to the console.
- **Wide ↔ close** at the booth is a camera move, not a cut: push into the screen, pull back to the window. When the outside camera crosses the scale where the monitor fills the frame, keep drawing the window behind it so nothing pops.
- List rows and panels arrive behind a reveal line, not with a flash band.

## 9. Pitfalls of the medium

- **Wrong colours for the material.** Aluminium is green-blue, steel blue, lithium cells blue-green, glass and bone green, water and food orange. Check every prop's class; a black area must be a genuinely thick, dense object.
- **Clutter.** Too many overlapping objects turn into mud. Keep 4–8 readable objects per bag, iconic shapes (keyboard grid, coil spring, J-hook) and vary the classes.
- **Thin things vanish** (a strap seen flat, a 1 mm plate): raise density or thickness until it reads at the shot's scale.
- **Open meshes and mirrored meshes** produce flecks and negative thickness (see §2).
- **Text over the image.** Panels go beside the object; dim the image outside the operator's box rather than covering it.
- **Flat side view.** Low objects look like a strip in the side view; use it for tall or layered things, not for crops.
- **Facts.** Screening rules differ between domestic and international flights and between airlines; quote the exact rule for the route you show, keep FACTS.md with source URLs and wording.
- **Render state.** Set a render target's viewport and scissor before binding it; a stale viewport squashes the image and makes frames depend on render order.
- **Brands.** No manufacturer names, logos or real products in the console or on labels.
- **Chrome in two languages.** Bilingual chrome (a Chinese legend at 20 px) drops under the readable size and clutters the console; keep chrome English and give Chinese only to the operator's labels, at full size.

