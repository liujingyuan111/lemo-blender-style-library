# 剪影律动 · Blender美术风格卡

原名：**Silhouette Rhythm**。来源：[Lemo-Opuscar 固定版本](https://github.com/lemomo-ai/lemo-opuscar/blob/00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4/styles/silhouette-rhythm/STYLE.md)。

本卡提取原作者美术约束；Blender做法标为适配建议。所有审美规则需人工审查，载入卡片不会自动判定达标。

## 原媒介与适配边界

- 原媒介：二维剪影／倒影／水光图层，与片元着色器的天空和水面合成。
- Blender路线：用二维或压平的三维轮廓承载主体，背景与水面独立布置；在构图中保持单黑形的读图逻辑。
- 边界：本卡保存轮廓、色彩、光影和摄影机约束；不附天空、水面、体积光、角色或节奏动画的实现。

## 必须保持

### silhouette-rhythm-01 · 主体必须读成一个完整黑色形状，身份与表演由外轮廓承担。

**Blender适配建议：**建议用统一剪影材质或独立剪影图层；从最终摄影机检查剪影的整体外轮廓，不能只检查模型细节。

来源：§1. Essence, and what it is not；原文核对句：The figure is one black shape.

### silhouette-rhythm-04 · 剪影始终落在明亮背景上，可依靠太阳、亮地平线或水面光带衬托。

**Blender适配建议：**在摄影机画面中分别检查主体各部分；仅有背光灯但主体仍落在暗水面上，不能视为满足规则。

来源：§1. Essence, and what it is not；原文核对句：A silhouette sits on light, never on dark.

### silhouette-rhythm-05 · 主体保持带微量紫色倾向的近黑，不随天空或场景改成彩色主体。

**Blender适配建议：**把主体颜色单独管理，避免受彩色灯或环境反射改色；示例HEX只作参考，近黑紫的角色保持一致。

来源：§3. Colour logic；原文核对句：The figure colour is fixed: near-black with a trace of violet.

### silhouette-rhythm-06 · 天空色域限于金、橙、珊瑚、绯红、洋红、紫罗兰，不加入绿色、蓝天或灰天空。

**Blender适配建议：**为天空建立受限色带并逐帧审看最终合成；不能直接套入任意HDRI天空。

来源：§3. Colour logic；原文核对句：No green, no blue sky, no grey.

### silhouette-rhythm-07 · 最亮区域属于太阳、地平线亮带与水面反光；文字使用太阳系的奶油色。

**Blender适配建议：**以最终画面亮度关系审查主次；文字不应比太阳高亮更抢眼。

来源：§3. Colour logic；原文核对句：Brightest values belong to the sun, the horizon band and the light on the water; type uses the sun's cream

### silhouette-rhythm-08 · 允许朝日侧的细薄光学亮缘和柔和晕光，靠近太阳时更明显；不能把它画成全轮廓描边。

**Blender适配建议：**将环境光学效果放在独立合成层或受方向限制的遮罩中；单独检查主体黑形与外部亮缘，保留两者区别。

来源：§2. Materials & rendering；原文核对句：a thin rim on the sun-facing edge and a soft halo

### silhouette-rhythm-09 · 水面承接天空与主体倒影；主体倒影围绕水线翻转，再进行扰动与压暗。

**Blender适配建议：**若画面使用水面，反射轮廓必须与主体对应；反射变形绑定世界关系，不能无理由另画一种形状。

来源：§2. Materials & rendering；原文核对句：Reflections of figures are the same shapes flipped about the waterline, wobbled and darkened.

### silhouette-rhythm-10 · 水波同时保留亮波峰和暗波谷；水滴是亮珠，不能成为黑色飞点。

**Blender适配建议：**为水光和暗反射分别处理可读性；检查逆光水滴是否被主体材质错误染黑。

来源：§2. Materials & rendering；原文核对句：bright beads, never black specks.

### silhouette-rhythm-11 · 摄影机以水平水面为基准；单镜头内地平线保持水平，不能用荷兰角倾斜画面。

**Blender适配建议：**锁定并检查摄影机滚转与水面基准；机位升降、焦距和构图变化仍需逐镜头判断。

来源：§5. Motion quality；原文核对句：the horizon line within a shot (no dutch tilt)

### silhouette-rhythm-13 · 关键时刻主体至少占画面高度三分之一；远景仍须把主体放在亮区。

**Blender适配建议：**按渲染画面测量关键镜头主体包围框；比例规则针对关键时刻，孤独等有意小主体构图需另行人工说明。

来源：§6. Camera grammar；原文核对句：at the key moments the subject fills ≥ 1/3 of the frame height

### silhouette-rhythm-15 · 文字置于下方暗水面，左对齐；不放在太阳内部，不居中，不加阴影或描边。

**Blender适配建议：**将文字单独排版并检查背景亮度与轮廓避让；字幕沿同一奶油色体系。

来源：§4. Type & subtitles；原文核对句：never inside the sun, never centred, no shadow or stroke.

### silhouette-rhythm-16 · 天空、太阳、水面和光学关系共用同一空间与色彩逻辑；天空渐变不能污染主体单黑形。

**Blender适配建议：**分别控制主体与背景的色彩通道，最后在合成结果中检查明暗二分；不能靠材质节点名称判断完成。

来源：§3. Colour logic；原文核对句：Two values carry the frame: black figure and bright ground. Everything else is the sky's gradient.

## 禁用项

### silhouette-rhythm-02 · 主体内部不增加明暗渐变、纹理细节、图形描边或用于造型的内部阴影。

**Blender适配建议：**主体参考材质采用不受灯光塑形的单色方案；手工检查表面高光、纹理、法线和投射细节是否破坏单黑形。

来源：§1. Essence, and what it is not；原文核对句：No detail inside it, no gradient, no outline, no shadow.

### silhouette-rhythm-03 · 不引入可见操纵杆、纸张纹理、灯后幕布、层叠纸片或轮廓内装饰。

**Blender适配建议：**不要沿用皮影或剪纸灯箱的材质与结构；这里的黑形没有纸材身份。

来源：§1. Essence, and what it is not；原文核对句：no visible rods, no paper texture, no lamp behind a screen

## 推荐约束

### silhouette-rhythm-14 · 优先侧面可辨的姿态，关键轮廓之间留空气，避免多个主体或肢体重叠为黑团。

**Blender适配建议：**用摄影机视角或剪影预览检查负形，必要时调姿态和相对位置；不依靠内部描线解读重叠。

来源：§9. Pitfalls of the medium；原文核对句：at key moments leave air between contours and keep limbs in profile.

## 允许选择的语汇

### silhouette-rhythm-12 · 长焦压缩、让太阳占据较大画幅，是可选镜头语汇，不是每镜必用。

**Blender适配建议：**可用长焦透视摄影机和受控太阳画面尺度实现；不把某个毫米数或固定太阳大小写成全片硬参数。

来源：§6. Camera grammar；原文核对句：Telephoto, sun filling half the frame

## 允许变化的内容边界

### silhouette-rhythm-17 · 主体种类与光源所在场合可改变，仍保持暖色色域、单黑轮廓与明亮背景。

**Blender适配建议：**可替换自己的主体与场合；不要为了换题材把轮廓内部加上表情、纸纹或彩色明暗。

来源：§11. Variation space；原文核对句：the cast (animals, dancers, athletes, vehicles), the place of the light

## 配色与允许变化

这些HEX全部来自原文明确标注的演示示例；可在原文暖色色域内调整。主体近黑紫、亮背景与暖色天空的关系是规则，示例HEX不是唯一合法色值。

| 名称 | 原文色值 | 角色 |
|---|---|---|
| figure | #090307 | 近黑紫主体示例 |
| sun | #FFF6DC | 太阳与文字奶油色示例 |
| gold | #FFB347 | 天空金色示例 |
| coral | #FC4D2B | 天空珊瑚色示例 |
| magenta | #E0245C | 天空洋红示例 |
| violet | #380A52 | 天空紫罗兰示例 |
| deep_violet | #1A083D | 深紫收束示例 |

## 材质起点

用于剪影主体的单色参考；Standard是Blender适配建议，需对照最终显示结果。天空渐变、水面反射、朝日细缘及晕光仍需独立制作，不通过纸纹或外描边补齐。

## 仍需人工判断

- 轮廓是否可辨、肢体是否重叠为黑团。
- 主体是否始终落在亮背景以及关键构图的占比。
- 朝日光学细缘与禁止的全轮廓描边的区别。
- 天空、水面、倒影的空间与色彩一致性。

原文保留自身许可与影片制作额外许可；本卡为注明出处的约束整理及Blender转译，不含原演示故事、场景或素材。

本卡署名：**Lemo-Opuscar by Lemomo (LemoLab)**。文档及改编规则采用 [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)，保留上游影片制作额外许可。改动：中文整理、翻译及明确标记的 Blender 实施建议。
