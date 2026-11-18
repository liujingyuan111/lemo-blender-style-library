# 像素小人录屏 · 原文美术章节

来源：Lemo-Opuscar by Lemomo (LemoLab)。原文：[STYLE.md](https://github.com/lemomo-ai/lemo-opuscar/blob/00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4/styles/living-screencast/STYLE.md)。

固定提交：`00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4`。原文 SHA-256：`62389f107308c738854f103e96c2b2e8bc47a14e28bf1081f15976d90e89b5f9`。

本页按章节摘录原作者的美术资料，保留所选章节原文；不是 Blender 原生实现，也不是已经通过的美术验收。原文中的示例、选项和建议保持原有含义，不自动升级为硬限制。某些原文章节顺带包含字幕、流程或声音提醒，它们仍是参考文字，不会加载为 Blender 约束。

文档许可：[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)，另有上游对自有／客户影片制作的额外许可，见[来源说明](../docs/SOURCE_NOTICE.md)。改动：只增加此说明并选择章节，所选原文未改写。

保留章节：1、2、3、4、6、9。

---

## 1. Essence, and what it is not

The film looks like a **screen recording of the real product**, but it is not a recording. Every window, menu, diff line and button is **redrawn in 2D (HTML/CSS/SVG)**, so the camera can go anywhere, every pixel is controllable and text stays sharp at any zoom.

A **mascot made of big square pixels** lives in that high-resolution world. The clash of two resolutions, a hard-edged low-res sprite against anti-aliased UI, is the look.

The mascot is the software's agency made visible: when the software reads, it runs along the rows it reads; when it plans, it holds a pixel pencil; when it tests, it stomps the button.

**Two actors, never a hand:** the **cursor** is the user; the **mascot** is the software.

Not a dark tech keynote (no black stage, no invented abstract UI: this is the real product), not a pixel-art game (the world is hi-res vector UI; only the mascot and its props are pixels), not a real capture (nothing is a screenshot).

## 2. Materials & rendering

- **Real UI, redrawn**: every label, mode name and shortcut matches the real product; no screenshots, no lorem ipsum. Demo content (code, data, test output) is coherent, and the app under test really changes.
- **Pixel grid is sacred**: the mascot, its props (pencil, "!", sparkles, heart, dust) and trails share one square-pixel grid with crisp edges. It scales with the camera; its position snaps to half-pixels, so its motion feels stepped.
- **Gravity = top edges of UI**: the mascot only stands on the top edge of a real element (input box, menu, list row, code line, button, status bar, the letters of a heading). Its position comes from **measuring the live DOM** every frame, never hand-placed coordinates.
- **Window on wallpaper**: the app floats on a desktop with a soft shadow; zoom never shows beyond the monitor.
- **Depth** only where it serves attention: rack focus (blur the pane that doesn't matter), a vignette spotlight. Never blur text the viewer must read.
- **Motion blur** is derived from camera speed and applied as an anisotropic blur on an **untransformed wrapper**, only on whips. Slow moves stay sharp.

## 3. Colour logic

- The product's own interface colours rule: follow its real light and dark themes exactly.
- The mascot keeps the product's or brand's mascot colour, or one saturated hue that no UI element uses, so it finds the eye in any frame.
- Overlays (chapter pill, key HUD, captions) are neutral frosted glass; one accent at most, taken from the product.
- A theme switch can be a story event: the whole film may change state with it.

## 4. Type & subtitles

- UI type follows the product (or licence-free look-alikes such as Inter, JetBrains Mono, a serif for editorial UIs).
- **Information layers only**: a chapter pill (01–04), a KeyCastr-style keystroke HUD, frosted-glass caption pills, an optional "▶▶ 4×" time-lapse tag. Nothing else overlays the screen.
- Captions sit in a pill at the bottom, never over the element being discussed and never under the mascot; hold ≥ max(1.8 s, speech + 0.6 s).
- A title, if any, is diegetic: it appears as part of the UI (an empty-state heading, a window title, a notification).

## 6. Camera grammar

A recording-software camera: one continuous take inside the screen, zoom ≥ 1, cuts only under chapter transitions. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Push-in to the cursor or caret | "this is where it happens" | typing a prompt; choosing a menu item; a setting |
| Slow drift at rest | the app is alive while we listen | a line of narration; waiting for a result |
| Whip-pan between panes (with blur) | cause here, effect there | sending a message → a result appearing; code → preview |
| Push-in + vignette freeze | the one promise to remember | a safety guarantee; a price; an undo |
| Rack focus between panes | attention moves, nothing else does | reading files; logs scrolling while chat waits |
| Pull back to the full window | the whole workflow in view | a summary; parallel tasks; before/after |
| Follow the mascot along a list | the software working through items | scanning results; a checklist; a migration |
| Split-window reframe | two things at once | parallel sessions; compare two versions |

Framing: the thing being discussed and its caption never overlap; the mascot never covers text to be read. Transitions: chapter pill wipes, pixel wipes, a theme reveal circle; never dissolves or screenshots.

## 9. Pitfalls of the medium

- Invented features or renamed modes → check every button, mode and shortcut against the product's documentation; if it isn't in the docs, it isn't in the film.
- The mascot floats or drifts off its element → measure the DOM every frame, stand only on top edges.
- The mascot covers text or sits under a caption → reserve a text-free lane for it.
- Blur-filter "fake depth" on text you want read, or zooming out past the screen → rack focus only on panes not being read; zoom ≥ 1.
- A hand, arm or finger on screen → the cursor is the user.
- Motion blur applied to a transformed layer smears the pixel sprite wrong → blur an untransformed wrapper, and only on whips.
- A keypress or pop landing on a product name masks it → shift foley off word onsets; re-check with whisper on the final mix.
- TTS mispronounces the product name → try voices and spellings, verify with whisper.

