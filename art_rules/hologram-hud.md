# 科幻全息界面 · 原文美术章节

来源：Lemo-Opuscar by Lemomo (LemoLab)。原文：[STYLE.md](https://github.com/lemomo-ai/lemo-opuscar/blob/00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4/styles/hologram-hud/STYLE.md)。

固定提交：`00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4`。原文 SHA-256：`81e2c6b0ede2cc211a8dd676417a1ce5efda278514f273c5249165e38ff34573`。

本页按章节摘录原作者的美术资料，保留所选章节原文；不是 Blender 原生实现，也不是已经通过的美术验收。原文中的示例、选项和建议保持原有含义，不自动升级为硬限制。某些原文章节顺带包含字幕、流程或声音提醒，它们仍是参考文字，不会加载为 Blender 约束。

文档许可：[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)，另有上游对自有／客户影片制作的额外许可，见[来源说明](../docs/SOURCE_NOTICE.md)。改动：只增加此说明并选择章节，所选原文未改写。

保留章节：1、2、3、4、6、9。

---

## 1. Essence, and what it is not

The subject is always a **line wireframe made of light** above a round projector pad on a near-black stage, never a rendered object. Everything reads as *scanned data*: a scan plane grows the model, parts pull apart along their assembly axes, numbers are *computed* on screen.

Three depth layers are always present: a **background dot grid** (slow parallax), the **subject** with its pad and floor, and the **foreground HUD** (corner brackets, rulers that parallax faster, status text).

Not a type-driven keynote (dark-keynote), not a drafting sheet (blueprint), not a product render (glass-product). The subject stays a wireframe; it may gain translucent faces once, and even then the lines stay on top.

## 2. Materials & rendering

- **Stage**: near-black tinted by the hue, a radial lift behind the subject, a fading dot grid, a strong vignette.
- **Projector pad** in true perspective: concentric rings (one bright, one dashed), ticks, faint rays; it rotates slowly and spins with any turntable move.
- **Wireframe**: additive ~1.3 px strokes in a few alpha levels set by **depth fog** (near bright, far ~25 %), plus two low-res glow passes.
- **Hot edges** (near-white of the hue) only for what matters now: the scan front, inner pieces flagged `hot` when opened, a light wave, a part being pinged.
- **Real CAD topology**: tubes are rings plus longitudinal lines. **Every part is physically connected**: a floating piece is noticed first.
- **Solid hologram**: faces filled with a screen-space **Fresnel** × a scrolling **interlace**; lines thicken as it ignites; a light wave climbs the model. A **beam** (one path, nonzero winding) with faint rays and dust.
- **HUD furniture**: corner brackets, parallaxing rulers, subject // mode top left, a live status line top right, telemetry at the bottom.
- **Text never sits on the wireframe**: every text block has its own **dark plate** (translucent near-black, 1 px border, corner ticks); the camera still keeps the subject clear of text.

## 3. Colour logic

- **One cold hue plus one warm accent**, both parameters (e.g. mint/orange, violet/lime, ice-blue/red; choose from the subject).
- The hue carries lines, HUD and fills. The **accent is spent on locked values only**: a number turns accent-coloured at the frame it becomes true. Nothing else ever uses it.
- White is heat: near-white edges and one-frame flashes mark what is active. Everything at rest sits in the hue's alpha levels.
- One object may keep its own colour (the single-colour exception, `keep`), for a brand mark, never for decoration.

## 4. Type & subtitles

- Rajdhani, all caps: Light for big numbers and the product name (wide tracking), Medium/SemiBold for labels. Share Tech Mono for micro data (coordinates, counters, zoom).
- Numbers are **monospaced** so rolls never jitter; the decimal point is a small square (a glowing "." reads as a comma).
- Subtitles are HUD: a dark plate with corner brackets and "voiceprint" bars moving with the speech, near-white Rajdhani Medium, bottom centre; in just before the voice, hold ≥ max(1.8 s, speech + 0.6 s).
- The title is part of the scene (no title card): the name rolls in like a value, then code, category and tagline.

## 6. Camera grammar

An orbit camera (yaw, pitch, distance, narrow fov) with a screen position for the target, so the subject can sit beside text. A vocabulary, not a route. Opening and ending come from the topic.

| Move | Expresses | Can serve |
|---|---|---|
| High 3/4, slow orbit craning down | Examination; a scan plane reads as an ellipse | a scan-in; a survey |
| Top-down plan view | Layout, order | a parts inventory; an assembly sequence |
| Eye-level profile, locked | The object as it stands in use | a height; a before/after |
| Push-in, then drift, 3/4 | This part matters; internals come towards the lens | the key spec; a flaw |
| Whip following the target box | Attention jumps to the next part | a list of parts |
| Orbit around a part's own axis | Axial structure only reads in rotation | rotors, stacks, hinges, lenses |
| Lateral dolly along a long part | Length, a path | a beam; a cable run |
| Pull back + loupe (frame in frame) | Where (wide) and what (loupe) | small parts; a sensor |
| Crane to eye level or back up | Status change: the object stands up or settles | a transformation; scale |
| Turntable 360° | Every side | a whole object; a symmetry |
| Nearly static, slow dolly | Reading time without a dead frame | a spec sheet; a checklist |

Framing: the subject is ≥ ⅓ of frame height at every key moment. Cards on one side, the chip rail on the other, subtitles bottom centre, a loupe above them: never colliding. Shorten explode vectors rather than fly a piece into text.

## 9. Pitfalls of the medium

- Target boxes balloon → rest pose, skip `internal` pieces, long attachments `box:false`.
- Long diagonal leaders point at the wrong part → ring on the part body, flash the part.
- Two parallel boxes moving don't read as an explode → shell slides on its axis, contents stay and glow.
- A part built from generic boxes doesn't read as that part → give it its characteristic silhouette.
- Voice masked by foley, not music → duck foley too, hold the duck through word gaps.
- UI blips inside a silence break it → check cues against silence windows.
- A whip written inside the next segment plays as a hard cut → start it in the previous one.

