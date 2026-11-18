# 剪影律动 · 原文美术章节

来源：Lemo-Opuscar by Lemomo (LemoLab)。原文：[STYLE.md](https://github.com/lemomo-ai/lemo-opuscar/blob/00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4/styles/silhouette-rhythm/STYLE.md)。

固定提交：`00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4`。原文 SHA-256：`66f1a0f7d44ad1067960046514336bb4d19fce9799a16ec1591696343987a291`。

本页按章节摘录原作者的美术资料，保留所选章节原文；不是 Blender 原生实现，也不是已经通过的美术验收。原文中的示例、选项和建议保持原有含义，不自动升级为硬限制。某些原文章节顺带包含字幕、流程或声音提醒，它们仍是参考文字，不会加载为 Blender 约束。

文档许可：[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)，另有上游对自有／客户影片制作的额外许可，见[来源说明](../docs/SOURCE_NOTICE.md)。改动：只增加此说明并选择章节，所选原文未改写。

保留章节：1、2、3、4、6、9。

---

## 1. Essence, and what it is not

- **The figure is one black shape.** No detail inside it, no gradient, no outline, no shadow. Everything the viewer reads is in the contour.
- **There is always light behind it**: the sun disc, the bright band of the horizon, the glitter on the water. A silhouette sits on light, never on dark.
- **Poses land on the beat** and hold between beats. A group moves in unison; anything off the beat is a deliberate choice of the story.
- **The freeze**: on the key beat the figures, droplets, ripples and clouds stop; the sky's colour and the sun keep going.
- **The sky is the clock**: the colour sinks from gold to magenta to violet as the story moves, and the sun goes down with it.

Not Shadow Puppetry (no visible rods, no paper texture, no lamp behind a screen), not Paper-cut Lightbox (no layered paper, no inner light), not Red Paper-cut (no ornament inside the shape), not a sunset stock photo (the figures act, on a grid).

## 2. Materials & rendering

- **Three 2D layers composited in one fragment shader**: silhouettes, their reflections, water light (ripples and droplets). The shader paints the sky, the sun and the water, then lays the layers over it.
- **Sky**: two vertical colour ramps (gold-to-crimson and magenta-to-violet) blended by one story-phase value; perspective cloud streaks lit on their sun-facing edge; a sun disc with a warm glow and a horizontal flare band.
- **Water**: the sky reflected with wobble from two noise octaves anchored to the world, a glitter column under the sun, darker towards the camera. Reflections of figures are the same shapes flipped about the waterline, wobbled and darkened.
- **Light around the figures**: volumetric rays marched from each pixel toward the sun (56 steps) and occluded by the silhouettes; a thin rim on the sun-facing edge and a soft halo, stronger near the sun.
- **Ripples** have a bright crest (in the water-light layer, tinted by the sky) and a dark trough (in the reflection layer), so they read on bright and dark water alike. **Droplets** are bright beads, never black specks.
- **Camera**: a level pinhole over flat water (focal length, horizon height, camera height, lateral and depth offset, yaw). Long focal lengths make the sun huge; the horizon height frames the shot.
- **Screen space only for** the end card and a true directional motion blur on whip pans (many samples along the motion, at full resolution).
- Light film grain at the master; nothing else in post.

## 3. Colour logic

- Two values carry the frame: black figure and bright ground. Everything else is the sky's gradient.
- The figure colour is fixed: near-black with a trace of violet. It never takes a hue.
- The sky moves through warm hues only (gold, orange, coral, crimson, magenta, violet). No green, no blue sky, no grey.
- Brightest values belong to the sun, the horizon band and the light on the water; type uses the sun's cream, never pure white.
- Colour change is time: plan the story's moments against the sinking sun (high, touching the horizon, half, a sliver).

Example (our demo): figure #090307, sun #FFF6DC, gold #FFB347, coral #FC4D2B, magenta #E0245C, violet #380A52 → #1A083D.

## 4. Type & subtitles

- **Roles**: a heavy condensed sans for the title (120–150 px, e.g. Anton), a condensed sans for small lines (30–40 px, e.g. Barlow Condensed), a bold CJK sans for Chinese (≥ 34 px, e.g. Noto Sans SC). OFL, self-hosted, subset to the characters used.
- Cream on the dark lower water, left-aligned in the lower third, never inside the sun, never centred, no shadow or stroke.
- **Type lands on the beat**: one word per beat, each landing with a small ripple on the water under it. One word may land late or early on purpose.
- Subtitles, when the film speaks: one line per language on the water at the bottom left, the same cream, clear of the figures; hold ≥ max(1.8 s, speech + 0.6 s).

## 6. Camera grammar

| Move | What it expresses | Can serve |
|---|---|---|
| Telephoto, sun filling half the frame | intimacy, a single gesture at its clearest | an introduction; a decision; a held breath |
| Low lateral track at water level | a group moving together, legs and splashes | a march; a chase; a procession |
| Side view, slow pan | a sequence happening in order | a cascade; a departure; a relay |
| Whip pan with directional blur | a sudden change of attention | "meanwhile"; a reveal of who was left behind |
| High wide, slow pull back | scale and solitude | aftermath; loneliness; a pause with no beat |
| Locked medium | the beat itself, counted | a count-in; a ritual; a joke landing |
| Orbit inside a freeze | the moment that matters, seen from around it | a climax; a record; a memory |

Framing rules: at the key moments the subject fills ≥ 1/3 of the frame height; a wide shot keeps the subject on light (in the glitter column or against the horizon band). Transitions belong to the medium: a near silhouette walking across the lens (a black wipe), a match cut on the same pose, a whip pan, a cut straight into a freeze. No dissolves, no page turns.

## 9. Pitfalls of the medium

- **Black on dark.** A silhouette over dark water or a violet zenith disappears. Put it in the glitter column, against the horizon band or in front of the sun.
- **Merged shapes.** Overlapping figures become one blob; at key moments leave air between contours and keep limbs in profile.
- **Unreadable spread shapes.** Open wings or limbs seen face-on lose the species or the person. Prefer profile; for birds, show flight from the side (neck forward, legs back), not a V above the body.
- **Puppet humans.** A naive forward-kinematics human reads as a marionette. Hand-key a small set of anatomically correct poses and blend them, or use animals.
- **Tiny subject in the wide.** If the subject must be small, make that the point (solitude) and keep it on light; otherwise cut closer.
- **Blocky blur.** Never fake motion blur by downscaling and upscaling the frame; sample along the motion at full resolution.
- **Cutting on every beat.** The beat lives in the poses; cuts follow sections.

