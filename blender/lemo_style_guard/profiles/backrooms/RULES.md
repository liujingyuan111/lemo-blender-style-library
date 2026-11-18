# 后室录像带 · Blender美术风格卡

原名：**Liminal Found Footage**。来源：[Lemo-Opuscar 固定版本](https://github.com/lemomo-ai/lemo-opuscar/blob/00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4/styles/backrooms/STYLE.md)。

本卡提取原作者美术约束；Blender做法标为适配建议。所有审美规则需人工审查，载入卡片不会自动判定达标。

## 原媒介与适配边界

- 原媒介：Three.js室内几何、自定义面板光照与雾，以及VHS摄像机后期。
- Blender路线：以三维室内材质、重复构成、平坦顶灯与摄像机媒介规则为约束；需要自行制作场景与合成。
- 边界：这是上游 Liminal Found Footage 风格，适配范围仅限该风格；原作者自定义无遮挡光照不能由普通 PBR 灯光设置自动等价获得。

## 必须保持

### backrooms-01 · 画面归属于同一台第一人称手持摄像机；媒介为1990年代VHS，原画幅为4:3。

**Blender适配建议：**从摄影机视角和镜头媒介出发制作；不要以第三人称展示摄影机无法到达的视角。此包只记录约束，不生成手持动画。

来源：§1. Essence, and what it is not；原文核对句：One first-person camcorder recording

### backrooms-02 · 4:3画面置于1920×1080画布中，两侧留柱状黑边。

**Blender适配建议：**在输出或合成中明确有效画面区域；不要把4:3源画面横向拉伸为16:9。

来源：§2. Materials & rendering；原文核对句：4:3 pillarboxed in 1920×1080.

### backrooms-03 · 空间是熟悉却不对劲的重复室内，以空旷、无人和日常机构性构造建立识别。

**Blender适配建议：**自行建立对应地点的室内构造与尺度；检查重复是否构成真实可走空间，而非随意拼贴物件。

来源：§1. Essence, and what it is not；原文核对句：An empty, familiar-but-wrong interior

### backrooms-05 · 保留克制的污损：少量水痕、变色带、剥落接缝和黄化或缺失顶板；干净感仍是风格的一部分。

**Blender适配建议：**为污损限定区域和密度，避免把全空间做成废墟；不为每一表面自动叠加相同脏污。

来源：§2. Materials & rendering；原文核对句：Restrained decay

### backrooms-06 · 密集顶灯构成平坦光照，不用清晰投影塑造戏剧性；接缝可由环境遮蔽加深。

**Blender适配建议：**这是原引擎的视觉目标。Blender可通过受控填光或专用材质近似，但需手动验证；不声称添加普通面积灯即可复现原算法。

来源：§2. Materials & rendering；原文核对句：Lighting = thousands of lights, no shadows

### backrooms-07 · 光板之间只有少量冷暖偏色、坏灯与闪烁差异，整体仍保持同一空间照明体系。

**Blender适配建议：**布光与材质变化维持小幅度；本规则不要求本包创建闪烁或曝光动画。

来源：§2. Materials & rendering；原文核对句：Per-light variation (a few % warm/cool/green)

### backrooms-08 · 远端走廊逐渐消失到黑暗，不能在尽头出现突兀的明亮背景平面。

**Blender适配建议：**检查体积雾、世界背景与远处灯光的联合作用；以画面中的远端亮度关系为准。

来源：§2. Materials & rendering；原文核对句：corridors dissolve into darkness, never a bright wall.

### backrooms-09 · 雾的亮度跟随局部照明；坏灯区域的雾也应暗，暗区轮廓不能被统一雾抬成灰色。

**Blender适配建议：**单一均匀体积雾可能不满足规则，需要局部控制或合成遮罩；是否成功由最终画面判断。

来源：§2. Materials & rendering；原文核对句：Fog follows local light

### backrooms-10 · 地点材料由一个病态主色统领，同色系深色线脚与斑驳地面配合；顶棚和灯板接近偏暖白。

**Blender适配建议：**先按地点锁定一个材质色族，再设计变化；原文的三套色板是替代选项，不应同时堆满一帧。

来源：§3. Colour logic；原文核对句：One dominant sickly hue

### backrooms-11 · 只允许一个高饱和信号色；泛光仅由这一信号产生。

**Blender适配建议：**为信号物体单独控制发光与合成阈值；人工检查其他材质、OSD或后期是否引入第二个高饱和视觉中心。

来源：§3. Colour logic；原文核对句：Exactly one saturated colour

### backrooms-12 · 白平衡允许漂移，成片不能呈现过于洁净的现代调色。

**Blender适配建议：**将媒介偏色与材质主色区分管理，避免把所有画面处理成中性、高通透的建筑可视化。

来源：§3. Colour logic；原文核对句：colour is never graded clean.

### backrooms-14 · OSD使用带黑色轮廓的位图字，独立于镜头桶形畸变和暗角。

**Blender适配建议：**将OSD置于镜头畸变之后的独立覆盖层；它属于摄像机显示，不贴在三维墙面上。

来源：§2. Materials & rendering；原文核对句：barrel + vignette on the image but **not** the OSD

### backrooms-15 · 场景告示呈办公室激光打印件的纸张与排版逻辑，固定在空间中并保持可读。

**Blender适配建议：**自行排版相应告示，用实际大小和拍摄机位审查文字；本包不提供演示告示内容。

来源：§2. Materials & rendering；原文核对句：office laser-print on yellowed paper, condensed sans headers

### backrooms-16 · 拍摄竖直纸面近景时降低机位、使镜头接近平行纸面，避免俯拍把字剪切成假斜体。

**Blender适配建议：**优先调整摄影机位置与朝向，检查透视变形及遮挡，不用后期拉正替代所有机位问题。

来源：§4. Type & subtitles；原文核对句：lower the camera so the lens is parallel to the page

### backrooms-17 · 闭路字幕位于4:3有效画面内、OSD上方，使用每行黑底白字的等宽排版，并保持不受磁带噪声污染。

**Blender适配建议：**将字幕独立于VHS处理链；检查字块边缘、居中位置和与OSD的间距。

来源：§4. Type & subtitles；原文核对句：Untouched by tape noise

## 禁用项

### backrooms-13 · 摄像机媒介使用VHS磁带和镜头缺陷，禁止CRT扫描线与RGB荫罩。

**Blender适配建议：**后期节点须按录像带成像设计；不要直接套用CRT电视屏幕材质。

来源：§2. Materials & rendering；原文核对句：No scanlines, no RGB mask.

### backrooms-18 · 不使用怪物特写、血腥图像或废墟式全面损坏来代替空旷与重复。

**Blender适配建议：**以空间、构图和媒介异常承载风格；没有为此规则补入角色、怪物或剧情内容。

来源：§1. Essence, and what it is not；原文核对句：no monster close-ups, no gore

## 推荐约束

### backrooms-04 · 隔墙与柱子围绕正交网格组织，留缺口和短墙，吊顶与嵌入式灯板有规律地重复。

**Blender适配建议：**使用模块化结构维持轴向和重复节奏；具体房间布局由项目决定，不复制演示路线。

来源：§2. Materials & rendering；原文核对句：axis-aligned partitions on a grid with random gaps and stubs

## 允许变化的内容边界

### backrooms-19 · 地点及其材料、路线和信号色可由项目决定，保留同一摄像机媒介与空旷重复的空间逻辑。

**Blender适配建议：**更换学校、机构或其他室内类型时，重新选择对应的材质色族；不要把某个黄色房间或演示路线误当唯一内容。

来源：§11. Variation space；原文核对句：the location and its materials

## 配色与允许变化

这是原文三个材质色板示例中的墙纸方案。池区或学校走廊可使用原文另外的文字／HEX方案；信号色由项目选择，本包不伪造其唯一HEX。

| 名称 | 原文色值 | 角色 |
|---|---|---|
| wallpaper | #d5bd66 | 原文墙纸示例 |
| trim | #4d3d26 | 同色族深色线脚示例 |
| carpet | #8c763c | 同色族地毯示例 |

## 材质起点

仅提供选择的材质配色参考；墙纸、地毯、污损、局部雾和VHS链仍需制作。原文没有规定Blender色彩管理或统一PBR粗糙度，因此不自动套入。

## 仍需人工判断

- 室内是否熟悉、克制、空旷，重复是否成立。
- 顶灯的平坦照明与暗区局部雾是否接近原风格。
- 是否仅有一个高饱和信号且只该信号泛光。
- VHS／镜头／OSD／字幕的分层是否正确。
- 具体告示排版、纸张尺度与最终文字可读性。

原文保留自身许可与影片制作额外许可；本卡为注明出处的约束整理及Blender转译，不含原演示故事、场景或素材。

本卡署名：**Lemo-Opuscar by Lemomo (LemoLab)**。文档及改编规则采用 [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)，保留上游影片制作额外许可。改动：中文整理、翻译及明确标记的 Blender 实施建议。
