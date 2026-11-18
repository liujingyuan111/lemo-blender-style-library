# 彩色玻璃窗 · 原文美术章节

来源：Lemo-Opuscar by Lemomo (LemoLab)。原文：[STYLE.md](https://github.com/lemomo-ai/lemo-opuscar/blob/00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4/styles/stained-glass/STYLE.md)。

固定提交：`00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4`。原文 SHA-256：`0f6551bd109a4127404068aa1e75f18f16b58c80b486c23480b3d193e597b060`。

本页按章节摘录原作者的美术资料，保留所选章节原文；不是 Blender 原生实现，也不是已经通过的美术验收。原文中的示例、选项和建议保持原有含义，不自动升级为硬限制。某些原文章节顺带包含字幕、流程或声音提醒，它们仍是参考文字，不会加载为 Blender 约束。

文档许可：[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)，另有上游对自有／客户影片制作的额外许可，见[来源说明](../docs/SOURCE_NOTICE.md)。改动：只增加此说明并选择章节，所选原文未改写。

保留章节：1、2、3、4、6、9。

---

## 1. Essence, and what it is not

- **Cut pieces of coloured glass in dark lead cames**, faces and folds **painted in brown grisaille**.
- Glass has no light of its own: it **glows only when the sun is behind it** and throws a soft coloured copy onto the stone floor; unlit, it is dark and milky.
- Figures move **piece by piece**, rigid and stepped.
- The room is always there: stone, a splayed embrasure, iron saddle bars, a floor that catches light.
- **Secular**: no crosses, saints, halos or other religious imagery; borrow the craft, not the subjects.

Not vector art with black outlines, not a kaleidoscope or Voronoi filter, not Tiffany Art Nouveau, not mosaic (mosaic reflects; glass transmits).

## 2. Materials & rendering

One formula for everything (a WebGL compositor), so every element sits in the same light:

```
glass   = tonemap( backlight(x,y,time) × transmittance × glass texture ) + weathering haze × room light
surface = albedo × (room ambient + glow spilled from lit panes + point lights)          // stone, lead, iron
floor   = flagstones × (ambient + projected colour-patch map, blurred + halo)            // perspective or top-down
+ additive light shafts with dust · bloom (bright glass eats into the lead: the "irradiation" effect)
```

- **Hue-preserving tone mapping**: per-channel `1-exp(-x)` turns cobalt pastel; blend to per-channel only at the very top so a sun disc burns white while blue stays jewel blue.
- **Unlit panes**: weak sky light + room-lit weathering haze, figures ghostly but readable. **Lit panes**: backlight ~2–3×, a soft, slightly skewed moving band edge.
- **Pieces**: smooth Catmull-Rom cuts (no deep concave corners). **Every piece is textured** (`multiply` in its clip): streaks at a per-piece angle, hue drift (±10 %), darker aged edges by the lead, ±9 % thickness variation. The shader adds seed bubbles, scratches and thickness clouds in world space; fade small features below ~0.6× zoom or they sparkle.
- **Lead**: near-black, one planar network, thinner on small pieces, round joins, faint grey flange, solder blobs; only where colours meet (one colour = one piece).
- **Grisaille**: tapered trace lines in translucent dark brown; **matting** (stippled wash, graded shade, soft band inside the lead); **scraped highlights** (a thin stroke beside each fold in the piece's own colour: the only highlight transmitted light allows). Patterns (mail, scales, plates) are grisaille arcs and bands.
- **Faces**: almond eyes, heavy upper lid, big pupils, brow flowing into the nose. **Expression lives in brows and mouth**; change it by swapping the face piece, never morphing.
- **Backgrounds**: hand-cut **lozenge quarries** (jittered lattice, shared vertices, a painted motif each); borders of a coloured band with pearls and a white fillet with a running vine.
- **Room**: warm grey ashlar, a lighter embrasure, mullions; floor of **large irregular flagstones**, never the wall's running bond.
- **Floor projection**: blurred, ~20 % desaturated, modulated by the stone, haloed, mirrored (the window's top lands farthest into the room). **Shafts**: additive with dust, near 0 at the window, peaking ~40 % down.

## 3. Colour logic

- Two hues **carry the picture** (one deep, one hot); three or four more only as **small touches**. Example (Chartres logic): cobalt ground, ruby, touches of gold, green, murrey.
- Greenish white glass sparingly (faces, fillets, sky). **Flesh darker than you think**, or backlit faces burn white.
- A story light (candle, lamp, screen) may take a colour no glass uses, so it reads as a source.
- **The sun's colour is the clock**: blue-white dawn, near-white brightest noon, gold afternoon, deep orange dusk (raise intensity rather than redness), weak blue moonlight. Patch length follows sun height.
- Stone and lead take colour only from spilled or projected light.

## 4. Type & subtitles

- **Subtitles**: a parchment **banderole** near the bottom (curled ends, gentle sag, thin rule), IM Fell English ~44 px in dark ink. It unfurls from the centre; text fades in only once it is ≥ 75 % open; pad the ribbon well past the text. Hold ≥ max(1.8 s, speech + 0.6 s).
- **Titles**: incised Roman capitals (Cinzel 600) in the stone, dark cut, light lower lip, gilding, revealed by a moving band of light; small lines ≥ 30 px on screen. In the glass, text only as grisaille on a white-glass scroll.

## 6. Camera grammar

A vocabulary, not a route. Opening and ending come from the topic.

| Move | Expresses | Can serve |
|---|---|---|
| Truck sideways with the band of light | Time passing, the story moving on | a sequence of steps; a day; chapters |
| Locked close-up on one pane | This panel is "now" | a line being read; a character's decision; a detail |
| Pull back to the whole window | The rule, or the whole story at once | learning the system; a summary; aftermath |
| Tilt down the shafts to the floor, then top-down | The picture leaves the glass and becomes light | an event too big for its frame; a dream; a memory |
| Hold through a crack, no cut | The event is the medium breaking | a turning point; a loss; a revelation |
| Slow push toward a small light | Attention narrowing to one source | a discovery; a secret; hope |
| Tilt up to a rose or tracery | Something above the panels governs them | a clock; a cycle; an overview |
| Rack between two panes, one lit, one dark | Past and present side by side | before/after; two lives; cause and effect |
| Low angle along the embrasure, glass raking | The window as architecture, scale | awe; an institution; a long history |
| Return to an earlier framing under new light | The rhyme shows what changed | growth; nightfall; repair |

Framing: subjects big (close-ups ~1.3–2.3× a lancet width); in a narrow lancet stack figures diagonally; a revealed thing near centre, ≥ ~1/8 frame width with glow. Transitions: moving light, shafts, a crack, darkness; never a dissolve, wipe or flip.

## 9. Pitfalls of the medium

- Hidden leads show through front pieces → erase the surface under each piece before stroking its lead.
- Pastel glass → hue-preserving tone mapping; darker flesh. Red dusk × blue glass = mud → keep blue alive, raise intensity.
- Voronoi reads as a filter; flat fills read as clip-art → hand-cut lozenges, texture on every piece, heavy grisaille.
- A sharp floor patch looks like a decal → blur, desaturate, stone-modulate, halo. Shafts at full strength at the window wash out the pane.
- Top-down projection is flipped → put the wall at the frame bottom so figures stand upright (mirrored, correct).
- Patch-map canvas size mismatched with the code draws into a corner of the texture → one constant size.
- Carved text in a dark wide is unreadable → push in, park a light on it.

