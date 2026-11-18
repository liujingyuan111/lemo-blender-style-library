# 低多边形等距 · Blender美术风格卡

原名：**Low-poly Isometric Island**。来源：[Lemo-Opuscar 固定版本](https://github.com/lemomo-ai/lemo-opuscar/blob/00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4/styles/lowpoly-island/STYLE.md)。

本卡提取原作者美术约束；Blender做法标为适配建议。所有审美规则需人工审查，载入卡片不会自动判定达标。

## 原媒介与适配边界

- 原媒介：Three.js平面着色低多边形世界、正交摄影机与深度相关天空／AO后期。
- Blender路线：用低分面网格、平面法线、无纹理材质和正交摄影机建立微缩形态，布光与合成保持柔和低对比。
- 边界：这里只提供造型、材质、配色、投影与构图限制，不生成岛屿、六角地块、建筑、海面、天空、粒子或生长动画。原文没有HEX色板，本包不添加猜测色值。

## 必须保持

### lowpoly-island-01 · 世界以平面着色低多边形几何构成，棱面必须可辨。

**Blender适配建议：**网格使用平面法线与有意义的分面；审查轮廓和受光面，不把高模仅调低采样当低多边形风格。

来源：§1. Essence, and what it is not；原文核对句：flat-shaded low-poly geometry

### lowpoly-island-02 · 摄影机采用正交投影与等距视角，不能出现透视缩小或视场角透视变化。

**Blender适配建议：**将Blender摄影机设为ORTHO，以ortho_scale控制取景尺度；高度与方位可在原文镜头语汇中变化，不锁成唯一角度。

来源：§1. Essence, and what it is not；原文核对句：orthographic camera

### lowpoly-island-03 · 背景不出现写实地平线，远处世界融入屏幕空间天空渐变，呈悬浮于颜色中的模型感。

**Blender适配建议：**自行制作深度与渐变的衔接；只把World设为单色不足以满足该视觉关系。

来源：§1. Essence, and what it is not；原文核对句：No perspective and no horizon

### lowpoly-island-06 · 道具由盒、棱柱、低段圆柱圆锥和低细分二十面体等简单几何组合。

**Blender适配建议：**按用途控制几何层级，避免添加写实密集的小零件；原文列出的是造型词汇，不要求每个道具全用一遍。

来源：§2. Materials & rendering；原文核对句：boxes, prisms, low-segment cylinders and cones

### lowpoly-island-08 · 若使用地块，浅色上盖与较暗侧柱分离，侧柱顶部须低于盖面，地块间留小缝。

**Blender适配建议：**检查共面几何与接缝，避免z-fighting；规则针对有地块结构的项目，不要求所有内容都做成岛屿。

来源：§2. Materials & rendering；原文核对句：sink the side column's top below the cap

### lowpoly-island-09 · 环境遮蔽必须帮助读出地块缝隙与屋檐下方的结构。

**Blender适配建议：**Blender可选合适的AO或等效接触明暗方案；原引擎GTAO名称不直接转成Blender某个保证等价的开关。

来源：§2. Materials & rendering；原文核对句：it draws the seams between tiles and under roofs

### lowpoly-island-10 · 整体采用粉彩、低对比和少量重复色相：一个地面色族、中性岩石、少量墙与屋顶颜色。

**Blender适配建议：**每个项目自行确定有限色板，控制饱和度与对比；原文没有数值色板，本包不把任意HEX冒充源色。

来源：§3. Colour logic；原文核对句：Pastel, low contrast, a handful of hues

### lowpoly-island-12 · 若表现日夜或时间变化，光照与整个环境色彩应联动；地面分面随太阳重着色，夜晚环境向蓝紫去饱和。

**Blender适配建议：**项目使用日夜变化时，应共同管理天空、水色、太阳与表面受光；本包不创建日夜动画。

来源：§3. Colour logic；原文核对句：night desaturates everything toward blue-violet.

### lowpoly-island-13 · 夜景中，暖色发光体是唯一明亮物体；其余环境保持低亮度。

**Blender适配建议：**按最终画面曝光与高亮分布检查；不要让环境HDRI或水面尖锐反光压过窗灯等暖色发光点。

来源：§3. Colour logic；原文核对句：At night, warm emissives are the only bright things

### lowpoly-island-14 · 水面若存在，应保持分面和受控高光；水面不接收阴影。

**Blender适配建议：**为项目水面单独设置受光逻辑，并检查反射亮斑是否破坏柔和粉彩。原文水面实现需专门转译。

来源：§3. Colour logic；原文核对句：water receives no shadows.

### lowpoly-island-16 · 通过正交视锥高度调整画面尺度，摄影机距离至少为视锥高度的三倍，防止画面底部看进海面下方。

**Blender适配建议：**根据实际画幅宽高比求出正交视锥的垂直高度，再核对摄影机与目标的距离；不能不顾宽高比直接把所有场景的ortho_scale当垂直高度。摄影机裁剪、目标高度与水面仍需人工核对。

来源：§6. Camera grammar；原文核对句：place the camera ≥ 3 × frustum height away

### lowpoly-island-18 · 字幕无底框，暖白字带柔和深蓝投影，居中靠下；画面文字卡保留能看到世界的空隙。

**Blender适配建议：**在实际输出画面检查字幕层与世界的留白关系；不导入示例字幕或标题内容。

来源：§4. Type & subtitles；原文核对句：A text card over the world leaves a gap where the world stays visible.

## 禁用项

### lowpoly-island-04 · 不使用纹理贴图、像素纹理或写实照片细节。

**Blender适配建议：**为适用对象检查图像纹理与材质输入；颜色主要来自材质和光照。此规则不等于禁止天空后期渐变。

来源：§2. Materials & rendering；原文核对句：no textures

### lowpoly-island-05 · 不使用圆滑法线、次表面散射或平滑三维卡通式的柔软表面。

**Blender适配建议：**保留平面着色，检查Subdivision、Auto Smooth等是否改变预期分面；不把软光误解为需要圆滑模型。

来源：§1. Essence, and what it is not；原文核对句：no rounded normals, no subsurface

### lowpoly-island-11 · 不用黑色材质与轮廓描线；暗部由阴影和AO形成。

**Blender适配建议：**检查材质、Freestyle和合成描边；通过结构受光分开面，不用外框线补可读性。

来源：§3. Colour logic；原文核对句：No outlines, no black; shadows and AO are the only darks.

## 推荐约束

### lowpoly-island-07 · 材质偏哑光，原文参考粗糙度约0.9；地块明度可作少量差异。

**Blender适配建议：**可将Blender粗糙度约0.9作为起点，再对照受光结果；不统一锁死所有水面或发光物体的参数。

来源：§2. Materials & rendering；原文核对句：roughness ≈ .9

### lowpoly-island-15 · 关键镜头中太阳相对摄影机保持侧向，避免低位逆光把分面水面变成眩光。

**Blender适配建议：**以摄影机、太阳和水面的实际关系构图，不固定某个世界坐标方向。

来源：§3. Colour logic；原文核对句：Keep the sun sideways to the camera in key shots

## 允许选择的语汇

### lowpoly-island-17 · 俯仰角可变：低角度约20–25度会展开天空，高角度约50度更像地图；这些是镜头选项。

**Blender适配建议：**按项目镜头目的选择角度，保持正交投影；不把单一角度设为所有镜头硬要求。

来源：§6. Camera grammar；原文核对句：low (≈20–25°) widens the sky band; high (≈50°) reads as a map

## 允许变化的内容边界

### lowpoly-island-19 · 具体世界、色板和摄影机路径可由项目决定，仍满足原文的造型、投影与配色逻辑。

**Blender适配建议：**为不同内容选择自己的少量粉彩色值和几何词汇；不强制沿用演示岛屿、某座建筑或相机路线。

来源：§11. Variation space；原文核对句：the palette within the colour logic

## 配色与允许变化

原文只有沙地／草地／珊瑚屋顶、雪地／松绿／红木屋等文字配色例子，没有HEX。保留少色、粉彩、低对比、不用黑色的约束，具体色值由项目填写，不附猜测样板。

## 材质起点

提供平面造型与哑光材质的适配方向，不自动创建色板。Standard只是Blender起点建议，不声称等同原文Three.js Neutral tone mapping；需对照最终粉彩层次手动调整。

## 仍需人工判断

- 正交构图、无地平线与远处天空渐变是否成立。
- 几何分面是否清晰，是否误用平滑法线或写实细节。
- 粉彩少色、暖夜灯、无黑材质与AO暗部的关系。
- 水面高光、接触暗部与昼夜配色联动。
- 具体字体、字幕占比和留白的最终可读性。

原文保留自身许可与影片制作额外许可；本卡为注明出处的约束整理及Blender转译，不含原演示故事、场景或素材。

本卡署名：**Lemo-Opuscar by Lemomo (LemoLab)**。文档及改编规则采用 [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)，保留上游影片制作额外许可。改动：中文整理、翻译及明确标记的 Blender 实施建议。
