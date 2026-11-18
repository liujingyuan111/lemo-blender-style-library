# 地铁线路图 · 原文美术章节

来源：Lemo-Opuscar by Lemomo (LemoLab)。原文：[STYLE.md](https://github.com/lemomo-ai/lemo-opuscar/blob/00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4/styles/transit-map/STYLE.md)。

固定提交：`00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4`。原文 SHA-256：`e6c62bc75071c86b67c30def595e919910d86245504c8c09882d151a3c719d1c`。

本页按章节摘录原作者的美术资料，保留所选章节原文；不是 Blender 原生实现，也不是已经通过的美术验收。原文中的示例、选项和建议保持原有含义，不自动升级为硬限制。某些原文章节顺带包含字幕、流程或声音提醒，它们仍是参考文字，不会加载为 Blender 约束。

文档许可：[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)，另有上游对自有／客户影片制作的额外许可，见[来源说明](../docs/SOURCE_NOTICE.md)。改动：只增加此说明并选择章节，所选原文未改写。

保留章节：1、2、3、4、6、9。

---

## 1. Essence, and what it is not

- **Eight directions only.** Every line segment, river edge and coastline is horizontal, vertical or at 45°; every corner is one fillet radius. A line never wiggles.
- **Growth is drawing.** A line exists as far as its pen tip has travelled; stops light when the tip passes; an interchange appears only when the second line actually arrives, and it lands with weight.
- **Ink on a sheet.** The map is printed on paper with tooth and fibres, lit by one raking light, and the sheet lies on a dark table. The camera sees it as an object: in perspective, with depth of field, and with its edge in wide or low shots.
- **Words are printed.** Station names, callouts and cartouches are ink on the sheet; running numbers live on one small mechanical counter. Every text line holds one language.
- **One map, many scales.** The same sheet serves a single station and the whole network; detail appears and disappears with scale.

Not Data Storytelling (even a time chart is drawn as two lines with stops), not Blueprint (no white-on-blue linework), not Isometric Infographic (the map is flat; depth comes from the camera), not a 3D city map (no extruded buildings, no terrain), not a keynote (no slides, header bars, centred titles or page turns).

## 2. Materials & rendering

**The unit is the grid step, G.** Every coordinate and size on the sheet is given in G. Named stations sit on a 0.1 G lattice and at least 0.7 G apart along a line; a city network spans about 30 × 30 G and the sheet adds margins for the cartouche and any printed panel (about 45 × 47 G in our demo). The camera's zoom is read in screen pixels per G at the focus point (1080p).

| Mark | Geometry (G) |
|---|---|
| Line | 0.15 wide, round caps; corner fillet radius 0.34 |
| Thin line (a second rail mode; ferry thread) | 0.07 wide; fillet 0.30 |
| Parallel lines sharing a corridor | each offset ±0.10 from the shared axis (0.20 centre to centre, 0.05 of paper between); three or more: 0.20 steps |
| Stop | white disc r 0.085, ring 0.046 in the line colour |
| Terminus | an ordinary stop; when the end of a line matters (a destination, an end card) a white ring r 0.15 with a 0.06 ink outline |
| Minor stop (generated tick) | white disc r 0.065, ring 0.036; at most one per 0.78 G of track |
| Interchange capsule | the bounding box of every line point at the station, padded 0.13 on all sides; corner radius = half the shorter side (a stadium); white fill; ink outline 0.055 (0.07 for a major hub) |
| River | a band 0.76 wide (0.70–1.0 for a big river) with a darker edge 0.025 each side, round joins; creeks 0.15 with 0.02 edges |
| Sea, bay, harbour, lake | a closed outline on the eight directions, any size, filled with the water colour; the same darker edge, 0.025 outside the fill. Where a ferry runs, at least 0.5 G of open water so its lane keeps water on both sides |
| Tunnel under water | the line dashed 0.16 on / 0.11 off, plus two ink casing lines 0.02 at 55 % opacity, 0.05 outside each edge of the line |
| Pen tip | white core r 0.11, ring 0.05 in the line colour, soft halo r 0.8 in the line colour (45 % at the centre) |
| Line bullet | rail: disc r 0.25 in the line colour; bus and ferry: rounded square 0.48 with corner radius 0.12. Numeral 800 weight, 0.27 (one figure), 0.22 (two), 0.15 (a short word); opening year 0.17 bold ink, centred 0.30 below |
| Vehicle | white capsule 0.40 × 0.14, ink outline 0.026, three windows 0.064 × 0.056 in the line colour; trains and buses at about 2 G/s, boats at 0.85 size and about 1.2 G/s |

- **Interchange shape follows the station.** Points side by side make a horizontal stadium, stacked points a vertical one; lines that cross at one point make a circle r 0.13 with the ink outline, which reads as an interchange next to the 0.085 stop because of its black edge. A capsule never rotates to 45°; a diagonal spread becomes a rounded square.
- **Two passes.** A 2D canvas inks only the region the camera sees into a texture (about 1.35× the screen density at the focus, capped at 4096², mipmapped, anisotropic filtering), limited in depth to a few camera distances so low views don't starve; a WebGL pass intersects each pixel's ray with the sheet plane, prints the ink onto procedural paper and computes depth of field from the plane's known depth.
- **Paper**: warm off-white, procedural and tileable, sampled in world coordinates so it never slides. Three layers: a cloud of value at about 9 G period with detail down to 0.04 G, a tooth at about 2.4 G period, and short fibres 0.02–0.1 G long. Paper value varies by no more than ±3 % (fibres darken up to 3 % more); ink is multiplied by the tooth so flat colour varies 7–10 % and is never flat. Stronger than this and the sheet reads as plaster.
- **Light**: one raking light from one corner of the sheet (north-west in our demo), about 33° above the paper, neutral in colour and fixed for the whole film; it lifts that corner about 7 % above the opposite one. A specular sheen (up to +10 %, narrow lobe) appears only when the camera tilts more than about 30° from straight down and is full at 65°. Warmth comes from the paper and the table, never from a tinted light.
- **The sheet edge** sits on a near-black warm table (about #1B1918) with a contact shadow that fades over about 0.2 G. Far away the table goes into a warm dark haze so the horizon never aliases.
- **Grade**: a light vignette (up to −24 % in the corners), a 1.02 gamma, a light film grain at the master; no colour cast, no bloom except the pen-tip halo.
- **Screen space only for the instrument** (the counter) and objects near the lens (a station plate standing on the sheet, a tunnel before the map). Everything else is anchored to the sheet.

## 3. Colour logic

- Neutral ground: warm off-white paper; ink near-black for text and interchange outlines; secondary text in warm grey; water one pale blue with a darker edge, its labels in a mid blue.
- **Line colours carry identity and nothing else.** A real network uses its published colours; an invented one picks hues spaced around the wheel at similar weight, never two neighbours alike.
- **Mode is carried by line form, never by hue.** Each line keeps its colour whatever kind of vehicle runs on it:

| Mode | Line | Stops | Bullet |
|---|---|---|---|
| Metro, suburban rail | solid 0.15 G | stop disc | disc with a figure |
| Another rail mode (tram, light rail, maglev, people mover) | solid thin 0.07 G | stop disc; no generated ticks | disc with a short word |
| Bus, BRT | hollow: 0.15 G wide, the colour as two edges of max(0.04 G, 2.5 px), a paper core of at least 2.5 px; in wide shots the line widens on screen to keep that. Colours lighter than 0.4 relative luminance (yellow, sand, light green) get an ink rim of max(0.015 G, 1 px) | named stops only, stop discs | rounded square |
| Ferry, boat | a 0.07 G thread in the line colour on a paper lane 0.25 G wide (at least 10 px on screen), solid, over open water; it starts at a pier on the water's edge, with at most 0.5 G over land | pier: white rounded square 0.17 G, ring 0.04 G in the line colour | rounded square |
| Under water or underground | the line's own form, dashed, with the ink casing (§2) | none inside the tunnel | — |
| Walking transfer, in a station complex | a white bar 0.06 G wide with a 0.055 G ink outline outside it (0.17 G overall) from capsule centre to capsule centre, under the capsules; each station keeps its own capsule (one line: the r 0.13 circle) | — | — |
| Walking transfer, through the street | ink dots of radius 0.015 G every 0.08 G between the two stations' own markers, no capsule added; the shared name is printed once, at the station the story arrives at | — | — |

  Dashes mean "below": a ferry is never dashed, a tunnel always is. The ferry's paper lane is what tells it from a tram at any distance (10 px of paper on blue in a wide shot); a tram never runs on water without a bridge, which is drawn as ordinary track.
- **Paper inside a line is never painted.** The paper of a bus core or a ferry lane is erased out of the ink layer (canvas `destination-out`), so the procedural paper of the print pass shows through with its own tooth and light; a paper-coloured stroke never matches it. Erasing removes every ink beneath, so order the ink: water → surface lines (bus, ferry) → rail lines → stops and capsules → labels. A bus core over water then shows paper (correct for a printed map), and a rail line crossing a bus line stays whole on top.
- **Red (or the oldest line's colour) is the story's accent**: the first section, the "you are here" dot, the stamp of a verdict. When the accent sits on a line of the same colour, the dot is r 0.17 G (more than twice the line's width) with a 0.04 G white outline and a pulsing ring, so it never melts into the line. A second, dark neutral (navy) stands for anything compared against.
- Light colours (yellow, lilac, aqua, light green, sand) carry ink inside bullets; deep colours carry white.
- A paper wash (veil, 60 % paper over the sheet) fades the network back when one part must lead; stations under it keep about 20 %; never a dark overlay.

Example (our demo): paper #F2EEE5, ink #1B1C1E, secondary text #4A4740, river #BCD6EA / #8FB5D6, river labels #5F88AD, accent #E3002B, comparison navy #24346E.

## 4. Type & subtitles

- **Faces**: a neutral grotesk for Latin and figures (Inter in the demo) and a CJK sans of matching weight (Noto Sans SC, subset to the characters used). OFL, self-hosted. Native language above, second language below, one line each, never wrapped.
- **Sizes on the sheet**, in G (native / second language): hub label 0.30 / 0.17 bold; interchange 0.23 / 0.14 semibold; named stop 0.20 / 0.14 semibold; the second line in warm grey, 0.03 G below. Callout: date figures 0.58 heavy, native line 0.34, second line 0.24. Printed panel titles 0.58–0.60 / 0.36–0.38. Cartouche title 0.64 / 0.30, its note 0.24 in grey. Water names 0.22 / 0.17, set along the band.
- **Labels**: a paper-coloured halo (0.05 G stroke at 92 %) under every label. Placement is automatic: eight candidates around the station's edge (in order of preference: east, west, north-east and south-east, north and south, north-west and south-west), each scored against every line of the **finished** network and against labels already placed, hubs and interchanges first. It runs once, before the first frame, so a label never jumps while lines are drawn and lines that arrive later never cross it. A hand preference may override the score for a few stations.
- **Levels of detail by zoom**: minor stops fade in between 55 and 85 px per G, interchange names between 62 and 90, named-stop names between 100 and 130; hubs keep their names at every scale and grow when pulled out (× (85 / zoom)^0.6, at most 1.75), anchored to the station edge so they grow away from it without changing side. Which names show may also be chosen by shot, never flashed by time. While the camera rides a tip, names leave the frame before they can be read: show them in the held shots that follow, not during the ride.
- **Legibility is measured where the text lands**: font size on the sheet × the zoom at that point, foreshortened by the tilt. Text the viewer must read keeps the native line ≥ 20 px at 1080p and the second line ≥ 12 px (≥ 16 px on the counter); a two-line label counts only when its block is ≥ 26 px tall on screen. Below that, hide it by level of detail or move the camera.
- **Callouts** are printed on the paper: a bar 0.10 G wide in the accent (or the line being drawn), then the date in heavy figures, one native line, one second-language line; they wipe on from the bar in about 0.5 s. When a callout must sit over lines it gets a paper-coloured block with a soft shadow, no border.
- **Cartouche**: in one corner of the sheet, an ink bar, the map's name in both languages and a one-line note in grey. It is furniture: the camera finds it, it is not a title card.
- **The film's title is printed on the map.** At the start the title appears in the map's world: the cartouche (the map's name is the film's title), a line bullet, a station name plate by the lens, or a printed callout. Never a card or caption floating over the picture. It is bilingual like every printed text (native line above, second line below, one line each) and is held for its reading time where it lands (sizes and legibility above).
- **The film closes on the whole network.** The last shot shows the finished network entire, in top view or a gentle tilt, every line drawn; the end title and any credit are printed on the sheet (the cartouche, or a block in a margin, in the map's own type and ink), never laid over it. A detail the story ends on (a terminus, a first section) comes before this view, not instead of it.
- **The counter**: a dark enamel plate in the top-left corner (about 660 px wide, 86 px per row, rounded 14 px, four screws), rows with the native label above (24 px), the second label below (17 px), cream rolling drums (38 × 60 px, heavy figures), units at the right. Drums land only on sourced values; in between they spin blurred so no invented figure can be read.
- Reading time: hold every line ≥ (CJK characters ÷ 4.5 + other characters ÷ 15) + 1.5 s.

## 6. Camera grammar

A pinhole camera with a 32° vertical field of view (about a 42 mm lens on full frame), aimed at a point on the sheet. **Tilt** is the angle from straight down (0° = top view); **heading** turns the view about the vertical; there is never any roll. Zoom is in px per G at the aim point; focus is always on the aim point. Depth of field is analytic: blur radius = aperture × |depth − focus depth| ÷ depth, in pixels at 1080p, capped at 26 px, so the far sheet blurs up to the aperture value and the near edge more.

| Move | Tilt / zoom / aperture | What it expresses | Can serve |
|---|---|---|---|
| ride the pen tip, aim about 1.5 G ahead of it | tilt 15–30°, heading within ±15°, 130–260 px/G for a tip at 1–3 G/s, aperture 16 | building, one step at a time | the first section; a single new line; a route described stop by stop |
| drop low where a line meets water | tilt ~60°, 185 px/G, aperture 26, eased in and out over ~0.5 s | crossing, risk, a threshold | a river or strait; a border; going underground |
| continuous pull-back with level-of-detail changes | tilt 12° → 0°, 80 → 50 px/G, aperture 6 → 0 | growth, scale arriving | years passing; a network filling in; "how big it became" |
| low oblique sweep with shallow focus | tilt 57–62°, heading swinging about 40°, ~100 px/G, aperture 24, inked depth extended | density, life, the present tense | the busiest core; everything running at once |
| glide across the sheet to another panel | tilt rises to ~25° mid-move and back to 0°, aperture up to 8 | changing the question, same object | a comparison chart; a legend; a timeline printed in the margin |
| rise until the sheet edge and the table show | tilt ~30°, ~40 px/G | the whole, the object | an overview; a chapter break |
| push in to one segment under a paper veil | tilt 4° → 0°, 60 → 140 px/G, aperture 3 → 0 | memory, origin | where it began; "you are here" |
| locked frame | tilt 0°, aperture 0 | reading, judging | any comparison or verdict (hold ≥ 2.5 s before the verdict) |

When riding a tip, keep tip speed × zoom at or under about 500 px/s on screen (a long, fast line means a wider zoom or a slower tip). The camera is never lower than about 25° above the paper (tilt ≤ 65°): lower, and the sheet stops reading as a map. Top views carry no blur; any tilt above 10° carries some.

Framing: the subject sits off-centre with room ahead of a moving tip; the counter owns the top-left corner and nothing important goes under it. Transitions: match cuts on round shapes (a headlight, a lamp, a coin becomes a station dot), glides across the sheet, hard cuts to a new panel. No page turns, no fades to black mid-film.

## 9. Pitfalls of the medium

- **Off-grid geometry**: any segment not at 0/45/90° breaks the style. Route between points with an automatic bend (straight then diagonal, or the reverse) and validate every segment.
- **Labels over lines, or labels that jump**: give labels a paper halo and place them once against the finished network, before the first frame. Placing against what is drawn so far makes labels hop as lines arrive.
- **Parallel lines sharing a corridor** collide: offset each line by ±0.10 G and let one capsule enclose all points of the station.
- **Too much text in wide shots**: hide minor names by zoom, not by time.
- **A flat map**: a top view all the way through reads as a slideshow. Tilt, focus and the sheet edge are what make it an object; a still of the style should show at least one tilted view with depth of field.
- **Paper too loud**: tooth and fibres stronger than a few percent turn the sheet into plaster or canvas.
- **Mode by colour**: a ferry or bus line in a "ferry blue" breaks colour as identity. Use the line forms in §3.
- **Real networks**: published colours and station names are facts, logos and branded bullets are not; the film is an unofficial tribute and says so on screen. Check every date and length against official sources; encyclopaedia figures for opening sections are often for a different span, and stations are renamed (the data rule is in §11).
- **Counters that interpolate** invent numbers. Land only on sourced values; spin between them.
- **Texture resolution in tilted views**: limit the far distance of the inked region and let depth of field hide the softness.
- **Stale ink**: when the inked texture is reused, reset the 2D transform before clearing it, or last frame's ink ghosts every other frame.

