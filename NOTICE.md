# 归属、许可与修改说明

本项目是供 Blender 及本地 AI 读取的风格资料整理和工具集。美术原始资料来自 **[Lemo-Opuscar by Lemomo (LemoLab)](https://github.com/lemomo-ai/lemo-opuscar)**；中文整理、规则合同和读取工具由 `lemo-blender-style-library contributors` 提供。本项目不代表上游作者，也不表示获得上游官方背书。

## 原作版本与作者

固定源提交：[`00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4`](https://github.com/lemomo-ai/lemo-opuscar/tree/00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4)。

- Lemo-Opuscar：Copyright (c) 2026 Lemomo (LemoLab)。
- **Memphis Diorama by EianLu, in Lemo-Opuscar by Lemomo (LemoLab)**：Copyright (c) 2026 EianLu；Copyright (c) 2026 Lemomo (LemoLab)。
- **Crayon World 3D by 2nd1st, in Lemo-Opuscar by Lemomo (LemoLab)**：Copyright (c) 2026 2nd1st；Copyright (c) 2026 Lemomo (LemoLab)。
- 本库新增代码、文档和改编贡献：Copyright (c) 2026 lemo-blender-style-library contributors。

## 各部分如何使用

| 内容 | 许可与说明 |
|---|---|
| 99 份原始 `STYLE.md` | [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)，另保留上游额外影片制作许可 |
| 99 份原始 `style.json` | 上游 MIT；版权归属与原始许可保持不变 |
| `art_rules/` 摘录、中文 `RULES.md` 和 `contract.json`、其他新增文档及内嵌规则文本 | CC BY-NC 4.0；本库自有新增部分另有同等用途的影片制作许可 |
| 本库新写的 Python 工具、Blender 加载器、测试及阅读器实现 | MIT；其中包含或导出的文档规则仍适用文档许可 |

完整路径范围见根 [LICENSE](LICENSE)。[CC BY-NC 4.0 全文](LICENSES/CC-BY-NC-4.0.txt)和[新增工具代码 MIT 全文](LICENSES/MIT.txt)随库提供。原始 [LICENSE](source/lemo-opuscar/LICENSE)、[REUSE.toml](source/lemo-opuscar/REUSE.toml)及全部原始许可全文保存在 `source/lemo-opuscar/`。

**文档及改编可按 CC BY-NC 4.0 的条件公开进行非商业分享。** 分享时保留作者、来源、许可、适用免责声明和修改说明。使用资料来制作自有影片、商业影片、客户影片，以及随对应影片工程交付资料，另有影片制作许可；详见[上游原始授权](source/lemo-opuscar/LICENSE)和[本库对自有新增部分的授权](LICENSES/ADDITIONAL-FILM-PERMISSION.txt)。这两类许可分别适用，额外影片许可不撤回 CC BY-NC 已允许的公开非商业分发。

## 修改记录与内容边界

- `source/lemo-opuscar/` 中保留的 213 个文件逐字节不变：99 份 `STYLE.md`、99 份 `style.json`、根 `LICENSE`、`REUSE.toml` 和 13 份许可文本。来源提交和逐文件哈希记录在 [`source/ORIGIN.json`](source/ORIGIN.json)。
- `art_rules/` 选取原作美术相关章节，保持被选章节原文，并增加来源与选择说明。
- 8 套 Blender 合同包含 150 条规则，增加中文整理、规则强度、原文短引、章节指向和单独标明的 Blender 实施建议。这些是改编与转译；上游没有实现本库的 Blender 加载器。
- 工具增加按风格查询、上下文导出、来源校验和 Blender 面板读取功能。导出或打包不会改变资料许可。
- 本库未打包上游影片、演示代码、字体、媒体、模型、纹理、音乐、旁白或第三方角色素材。原文中的链接和名称用于保留来源上下文，不表示相关素材已被授权或包含。

复制单个风格、生成 AI 上下文或重新打包时，应让使用者仍能取得相应作者、源提交、源文档路径、许可与修改说明。使用两套外部贡献风格时，还应保留上列 EianLu 或 2nd1st 的署名。
