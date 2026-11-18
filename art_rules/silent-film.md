# 1920s 默片 · 原文美术章节

来源：Lemo-Opuscar by Lemomo (LemoLab)。原文：[STYLE.md](https://github.com/lemomo-ai/lemo-opuscar/blob/00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4/styles/silent-film/STYLE.md)。

固定提交：`00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4`。原文 SHA-256：`44633a4edd4ec6b84be809bd48b38503a75a71531112b3d28a52f27135012b20`。

本页按章节摘录原作者的美术资料，保留所选章节原文；不是 Blender 原生实现，也不是已经通过的美术验收。原文中的示例、选项和建议保持原有含义，不自动升级为硬限制。某些原文章节顺带包含字幕、流程或声音提醒，它们仍是参考文字，不会加载为 Blender 约束。

文档许可：[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)，另有上游对自有／客户影片制作的额外许可，见[来源说明](../docs/SOURCE_NOTICE.md)。改动：只增加此说明并选择章节，所选原文未改写。

保留章节：1、2、3、4、6、9。

---

## 1. Essence, and what it is not

A one-reel film as it would look *projected*:
- **A 4:3 print in a gate between theatre curtains**; the sides of the 16:9 frame are the picture house.
- **An ink drawing with washed greys and hatching**, printed on silver stock that flickers, weaves, scratches and burns at the edges.
- **Nobody speaks.** Beats are told by **action in wide shots** and by **intertitle cards**.
- **The only sound is a cinema instrument** (piano, organ) and the projector in the booth.

Not a noir (no hard shadows as mood, no voice-over), not a sepia photo filter on modern animation (the drawing itself is engraved and inked), not a Chaplin pastiche.

## 2. Materials & rendering

- **Tonal painting + Redraw.** Scenes are painted in grey values only (print densities roughly: ink 0.07, dark cloth 0.15–0.3, mid wood 0.45–0.6, skin 0.8, white linen 0.9–0.95), with soft light gradients and a thin separation line. A **Redraw** pass (WebGL2) inks the whole frame: difference-of-Gaussians contours on the dark side of every edge, luminance posterised into ~5 soft wash steps, and 45° hatching (then crossed) in the darks, re-drawn every two frames like hand-redrawn animation. Real video frames can go through the same pass so footage and drawing share one hand.
- **Print pass**: silver tone with a sepia amount between ~0.1 and ~0.36, print black ~0.055 and white ~0.93, S-curve, halation on highlights, uneven density, flicker, gate weave with occasional perforation jumps, broken vertical scratches (white = scraped emulsion, dark = dirt on the negative), brown burn creeping from the edges, vignette, two-octave silver grain; then dust, a hair in the gate, a rare blotch.
- **Frame**: 1440×1080 in the centre of 1920×1080, a rounded aperture with a soft dark rim; velvet drapes at the sides lit by the screen's spill and by footlights. Curtains can part and close.
- **Figures**: realistic proportions (7.5-head adults, ~5-head children) on a 2.5D rig (joints solved in 3D, projected with a yaw), silent-era make-up (pale skin, dark lids and lips); identity by silhouette marks (a hat, a garment, a tool).

## 3. Colour logic

- **Monochrome silver**, tinted only by the print: colder and harsher (more damage, less sepia) when things go wrong, warmer and cleaner when the film turns tender. Tint and damage are mood controls, set per section.
- Values carry everything: dark clothes against pale walls, pale faces against dark interiors; check every shot as a thumbnail.
- **One colour, at most**: an element drawn into a separate colour mask keeps its hue through the print (still getting grain, flicker, vignette). Use it for the single thing the film is about, or not at all.
- Period tinting of whole scenes (amber for day interiors, blue for night, rose for romance) is a valid alternative to sepia; one tint per section.

## 4. Type & subtitles

- **The intertitles are the subtitles**; the `.srt` lists their text. A card holds 2.5–3.75 s (≥ max(1.8 s, reading time + 0.6 s)).
- A black painted card with a deco border whose ornament follows the emotion: one heavy rule for a shout (the text shakes), a double rule with stepped corners and fans for narration, vines and small flowers for tenderness.
- Period faces (OFL): a small-caps display serif (e.g. Playfair Display SC) for titles and shouts, an italic old-style serif (e.g. Old Standard TT Italic) for narration and dialogue.
- A few words per card; three to five cards in a short film. A card never explains what the picture already shows.

## 6. Camera grammar

A vocabulary, not a route. The period camera is heavy: most shots are locked. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Locked-off extreme wide | cause and effect seen whole; the wait is the joke | a mechanical gag; a crowd; an elaborate process |
| Locked full shot | the premise in one frame | a character's routine; a confrontation |
| Tracking shot with foreground passing | pursuit; momentum | a chase; a race; a delivery against the clock |
| Iris in / out | attention on one thing; a beginning or end of a thought | an object; a face; a memory |
| Half-open iris, held | a character sharing a look with the audience | a wink; a secret; complicity |
| Slow motivated push-in | tenderness; realisation | a kneel; a letter read; a decision |
| Masked shot (keyhole, binoculars) | point of view; spying | a detective; curiosity; romance |
| Split screen / double exposure | trickery; dream; two places at once | a phone call; a ghost; a daydream |

Framing: wide and medium shots; big close-ups of rigged faces look like mannequins, so keep any close-up small or inside an iris. Transitions: iris, fade to black, straight cuts, the curtain. No dissolves between shots of the same scene, no modern whip pans.

## 9. Pitfalls of the medium

- **Too much content kills a silent film**: a many-step chain at small figure scale is noise in a thumbnail. One legible chain with a pause in the middle beats three busy ones.
- **Puppet arms**: apply abduction before flexion, let the shoulder rise and swing forward as the arm goes up, slim the torso's shoulder corner on the raised side, hide the arm's contour where it lies over the torso. Raise arms sideways (or turn the figure) so they don't cross the face.
- **Pose pops**: drive every figure by eased keyframe lists, never by `if` branches.
- **Floating props**: hold a prop between the palms at the depth between the arms; tie a rolling object's rotation to distance (angle = distance / radius).
- Brow angles flip with facing direction: check expressions in a crop at final size.
- An iris must track its target in film coordinates after any camera zoom.
- A grab must put the hand exactly where the object is at the beat, or it doesn't read.
- Closed curtains lit only by a dark screen go pure black: add footlights.
- Heavy grain makes huge files → re-encode with `-tune grain` at a higher CRF.

