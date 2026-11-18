# 微游戏快闪 · 原文美术章节

来源：Lemo-Opuscar by Lemomo (LemoLab)。原文：[STYLE.md](https://github.com/lemomo-ai/lemo-opuscar/blob/00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4/styles/microgame/STYLE.md)。

固定提交：`00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4`。原文 SHA-256：`04e2b7fa9dee5cac346b475e400e577e977b6753afe35ee4e45f66111496ce6a`。

本页按章节摘录原作者的美术资料，保留所选章节原文；不是 Blender 原生实现，也不是已经通过的美术验收。原文中的示例、选项和建议保持原有含义，不自动升级为硬限制。某些原文章节顺带包含字幕、流程或声音提醒，它们仍是参考文字，不会加载为 Blender 约束。

文档许可：[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)，另有上游对自有／客户影片制作的额外许可，见[来源说明](../docs/SOURCE_NOTICE.md)。改动：只增加此说明并选择章节，所选原文未改写。

保留章节：1、2、3、4、6、9。

---

## 1. Essence, and what it is not

- **A microgame = a shouted command word + 2.5–4 s + one action + one result** (success, or a funny failure).
- **Each microgame uses a different visual medium** (crayon, ink wash, terminal, risograph, pixel, blueprint, Swiss type, clay, cut paper, woodcut…). The jolt of each switch is both the joke and the beat.
- **One fixed home look** holds the film together: a show stage with a host, a lives counter and a stage number, which the film returns to between games.
- **It keeps accelerating**: every few games tempo, game length, dwell, command hold and animation frame rate step up together.
- **The hero survives every medium** by keeping two or three silhouette marks.

Not Rhythm Game Show (one art style, rounds of bars, call-and-response), not a style sampler reel (every game has stakes; lives connect them), not a montage (each game has a rule grasped in under a second).

## 2. Materials & rendering

- **Home stage**: flat toon, thick near-black outline (~7 px), flat fills, **one hard-edged shadow** (fill in the shade colour, clip to the shape, refill shifted up-left). Fixed furniture: a frame-within-the-frame where games play (a TV, an arcade cabinet, a phone, a window), the lives board, a stage badge, a trigger prop (button, lever, bell).
- **Each medium is a simplified re-drawing, 100–200 lines of code**, built around one channel trick that makes it read at a glance:
  - drawn media store **pressure or wetness in a channel** (crayon: alpha = pressure against paper tooth; ink: wet and dry ink channels);
  - print media store **plate densities** (riso: a channel per plate, additive overprint, halftone, misregistration);
  - screen media are **low-res buffers** scaled up (pixel: indexed buffer, auto outline, dither; terminal: hand-authored glyph art, phosphor shader);
  - technical media are **line systems** (blueprint: line weights and dimensions; Swiss: a strict grid, one sans, one signal colour).
- **Hero translation**: the hero is redrawn from scratch in each medium, but the same marks always survive (e.g. a hat shape, one coloured dot, a number on the chest). Make a model sheet of the hero in every medium before animating.
- **Mixed-media frames**: alpha-coverage media over a base, paper media multiplied, screen media flat and clipped to a panel. WebGL2 material shaders turn the channel buffers into each look.

## 3. Colour logic

- **The home stage owns a saturated party palette**: a deep ground behind a rotating sunburst, two or three loud accents, plus a fixed success colour and a fixed fail colour used by stamps and the lives board only.
- **Each medium brings its own palette** from its tradition (wax colours, one-ink-plus-vermilion, amber phosphor, three riso plates, a limited pixel palette, white-on-blue, black-white-red). Never tint a medium with the home palette.
- **One accent follows the hero across media** where the medium allows (a single vermilion dot in ink, an inverse glyph in a terminal, a signal-red circle in Swiss type): it is how the eye finds the hero after a switch.
- Example home palettes: violet `#2a0f5c` with magenta `#ff2e88`, gold `#ffc928`, cyan `#1fd1d1`; teal ground with coral and lemon; black stage with hot orange and electric blue.

## 4. Type & subtitles

- **The command word is the subtitle**: a heavy display face (e.g. Titan One), white with a thick ink outline, a coloured drop and a burst behind it, skewed a few degrees. It slams in over ~3 frames (overshoot → settle), holds, then **shrinks into a corner tag before the first action**, so the result is never covered. One-off banners fly out instead of tagging, so tags never pile up.
- **Other lines**: a rounded card in the home palette with the home outline and hard shadow, a friendly rounded face (e.g. Lilita One ~50 px), a small speaker icon; placed above the timer in games. Hold ≥ max(1.8 s, speech + 0.6 s), never under a big banner.
- Inside a game, any text (replay captions, labels) uses **that medium's own typography**.
- The command word appears in the .srt only, never burned twice.

## 6. Camera grammar

A vocabulary, not a route. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Start inside a game, command already slamming | the rules explain themselves | throwing the viewer in |
| Pull back out of the game screen | scale: this was one screen on a show | the first return to the stage |
| Locked frontal home frame | the constant; only the scoreboard changes | stage beats; the host's reaction |
| Slot reels (the stage splits into spinning strips of earlier frames, stopping one per beat) | acceleration, a summary | a speed-up; a change of round |
| Extreme insert on the trigger prop | the start, felt | a game starting on the downbeat |
| Lights cut to one top spot, frame unchanged | stakes; the last chance | the last life; a decision |
| Tile flip (last frames of past games flip into pieces of a new frame) | the past becomes the material of the present | a boss or finale; a recap |
| Push into a detail, hold | the viewer notices before the hero does | a clue; a silence |
| Snap back to wide on one beat | release | a solution blooming; a save |
| Split screen, two media side by side | comparison, rivalry | two players; before/after; two approaches |

Framing: the game screen is a fixed fraction of the frame (around 40 % of the width); in a mixed-media frame keep **one focal chain** (A leads to B leads to C) and push info panels into a corner.

## 9. Pitfalls of the medium

- **A luminance-ramp ASCII figure is mush** → hand-authored glyph art with structural glyphs, an inverse glyph for the accent.
- **Ink shapes read as smoke** unless their silhouette is designed (a short round blot phase, then a clear structure with seams and light edges).
- **A failure at high tempo goes unread** → make the action overshoot and hit something, or give it an instant replay.
- **Alpha-coverage media show the background through gaps** → a full-pressure base where it must be solid.
- **Drawing helpers with a global context** draw on the wrong canvas when scenes render into offscreen buffers (game screen, reels, tiles) → set and restore the context.
- **Command tags pile up** → secondary commands fly out.
- **A 100 % white flash** reads as a blank frame → cap at ~60 %.
- **TTS single-word commands** gain a vowel tail ("Pump!" → "Pompey") → generate a two-word phrase and cut after the first word using ASR timestamps; verify each clip, since ASR mishears 0.2 s words in a dense mix.

