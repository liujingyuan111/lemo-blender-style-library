# 等距小人场景 · 原文美术章节

来源：Lemo-Opuscar by Lemomo (LemoLab)。原文：[STYLE.md](https://github.com/lemomo-ai/lemo-opuscar/blob/00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4/styles/isometric-picture-book/STYLE.md)。

固定提交：`00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4`。原文 SHA-256：`0118a0183745d8bbd29ab06792c2ea887edeee7d3dcd47b5a89889c57687cd59`。

本页按章节摘录原作者的美术资料，保留所选章节原文；不是 Blender 原生实现，也不是已经通过的美术验收。原文中的示例、选项和建议保持原有含义，不自动升级为硬限制。某些原文章节顺带包含字幕、流程或声音提醒，它们仍是参考文字，不会加载为 Blender 约束。

文档许可：[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)，另有上游对自有／客户影片制作的额外许可，见[来源说明](../docs/SOURCE_NOTICE.md)。改动：只增加此说明并选择章节，所选原文未改写。

保留章节：1、2、3、4、6、9。

---

## 1. Essence, and what it is not

- **One real place, full bleed.** A platform, a gate, a cabin, a crossing, a counter: the ground runs off every edge of the frame. No floating board, no frame line, no vignette. A topic that travels (a parcel, a route, a production line) can still be one place: one continuous ground at one scale, with the stops along it (see §11); what breaks the look is a separate board, a map view or a change of scale for each stop.
- **People are the diagram.** Slim figures seen from behind, no faces and no hands, move only when the rule says so. Who moves first, who waits, who sits is the information.
- **Type lies on the ground.** Each idea is one key word or number painted on the floor, big and small sizes, one accent character, landing one character at a time.
- **The cut-away.** Whatever stands between the camera and the action (a roof, a canopy, the top of a wall, a glass façade) is cut low or lifts off like a paper flap, so the camera always looks into the place from above.
- **Clean, always.** One place, one action, one phrase per beat. Large calm areas of ground around the type, people in tidy lines and rows, few props, every object instantly recognisable. A frame that needs a second look to find its subject is wrong.

Not **Isometric Infographic**: that style builds a model on a floating board over a dot lattice and labels it with sans-serif pins, icon statistics and inset bubbles to trace a process; here there is no board edge, no pins and no icons: the place is real and full bleed, the labels are serif words lying on its floor, and the explanation is people obeying a rule. Not **Low-poly Isometric Island**: no lighting, no faceted terrain, no shadows or glow; solids are flat three-tone paper colours and the ground is a printed plane. Not a cartoon (no expressions, no gags), not a slide (no headers, no centred titles, no cards).

## 2. Materials & rendering

- True isometric (axes at 30°), Canvas 2D, painter's sort. Every solid and every person is sorted by its **floor footprint** (x + y at floor level), never by the centre of its box: a seat back sorted by its centre height ends up drawn over the passenger sitting behind it.
- Solids are flat-shaded in **three tones per colour**: top lifted toward warm paper, +y face the base colour, +x face dropped toward a warm umber. Curved bodies (a fuselage, a column) are faceted and quantised to the same tones plus one in-between, so they read as round without gradients. No outlines on solids, no shadows, no textures, no highlight spots (a round tree crown or a ball is a flat disc or a faceted solid in the same tones, never a glint).
- **New objects** (vehicles, machines, buildings, trees) follow the same model: built from boxes, prisms and faceted solids at real size in metres, three tones from the kit's `tri()`, recognisable from their silhouette at a glance, simpler than the people. Vehicles read from the body (cab, cargo box, a band of the subject hue); wheels are small, low and mostly under the body in one dark tone, never thick drums or tyre-and-hub detail.
- Ground surfaces carry only their functional markings (painted lanes, chevrons, lead-in lines, stop bars, seat squares) and a faint tile or slab grid.
- **Cut-aways** are part of the model: the near wall is cut low and the far wall keeps its windows; a lid is its own solid with a paper-coloured underside, hinged on the far edge so it opens away from the camera; glass is a pale tint with thin mullions and is cut to a parapet whenever it would stand between the camera and type or people.
- **People** are billboards anchored at their feet, about 1.6–1.8 m tall: a round hair-dark head with a sliver of skin at the ear, a two-tone torso, separate trouser legs, dark shoes, optional long hair or skirt, a rolling case. Seated people show only shoulders and the back of the head above a low seat back. Walking scissors the legs along the screen; arms counter-swing.
- Bodies obey space: people never pass through seats, walls or each other; a queue keeps about 0.75 m between feet; someone sitting down first steps back into the row's legroom, walks sideways to the seat and sits (never sinking into or floating above it); a lifted case travels up over the open bin and is lowered in, never into a wall or a seat.
- Everything is a function of time. A crowd that queues is simulated once at load (deterministic) and **sampled with interpolation**, so replaying it slowed down still moves every frame.

## 3. Colour logic

- A warm paper neutral for every ground (outdoor concrete a touch cooler, indoor carpet a touch warmer), one dark ink, **one accent reserved for the rule** (the key character, the "stand here" outline, arrows, a lit sign, the winning number, a stretch of floor that matters), one **subject hue** carried by the place itself (seats, livery bands, chairs in a paler tint, sign trim), one marking colour (lead-in lines, a tug, a baggage tractor). People wear four muted tops, so a filled room reads as an even four-colour weave.
- The accent never decorates; it appears only where the rule is. It stays small because its rarity is what makes the eye go to it: many frames carry none at all. A path in the accent marks the stretch being explained now (it grows ahead of the walker or the vehicle and fades behind it), not a trail left across the whole film.
- The subject hue and the marking colour must be clearly apart, in hue and in value, from the four tops: people have to stand out from the place they move through (a blue-green place swallows fog-blue people).
- Shade toward warm umber and paper, never toward grey or violet: dirty shadows are the fastest way to lose this look.
- Example palette: paper #F1E8D8, concrete #EAE2D3, carpet #F2E5CE, ink #2A2E29, accent persimmon #D0573A, subject green #3D6B59 / #A7C2B2, marking ginger #E2AE3A; tops ochre, fog blue, grey violet, oat.

## 4. Type & subtitles

- Chinese: a serif (Noto Serif SC, 700 for keywords, 500 for particles); Latin and numerals: a book serif (Newsreader). Open-licence fonts only, subset to the characters used.
- **Floor type**: big ≈ 1.5 m on the ground, small ≈ 0.8 m; read along the up-right axis (coordinates in §10). One phrase per beat; one line where the frame is tight. One accent character or number per phrase, never a single thin stroke (一 in the accent reads as a line, not a character). Characters land ≈ 0.14 s apart: fade and scale 1.22 → 1, pale ghost → ink. A painted title or a pair of numbers may scale up to ×1.6.
- Type sits on clear ground: nothing stands on it, nothing raised stands in front of it (see §9), at least 5 % from every frame edge, and clear of the subtitle bar.
- Signs in the world (gate signs, group signs, screens) face the camera side of the room at the iso angle, never a flat card facing the lens.
- Reading time: every piece of world text stays fully in frame ≥ CJK/4.5 + Latin/15 + 1.5 s.

### Narration & subtitles

When the film tells something, a narrator says it and the picture shows it at the same moment: one line per action or shot, each line starting as its action starts. A calm, quick reader in the film's language; the floor carries only that line's key word or number, never the sentence. Subtitles: one cue per narration line on a pale bar in the lower safe area, one Chinese line above (≈ 34 px) and one English line below (≈ 25 px, a translation of the whole sentence), switched hard, never two cues on screen. Numbers the viewer must remember: at most three, each said with what it compares to, and held on screen ≥ 2.5 s.

## 6. Camera grammar

| Move | What it expresses | Can serve |
|---|---|---|
| slow drift and push (≈ 6–8 % zoom) | calm attention on one rule | a call, a waiting room, a hold to read |
| follow the head of a line | the order of things | a corridor, a boarding, a procession |
| travel along the ground at the subject's pace | one place after another on the same road | a delivery, a parade route, a line of workshops |
| rise to wide while a lid opens | revealing a space whole | an interior, a capacity, a grid of places |
| locked frame | judging, reading | a verdict, a comparison, the last frame |
| step back to frame one whole incident | cause and effect in one view | one person blocking, one door jamming |
| tilt down from outside to the people | arrival, cause → people | an opening, a change of place |
| scale jump (room → building → site) | the result in context | a verdict, an ending |

The angle never changes (iso is fixed); camera moves are translation and zoom. Every move is motivated by the action, and text and subject stay inside the frame at both ends of it. Transitions: a continuous move, a lid opening, a run back along the same path, or a cut on the beat at the same angle. No page turns, wipes, black or blank frames; a pull-out shows its next subject (a mark being drawn) within half a second. A lid is a reveal only while it is seen: it finishes turning, paper side up, inside the frame before it glides off away from the camera.

## 9. Pitfalls of the medium

- Anything raised by H metres hides what lies behind it (toward −x behind a face that looks +x, toward −y behind a face that looks +y): floor up to H metres back from a long edge, and a person standing there loses everything below the edge's top, vanishing completely within H − 1.7 m. It holds for low objects too: a 0.8 m belt or counter covers floor type 0.8 m behind it, a 3.2 m truck side hides people's legs up to 3.2 m behind it and whole people within 1.5 m, a glass wall or a wing hides type metres away. Keep type and the people who matter on the camera side of tall objects, or cut those objects down; check every frame in which a vehicle passes.
- A path that zigzags (turning at every vehicle or doorway) reads as noise; routes run along the world axes with few right-angle turns, and the walker or vehicle on them heads away from the camera (see the back-view pitfall below).
- A crowd folded into a serpentine reads as a solid block; one straight line reads as order. Numbers on the floor beside each person need spacing wide enough for the label (about 1 m).
- People walking toward the camera show a back view that looks wrong; route walks up-left, up-right or across.
- Seated people disappear behind high seat backs: keep backs low enough that shoulders show.
- Sorting boxes by their centre and people by their feet puts furniture over people (see §2).
- Colours passed to the engine as a bare hex string are shaded by `engine.js`'s own `tri()`, which darkens toward violet; always pass `kit.js`'s `tri(colour)` (warm umber). `iso.sphere` adds a white glint unless given `{ hi: false }`.
- A simulated crowd sampled by rounding to frames steps on and off when replayed slowly; interpolate. Compressing a long process by moving people faster than ~6 m/s (0.2 m per frame) reads as teleporting.
- A camera move can drag a sign or a word across the frame edge, and background details (a far sign, a row of labels) can appear half-cut at the edge of another shot: anything meant to be read needs both ends of the move checked, and background text belongs only to its own shot.
- Check a crowd film frame by frame, not by eye: `demo/tools/motion_check.mjs` renders every frame at 30 fps and lists jumps, stop-start stepping and people standing closer than a body width, from positions the film reports through a one-line hook (documented in the tool); copying it is in §10.

