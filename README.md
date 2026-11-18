# Lemo 美术风格约束库 · Blender / AI

把 **Lemo-Opuscar 的美术风格限制**整理成可追溯、可检索、可供本地 AI 读取的资料，并映射到 Blender 制作流程。重点是配色、材质、轮廓、构图、光影、摄影机、文字和跨镜头一致性。

**版本 0.4.0 · 99 套原文资料 · 8 套 Blender 中文约束 · 150 条规则。**

原作者：**[Lemo-Opuscar by Lemomo (LemoLab)](https://github.com/lemomo-ai/lemo-opuscar)**。上游固定提交：`00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4`。本库是独立整理与 Blender 适配项目。

## 本地 AI 从这里开始

需要 Python 3.10 或更新版本。检索和导出只使用标准库，不需要联网、API Key 或安装 Blender。

```bash
git clone https://github.com/liujingyuan111/lemo-blender-style-library.git
cd lemo-blender-style-library

# 列出已整理的 8 套 Blender 约束
python tools/ai_context.py list --blender-only

# 在风格资料中检索
python tools/ai_context.py search "剪影"

# 导出一套风格给本地 AI（输出文件必须尚不存在）
python tools/ai_context.py export spy-titles --format md --output spy-titles-context.md
```

给能读取本地文件的 GPT、Codex、Claude、Gemini 或其他助手这样说：

> 请先读取这个仓库的 AGENTS.md 和 AI_START_HERE.md。为我的 Blender 项目采用 spy-titles 风格，只读取这一套的规则及必要的原文。先列出必须保留、明确禁用、允许变化，以及如何在材质、轮廓、光照、摄影机上落实。原文要求和你推导的 Blender 建议分开写。接下来根据我的内容制作，最终对照实际渲染逐条核对。

把 `spy-titles` 换成选中的 `style_id`。不具备本地文件读取能力的客户端，可上传导出的单风格 Markdown；机器集成可改用 `--format json`。客户端也可通过 GitHub 文件链接读取，但需有相应的网页或仓库读取能力。

| 入口 | 用途 |
|---|---|
| [AI_START_HERE.md](AI_START_HERE.md) | 本地 AI 接入、复制即用的指令和工作流 |
| [AGENTS.md](AGENTS.md) | 仓库级读取顺序、来源优先级、规则与建议的边界 |
| [llms.txt](llms.txt) | 轻量索引，按需寻找资料 |
| [catalog/styles.json](catalog/styles.json) | 99 套风格目录及明确的 Blender 适配状态 |
| [START_HERE.html](START_HERE.html) | 下载仓库后在浏览器打开的离线阅读器 |

这些入口是普通文本文件。不同 AI 客户端的自动发现机制不同；必要时显式要求它读取入口。

## 已完成的范围

| 内容 | 数量 | 状态 |
|---|---:|---|
| 原始 STYLE.md 与配置 | 99 套 | 按固定提交保留原始字节，可校验来源 |
| 原文美术章节摘录 | 99 套 | 保留所选章节原文及出处 |
| Blender 中文风格约束 | 8 套、150 条 | 分级规则、原文短引、Blender 建议、人工核对项 |
| 其余原文风格 | 91 套 | reference_only，尚未完成 Blender 约束整理 |

本库提供风格规范和读取工具。材质、光照、摄影机与构图仍需落实到具体项目；加载规则不会自动产生符合原作审美的画面。

## 首批 8 套 Blender 约束

| 风格 ID | 原风格 | 核心美术限制 | Blender 对应方向 |
|---|---|---|---|
| spy-titles | 60s 间谍片头 | 四墨平色、固定手剪边、轻微纸层关系、文字参与结构 | 平面或浅层纸片，轮廓与纸影分别处理 |
| silhouette-rhythm | 剪影律动 | 单黑形、无内部细节、亮背景、暖色光环境 | 优先保证轮廓与侧面姿态可读 |
| shadow-puppet | 皮影戏 | 透光染色皮片、刻孔、关节、操纵杆、幕与背光 | 材料透光和幕布关系 |
| paper-lantern | 纸雕灯影 | 箱内平行纸层、近暗远亮、软投影、内部暖光 | 有限深度叠纸及灯光；箱外物件可有正常体积 |
| paper-popup | 纸片立体书 | 纸片世界、折痕、暖白切边、深棕墨、书页关系 | 纸片与书页层次；书及外部环境可有正常体积 |
| backrooms | 后室录像带 | 4:3 摄像媒介、重复空室、克制损坏、有限信号色 | 空间、材质及镜头媒介约束 |
| white-model | 白模投影 | 真实地点与比例、哑光白模、颜色来自投光 | 模型本体和投影色分开 |
| lowpoly-island | 低多边形等距 | 正交、平面法线、无纹理、粉彩少色、无黑色描边 | 投影、面结构、色彩和阴影职责 |

完整规则位于 `blender/lemo_style_guard/profiles/<style_id>/`。每套同时提供适合人读的 `RULES.md` 和适合工具读取的 `contract.json`。

## Blender 安装和使用

插件最低声明版本为 Blender 4.3，集成验证版本为 **4.3.2**。从源码生成安装包：

```bash
python tools/build_package.py
```

然后在 Blender 中：

1. 打开 `Edit → Preferences → Add-ons`，从菜单选择 **Install from Disk**，安装 `dist/lemo_style_guard-v0.4.0.zip` 并启用 **Lemo 美术风格约束**。
2. 在 3D 视图按 `N`，打开 **Lemo 风格**，选择风格并点击 **载入美术风格约束**。
3. 按配色、材质、构图等类别查阅规则和原文依据，在自己的工程中实施。
4. 对照实际渲染逐条勾选 **已人工核对画面**，点击 **生成风格核对记录**。

规则卡和核对记录保存在 `.blend` 的文本数据块中，可在 Text Editor 阅读。每个 Scene 独立保存记录。安装步骤依据 [Blender 4.3 官方手册](https://docs.blender.org/manual/en/4.3/editors/preferences/addons.html)。

载入只附加规则、来源和核对状态。可选的 **创建原文参考色板** 按原文 HEX 创建未分配的取色参考材质；这些材质用于选色，不是已经完成的表面着色器。皮影、立体书和低多边形三套没有原文 HEX，保留文字色彩约束供项目自行选色。

也可对已有工程附加规则并另存为新文件：

```bash
blender -b your-project.blend --python-exit-code 1 --python tools/load_style.py -- --style spy-titles --output your-project-with-style.blend
```

输出路径必须不存在；加 `--reference-swatches` 可同时创建未分配的原文取色参考。

## 原文要求与实施建议

| 字段 | 含义 |
|---|---|
| rule_zh、level | 中文整理及原文强度：必须、禁止、建议、可选、示例 |
| source_section、source_quote | 可回查的原章节和连续原句 |
| blender_translation | 本库提出的 Blender 实施建议 |
| palette.status | 色值来源；当前色板均标为 source_example |
| material_recipe.origin | 显式标明为 Blender 适配建议 |
| review: manual | 要对照画面人工判断，程序不自动验收美术 |
| attribution | 原作者、许可、原文 URL 与改动说明，随单份合同保留 |

原文的示例色不能升级为唯一允许色。原文像素值需按最终画幅校准，不能直接当成 Blender 米数。选择一套主风格后保持其材质、轮廓、摄影机和色彩职责；要融合风格时，先明确冲突和新的衍生规范。

## 来源与许可

这是一个**公开风格资料库，许可按内容区分**：

- 上游风格文档、摘录、中文规则、合同 JSON 及内嵌这些规则的导出内容：**CC BY-NC 4.0**，保留原作者额外的影片制作许可。
- 上游配置 `style.json`：上游 **MIT** 条款。
- 本库新增的 Blender 加载器、检索导出和验证代码：**MIT**。

文档可按非商业条款公开分享。原作者另允许使用和改编文档制作自有或客户影片，包括商业影片，并在相应影片项目交付中包含文档；该额外许可并不将文档整体改为无限制商业许可。完整范围见 [LICENSE](LICENSE)、[NOTICE.md](NOTICE.md)、[来源说明](docs/SOURCE_NOTICE.md) 和保留的 [上游 LICENSE](source/lemo-opuscar/LICENSE)。

原始文件保持不变；章节摘录只选取原文；中文规则是翻译和整理；Blender 转译与工具为本库新增。外部贡献署名：**Memphis Diorama — EianLu**；**Crayon World 3D — 2nd1st**。本库不代表原作者官方维护或认可。

## 维护与验证

```bash
python tools/check_contracts.py
python -m unittest discover -s tests -p test_ai_context.py
python tools/extract_style_sources.py
python tools/build_package.py
node tests/test_reader.cjs
```

前两项检查规则来源和 AI 导出行为；第三项可离线重新生成原文摘录与目录；构建输出位于 `dist/`。Blender 集成测试位于 `tests/test_blender_guard.py` 和 `tests/test_install.py`，核对加载、工程状态保持、人工记录保存和真实 ZIP 安装。验证记录保存在 `validation/`；技术检查通过不代表美术效果自动通过。

新增风格时先保存来源和改动说明，再按 [数据约定](spec/CONTRACT_FORMAT.md) 提取规则。只有完成 Blender 整理和审校，才能将目录状态由 `reference_only` 改为 `contract_available`。
