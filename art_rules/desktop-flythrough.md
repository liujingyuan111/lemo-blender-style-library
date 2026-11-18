# 桌面卡片穿梭 · 原文美术章节

来源：Lemo-Opuscar by Lemomo (LemoLab)。原文：[STYLE.md](https://github.com/lemomo-ai/lemo-opuscar/blob/00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4/styles/desktop-flythrough/STYLE.md)。

固定提交：`00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4`。原文 SHA-256：`38993ddb69447ba7c44890fbdcff8698b31cbfcd48de82932334b65124f2c390`。

本页按章节摘录原作者的美术资料，保留所选章节原文；不是 Blender 原生实现，也不是已经通过的美术验收。原文中的示例、选项和建议保持原有含义，不自动升级为硬限制。某些原文章节顺带包含字幕、流程或声音提醒，它们仍是参考文字，不会加载为 Blender 约束。

文档许可：[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)，另有上游对自有／客户影片制作的额外许可，见[来源说明](../docs/SOURCE_NOTICE.md)。改动：只增加此说明并选择章节，所选原文未改写。

保留章节：1、2、3、4、6、9。

---

## 1. Essence, and what it is not

- **The desk is the world.** A matte paper mat with a regular dot grid lies on a light wooden desk, lit by one low warm sun through a window. Everything sits on it and casts a long, soft shadow. A few everyday desk things (a pen, sticky notes, a mug, earbuds) sit around the edges as foreground and background layers.
- **Interfaces are paper cards.** Phones, tools and dashboards are rounded slabs a few millimetres thick with the interface printed on top. They are places: characters stand and hop on them, and parts of the interface rise out of them as small 3D objects.
- **The cast are pixel sprites made solid.** One bevelled cube per pixel, thicker inside than at the edge, eyes standing proud. They lie on a card as flat stickers and pop up into toys; they blink, wait on the beat, get squashed and spring back.
- **Every stop is busy.** At each station something small moves besides the main action: debris bursts, data cubes hop, a lamp blinks, marks vibrate.
- **One take.** No cuts. The camera glides, orbits, cranes and whips between stops; it closes on the whole desk.
- **Everything lands on the beat.** Hops, pops, ticks and slams sit on the 16th-note grid of one steady tempo, and every action has a sound.

Not a screen recording (no cursor, no glowing monitor, no real app chrome or logos); not a brick or clay toy film (pixel voxels on printed paper); not an isometric infographic (perspective camera, real light); not flat motion graphics (everything has thickness and a shadow).

## 2. Materials & rendering

- three.js, physically based, neutral tone mapping. Scale: a card is 0.3–0.7 units wide (1000 canvas px per unit); dots 0.03 apart. A character must be big enough to show its eyes: in the demo about 1/5–1/3 of the card it stands on (0.006–0.0075 units per pixel, so a 16-pixel sprite is about 0.1 wide); smaller casts lose their faces in a medium shot. A character may be scaled for a moment (`scale`) when the story needs it; it reads best on a beat, with a pop's overshoot.
- **Light**: one directional sun low from the back-left (about 20° up, so a toy's shadow is two or three times its height), a 4096 soft shadow map that follows the camera target and resizes with distance; a cool-sky / warm-ground hemisphere fill, so shadows read blue and lit faces warm; a faint room environment for highlights; exponential fog thinned as the camera pulls back.
- **Desk**: a dotted paper mat (a thin rounded slab whose size is a multiple of two dot spacings, so the printed dots line up with any 3D dots) on a procedural light-oak plane (planks, long soft grain). Soft window-light patches (blurred four-pane shapes, warm, additive, low opacity) lie under the cards. Props are plain primitives in matte or satin materials, placed so each close shot has something soft in front of or behind its subject.
- **Cards and screens**: a rounded slab plus a canvas texture on top with a faint deterministic grain. Print is flat: one ink, mono labels in spaced caps, bold numerals, thin rules; a card head carries two lines (English mono caps over the other language in bold). A phone is a card with a dark bezel and a whole interface of whatever app the story needs: a status bar, a header that names the screen, content filling the screen, controls at the bottom. Redraw a canvas only when its state changes; quantise continuous changes.
- **Voxel cast**: instanced bevelled cubes per pixel; depth grows with distance from the silhouette; pure-black pixels are eyes, which protrude and blink (they take the colour of the pixel above). Rig: root (feet, yaw) → hinge (lying flat ↔ standing) → squash (scaled at the feet) → spin. State: `e` (0 flat sticker … 1 full toy), `hinge`, `sq`. The same picture at half resolution is the same character, smaller and chunkier.
- **Props**: the same voxel recipe (crosses, ticks, bells) or plain rounded primitives (bricks, presses, drawers, towers, tent cards, stamps). Data that rises out of a card is extruded from its printed shape, so it still reads from above.
- **Impact ring**: a thin accent-coloured ring spreads over the paper from an impact and fades in about a second.
- **Post, per frame**: 16–24 sub-frames with Halton sub-pixel jitter (anti-aliasing, and a little motion blur on fast moves) → depth of field on each sub-frame, behind the focus plane only → bloom on highlights only → grade (light vignette, slight warmth, a little contrast and saturation). Subtitles are DOM on top.

## 3. Colour logic

- **One light ground** (the mat) with a slightly darker dot, cool-tinted so the warm sun leaves it fresh; a warm wooden desk around it; cards in a near-white of the same temperature; **one dark ink** for print; **one accent reserved for what matters now**: the route, the current step's badge, the send button, the lit window, the key word.
- Two or three support hues for the cast and props, mid-saturated, never neon; one warm cast colour against the cool ground. **Red only for failure or trouble** (an error, a weak signal), **green only for success**; data in motion may take one bright support hue so it reads apart from the route.
- Judge the rendered frame: avoid grey on grey; keep the vignette light and the shadows tinted by the sky fill.
- Brand use: the brand colour becomes the accent; the brand's interface colours print on the cards; the ground stays light.
- Two example palettes besides the demo's (starting points, not a menu; the names are the keys of `COL` in `src/cards.js`):
  - *Lilac and violet* (creative tools, music, learning): paper `#e7e4f3`, dot `#cbc5e2`, card `#fcfbff`, ink `#1d1a2e`, mute `#807a96`, line `#e2dfee`, accent `#6b4ce6`; support apricot `#f39a5b`, sky `#5fb4e8`, lemon `#f2c94c`; red `#e2483d`, green `#3fa57a`; haze `#e8e4e6`.
  - *Cool grey and amber* (money, logistics, energy, food): paper `#e5e9ed`, dot `#c8cfd7`, card `#fdfdfc`, ink `#20252b`, mute `#7f8790`, line `#e0e4e8`, accent `#e8890c`; support teal-blue `#2f8fb0`, plum `#8a5a9e`, cream `#f4e3b5`; red `#d23a3a` (keep it clearly apart from the amber), green `#3c9c6e`; haze `#e6e4e1`.

## 4. Type & subtitles

- **In the world, only keywords and numbers**: step badges (a camera-facing accent pill with a digit and one word), sizes, a name on a screen, a banner, a title card. Text meant to be read is framed above the subtitle area, held still for its reading time, and large enough at the angle it is seen: flat print reads from 55–70° down; a low camera reads a standing tent card.
- **Titles are objects on the desk**: an opening tent card beside the first stop; at the end a large paper card dropped onto open desk in the final frame. Where depends on the layout: wherever it covers no station, route or character and sits clear of the subtitle bar (the demo's stops leave the middle free; a zigzag layout may leave the front edge). Leave that space when laying out the desk.
- Every face on screen comes from the film's own font files (cards, pills, subtitles); the mono stack falls back to the film's CJK face, never to a system face.
- Three roles: a mono for labels and numbers (spaced caps), a sans with a heavy weight for pills, titles and subtitles, and a CJK (or other script) face both fall back to. The families are free (e.g. DM Mono or JetBrains Mono, Manrope or Space Grotesk, the Noto Sans of the film's language); the roles are not. Pixels belong to the cast, so no pixel font on the print.

### Voice-over and subtitles

- When the film explains something, a voice tells it: short spoken lines, one idea each; the picture shows what the voice is saying at that moment, and the words on cards are only the keywords of the line.
- **One subtitle cue per spoken line**, in a quiet bar at the bottom centre (a rounded ink box at about 72 % opacity, about 64 px above the frame edge): the spoken language on the first line (bold, about 40 px), a whole-sentence translation on the second (about 26 px). One language per line, never wrapped. The cue appears with the line and leaves with it.
- The camera keeps its subject about 110 px above centre (a fixed vertical view offset), so nothing that matters sits under the bar.
- A version voiced in another language starts each line on the same second, so picture, subtitles and timing do not change.

## 6. Camera grammar

| Move | What it expresses | Can serve |
|---|---|---|
| Macro glide with a slow orbit (close, 20–45° down) | being there, small scale | a character at work; one detail of an interface; a title standing on the desk |
| Whip from card to card (0.3–0.5 s, banking into the turn) | the next step, cause → effect | a process moving on; a hand-off between tools |
| Rise to near top-down (55–70° down) | reading, one card as a whole | a screen, a counter, a table; any verdict |
| Ride along, low behind the subject | travel, momentum, pursuit | a route; a delivery; a download |
| Pull back over the desk | the whole system, scale | a recap; the route so far; many stations at once |
| Hold with a shake | impact | a press, a stamp, a ring |

- One take, no cuts, no dissolves. Targets are live subjects; between keys the target follows a Hermite path with live end points; drift is a breath, not a handheld wobble.
- At a key where a whip starts, the target rests first (or the camera stutters). A character's take-off is the natural start of a whip. A whip between far-apart stops arcs up mid-way so the stops in between stay in frame.
- Wide shots frame the stations to fill at least 70 % of the frame width. **The film closes on the whole desk**: every stop and the route in one frame, everything moving once, the title landing in open space.

## 9. Pitfalls of the medium

- **Softness**: depth of field and motion blur easily turn a subject or its words to mush. Blur only what lies behind a focus plane set a little beyond the subject, lightly (≤ 5 px), never anything in front; let the shutter shrink with camera speed so a streak never exceeds about 8 px; draw card and screen canvases at 3–3.4× (pills at 3×) so print stays crisp when a card fills the frame; no CSS or canvas blur on anything meant to be read.
- **Flat print read at a low angle**: text on a card seen from 20° is unreadable. Rise to 55–70° to read a card; put text the low camera must read on a standing object.
- **A standing toy hides the row behind it**: place characters beside or behind the text being read, or off the card, and check every reading frame for overlap.
- **Text under the subtitle bar or cut at the frame edge**: keep the fixed vertical offset; show name plates and labels only in the shots that frame them whole; take camera-facing pills away before the camera moves on.
- **Screens that read as blank**: a phone card without a whole interface reads as an empty white slab in close-up.
- **Shadows of floating labels**: with the sun at 20°, a pill a few centimetres up throws a long shadow across the card and greys out its print. Labels and pills cast no shadow (`pill()` turns it on: set `castShadow = false`); a real floating object (a bell) may, but no shadow falls across text being read.
- **Characters lost in the wide**: on screen a character is about `width × 1080 / (2 · dist · tan(fov / 2))` px wide. In the closing wide view keep every character at least about 35 px wide (the demo's smallest is about 37 px); otherwise frame closer, bring it forward, or scale it up for the curtain call.
- **Voxels seen edge-on**: a standing sprite seen from far to the side reads as stripes and its eyes vanish; turn it towards the camera (`yaw`) for its key moments, and give a large picture-like sprite a thinner `depthK` (0.6–0.9).
- **Whips over bare paper**: a fast move between far-apart cards crosses empty desk; arc it up so the stops in between pass through frame.
- **Dead stations**: a stop where only the main action happens looks static; give it one or two small moving things that do not compete with what the voice says.
- **Bars and ticks seen from above**: upright 3D bars and standing checkmarks turn into blobs in a top-down view; extrude them along the card or lay them flat.
- **Interpenetration**: characters at the same depth overlap; followers move one 16th apart; a knocked-flat pile goes back to sticker thickness before it stacks; check props against card edges, gates and drawers.
- **Ripples as pegs**: lifted 3D dots read as pegs from above; use a flat expanding ring.
- **Slow renders**: canvas redraws on every sub-frame; redraw on state change only.
- **A score made of fragments**: write whole phrases and put the accents on top.

