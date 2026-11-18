# 暗色科技发布 · 原文美术章节

来源：Lemo-Opuscar by Lemomo (LemoLab)。原文：[STYLE.md](https://github.com/lemomo-ai/lemo-opuscar/blob/00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4/styles/dark-keynote/STYLE.md)。

固定提交：`00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4`。原文 SHA-256：`b0791b5e95f56bf46c621e6064d426ebbee810c7515fb87e951b73668a2a0d24`。

本页按章节摘录原作者的美术资料，保留所选章节原文；不是 Blender 原生实现，也不是已经通过的美术验收。原文中的示例、选项和建议保持原有含义，不自动升级为硬限制。某些原文章节顺带包含字幕、流程或声音提醒，它们仍是参考文字，不会加载为 Blender 约束。

文档许可：[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)，另有上游对自有／客户影片制作的额外许可，见[来源说明](../docs/SOURCE_NOTICE.md)。改动：只增加此说明并选择章节，所选原文未改写。

保留章节：1、2、3、4、6、9。

---

## 1. Essence, and what it is not

A keynote-grade product film for **software**. There is no physical product and no glass render: the protagonist is the interface (a cursor, windows, notifications, tiles, a number). It lives on a dark stage lit by soft, cool light, with **one brand accent** reserved for the single most important element.

The style is defined by **precision**: every element snaps to a grid, every motion lands on a beat, every sound belongs to one designed family. Drama comes from contrast: disorder shown as generated UI, one decisive action, then empty space.

Not a glass product render (no physical object), not a screencast (no real OS or apps), not a hologram HUD (no scanlines), not a chart film (one number, not a chart).

## 2. Materials & rendering

- **Stage**: a near-black base with a radial lift at the upper centre, one large cool glow at single-digit opacity off-centre, a 50–55 % corner vignette. A hairline grid (white at ~3 %, every 4th line ~6 %) on a 48 px module. No grain.
- **UI kit, all original and drawn in code**: rounded windows (title bar with only a small glyph and title; never traffic-light buttons, menu bars or docks), notification cards, file icons with mono filenames, procedural thumbnails, list rows, tabs, badges, bars, uniform tiles.
- **Surfaces**: three steps of raised dark surface, 1 px border (~8 % white), 1 px inner top highlight, soft shadows.
- **Depth**: a 2.5D camera (`s = 1/(1/zoom − z)`); cards near the lens blur with magnification. Rotations use strip-rendered perspective (rotY ≤ ~24°).
- **Light** is the reveal tool: only pixels the light has passed turn on; unlit areas sit at a few percent.

## 3. Colour logic

- A cool neutral ladder only: near-black stage, three surface steps, text in three greys (primary, secondary, label). Neutrals are slightly blue, never warm brown.
- **One accent**, saturated and luminous, with its own glow. It is reserved for what the product *is* or *does*: the protagonist element, the call to action, confirmations, the key number. If two things are accent-coloured, one is wrong.
- **A problem colour** (typically a red for badges and warnings) may exist only while the problem exists; after the turn it never returns. Problem colour = noise, accent = the product.
- Secondary hues only as **category codes** in motion (a trail per data type), desaturated, and never on static UI.
- Example accents, pick one per film: lime `#B7F34A`, electric violet `#8B7CFF`, signal orange `#FF7A1A`.

## 4. Type & subtitles

- **OFL faces**: Inter (UI, captions, headlines; variable weight), Inter Tight 600 for giant numbers (tracking around −4.5 %), JetBrains Mono for labels, filenames and status text (wide tracking in small-caps labels).
- One line per screen for headlines. The big number gets its own screen and **no caption over it**: the number is the message.
- **Captions are a UI component**: a bottom-centre toast (dark translucent pill, 1 px light border, soft shadow, Inter 500 around 40 px, a small accent "speaking" dot). It enters with a small rise + fade in ~0.16 s and can turn more opaque over busy frames. Hold ≥ max(1.8 s, speech + 0.6 s).
- **Typed text is its own subtitle**: text the cursor types in frame is not burned twice (it goes only into the .srt).
- Lift product content while captions are up so toasts never clip it.

## 6. Camera grammar

A vocabulary, not a route. Opening and ending come from the topic.

| Move | Expresses | Can serve |
|---|---|---|
| Locked extreme close-up on a tiny UI element | Intimacy, one thing alive on a screen | a single action; a thought forming; a quiet status |
| Continuous pull-back, keyed per bar in log space | Accumulation, scale growing out of one point | spreading load; a network growing; a team joining |
| Push-in through a frozen frame | Time stopped, focus narrowing | a decision; the instant before a commit; a bug found |
| Whip pull-out in one beat | Cause and effect seen at once | a sync completing; a deploy landing everywhere |
| Dive into a small UI element (log-zoom) + match cut | Going inside the detail | a counter that matters; a log line; a setting |
| Half-second inserts expanding from their source | Overload, too much to read | notification storms; errors; choice overload |
| Near-locked frame while an object turns and light sweeps | Presentation, the product as hero | a reveal; a new version; a feature name |
| Slow lateral track across a UI plane | Order read by the eye | a timeline; a pipeline |
| Top-down plan over the grid | System view, structure | architecture; permissions; a workflow map |
| Return to an earlier framing | Rhyme: what changed | before/after; a loop closed; an echo |

Framing: generous negative space, one focal element, the accent at the focal point. Dutch angle and wobble only for disorder.

**Transitions = UI expand / collapse**: every shot change is an interface element expanding into the frame or the frame collapsing into an element. No fades, no blank frames. An expansion on a beat starts one frame early so the beat frame is already ~80 % open.

## 9. Pitfalls of the medium

- Strip perspective of a semi-transparent canvas shows vertical seams (overlapping slices double alpha) → project the *opaque* surface, then light it in screen space.
- A hard white glint reads as a sticker reflection → soft front, glint ≤ 20 %.
- Nearest-slot snapping looks like a flicker, not a collapse → typed destinations, curved paths, trails.
- Too few elements leave holes in a grid that read as a mistake → generate by rule, then trim or pad to exactly the slot count per group.
- A flat tinted rectangle for "closing" looks like a placeholder → squash the real surface.

