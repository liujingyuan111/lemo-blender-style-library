# 档案看片台 · 原文美术章节

来源：Lemo-Opuscar by Lemomo (LemoLab)。原文：[STYLE.md](https://github.com/lemomo-ai/lemo-opuscar/blob/00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4/styles/archive-lighttable/STYLE.md)。

固定提交：`00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4`。原文 SHA-256：`2f18ac9a42822b7a9941866c42b0642e5417dea5431d61f141f6e11b29c1ec14`。

本页按章节摘录原作者的美术资料，保留所选章节原文；不是 Blender 原生实现，也不是已经通过的美术验收。原文中的示例、选项和建议保持原有含义，不自动升级为硬限制。某些原文章节顺带包含字幕、流程或声音提醒，它们仍是参考文字，不会加载为 Blender 约束。

文档许可：[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)，另有上游对自有／客户影片制作的额外许可，见[来源说明](../docs/SOURCE_NOTICE.md)。改动：只增加此说明并选择章节，所选原文未改写。

保留章节：1、2、3、4、6、9。

---

## 1. Essence, and what it is not

- **The objects are real**: scans of public-domain or licensed archive items, at their true proportions, with their real damage (broken corners, emulsion edges, folds, pencil marks). Nothing in them is drawn or generated.
- **Light comes from below**: the table glows a near-white cool grey; film and glass transmit it, paper glows warm at its edges, opaque things read darker than the table.
- **The loupe is the camera's door**: every dive into an object goes through a loupe that lands on it. The inside of the lens is where the object changes state.
- **Catalogue truth**: every object carries its real identifier, date and title from its holder; numbers on screen come from the record.
- **One signal colour** for marks, readings and anchors; everything else is the archive's own greys and paper tones.

**Sources and licences.** Open collections with masters and catalogue records: the Library of Congress (files on `tile.loc.gov`; records from its SRU server `lx2.loc.gov:210/lcdb` when loc.gov pages are blocked), Smithsonian Open Access (CC0), the Rijksmuseum (CC0), NARA, Europeana (check each item's rights statement). CC0, public domain and CC BY (credited) are fine. "No known restrictions", CC BY-SA and other terms are not CC0: name the terms to the user and ask. For brand history, ask the user for their scans, archive numbers and right to use them. Never stand a generated image in for an archive object. Keep a `FACTS.md` in the project folder (claim, source URL, quoted wording, or how a figure was derived) and deliver it with the film.

Not Halftone Dossier (no newsprint dots, no aged-paper grade), not Satellite Briefing (objects on a table, not the ground from orbit), not Data Storytelling (no charts; the numbers live on the objects), not a keynote (no slides or header bars).

## 2. Materials & rendering

- **One world, one camera**: every object is a textured quad on the table with a centre, rotation and scale (texture px → world units at true size). The camera is a 2D centre, zoom and roll; the table and every mark go through the same world → screen function.
- **The light table**: an emissive surface (≈ 0.97 white, slightly cool), soft falloff, diffuser noise, an aluminium frame and a dark desk beyond. It can be switched off (ambient ≈ 0.04) and flicker on.
- **Glass negatives**: transmission from the scan's positive, `T = 0.035 + 0.9 · (1 − pos)^1.25`, with a warm silver-gelatin tint; the emulsion mask comes from the scan (white margin touching the border = no glass), so broken corners show the table. Dust and scratches are procedural, anchored to the table.
- **Paper**: backlit, its colour is transmission (paper tone × light); lit lines get darker ink and brighter paper; unlit text can dim to bring one line forward.
- **The loupe**: inside the lens each pixel maps back to the table through the magnification (≈ 2.5×) with a pincushion term (k ≈ 0.16 at the rim), slightly different per RGB channel for colour fringes. Around it: a black ring with a bevel highlight and a clear acrylic skirt that refracts the table and glows at its foot. Landing and lifting, it scales by about 1.35× and casts a soft shadow.
- **The photograph space**: after the push the lens stops being a lens. A photo gains depth from a ground-plane nearness map (zero at the horizon, linear in the row below it), cut-out layers for upright subjects and a filled background; a dolly and a lateral shift drive parallax, and a subject layer may drift. Things left on the ground plane lean: centre the dolly between them.
- **Sampling**: all texture reads inside the branching lens code use explicit gradients (`textureGrad`), otherwise quads that cross a branch pick a wrong mip level and leave dashed seams.
- **Marks** live on a 2D canvas above the picture: hairlines 1.5–3 px, rings, crop corners, underlines, leaders. Table marks are clipped out under the loupe; marks inside a photograph use its forward mapping, parallax included.
- **Post**: a light vignette and fine moving grain (heavier inside photographs). No film damage, no sepia, no halftone.

## 3. Colour logic

- Neutral ground: the light table (near-white, cool) and the archive's own tones (silver greys, paper tans). Do not regrade the archive into a colour scheme.
- **One signal colour** (e.g. a signal orange) for marks, readings, anchors and the verdict; never as a fill behind pictures, never for decoration.
- Text is ink (near-black) on light areas and paper-white on dark caption plates; choose the contrast by the ground, never colour on colour.
- Positives inside the lens may be gently levelled (black and white points) so a weak scan reads; negatives stay as the glass gives them.

Example (our demo): table #F7F9FB, ink #15171A, signal #FF5A1F, caption plates rgba(14,15,17,0.74).

## 4. Type & subtitles

- **Roles**: a monospace for identifiers, dates and readings (e.g. IBM Plex Mono, 17–34 px; readings 74–120 px); a sans for labels in the film's language (e.g. Noto Sans SC or Inter, 21–36 px); a serif only for titles and the one name a photograph carries (60–76 px). OFL, self-hosted, CJK subset when needed.
- **Labels attach to objects**: an anchor dot and ring, a vertical leader, then the text. A reading sits in a dark caption plate with a small label above and the source (the catalogue number or the original wording) below.
- **Subtitles** are a caption strip at the bottom centre, on a dark plate with a 3 px signal-coloured edge. If the film is bilingual, the film's language goes on top. Hold ≥ max(1.8 s, speech + 0.6 s).
- **Quote the source when you can**: a crop of the actual line, or the record's wording in quotation marks, beats a paraphrase.

## 6. Camera grammar

| Move | What it expresses | Can serve |
|---|---|---|
| table glide (pan and roll) | surveying; moving to the next piece of evidence | a timeline of documents; a product family; an album |
| loupe landing + push into the lens | choosing one object; "look closer" | the claim; the key photograph; a signature |
| inside the lens: tracking along a line | reading | a letter, a ledger line, a caption, a spec |
| photograph space: dolly + parallax | being there | the event itself; the founding moment; the place |
| rise out of the lens | stepping back, the evidence noted | a transition; a summary |
| pull back to the whole table | scale; everything at once | an index, a timeline, a closing |

Framing: at a reading moment the subject fills at least a third of the frame height; readings and labels stay clear of the subtitle strip (bottom 140 px). Transitions are made by the loupe (land, push, rise, lift) and the glide; no cuts, fades to black or page turns between objects.

## 9. Pitfalls of the medium

- **Over-magnifying a weak scan**: keep the lens interior under about 1.5 screen px per scan px; choose items by scan size.
- **The loupe sweeping over empty table**: lay objects close together, land the loupe straight onto the object (drop in, don't slide in), and glide the camera over objects, not gaps.
- **Shear in the photograph space**: one depth map for a photo with people or machines in it tears them apart. Cut upright subjects into layers, fill behind them, and keep 2.5D moves small enough that the fill is barely seen.
- **Labels that scroll away**: a label on a moving table leaves the frame before it is read; hold the camera, or fix the caption on screen.
- **Vintage creep**: no sepia, no halftone, no paper-ageing overlay. The age is in the objects, not the grade.

