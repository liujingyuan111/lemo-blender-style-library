# 风格资料来源、改编与使用范围

## 原作者与固定版本

**[Lemo-Opuscar by Lemomo (LemoLab)](https://github.com/lemomo-ai/lemo-opuscar)**。

本库固定于提交 [`00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4`](https://github.com/lemomo-ai/lemo-opuscar/tree/00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4)。99 套风格的原文 `STYLE.md` 与 `style.json` 保存在 `source/lemo-opuscar/styles/`。逐文件 Git blob、SHA-256 和字节数见 [`source/ORIGIN.json`](../source/ORIGIN.json) 与 [`validation/source_report.json`](../validation/source_report.json)。

两套外部贡献风格保留额外署名：

- **Memphis Diorama by EianLu, in Lemo-Opuscar by Lemomo (LemoLab)**。
- **Crayon World 3D by 2nd1st, in Lemo-Opuscar by Lemomo (LemoLab)**。

上游版权为 Copyright (c) 2026 Lemomo (LemoLab)；两套外部贡献分别另保留 Copyright (c) 2026 EianLu 和 Copyright (c) 2026 2nd1st。本库新增贡献为 Copyright (c) 2026 lemo-blender-style-library contributors。

## 参考层与修改范围

`source/lemo-opuscar/` 保存 99 份原始 `STYLE.md`、99 份原始 `style.json`，以及上游根 `LICENSE`、`REUSE.toml` 和 13 份 `LICENSES/` 许可全文，共 213 个文件。原始文件逐字节保持不变。

本库未引入上游 `DEMO.md`、演示代码、字体、媒体、模型、纹理、音乐、旁白或第三方角色素材。保留许可全文不表示相应第三方素材也已收入。原始文档可能链接上游演示或引擎文件；需要这些上下文时，使用目录中的固定提交链接。

原始 `style.json` 可能含上游演示片名和简介。这些内容作为原始元数据保留，不会成为新项目的故事要求，也不进入 Blender 约束加载器。

`art_rules/` 从原文中选取视觉身份、材料与渲染、颜色、字体、构图与摄影机、视觉缺陷及一致性相关章节。标准风格通常选第 1、2、3、4、6、9 章；非标准风格按实际标题选择。所选章节保持原文，另增加来源说明；章节范围和逐章节哈希在提取报告中记录。

部分被选章节也包含字幕、技术流程或声音提醒，它们保留为原文上下文。提取本身不会将建议改写为强制规则，也不会自动提供相应 Blender 实现。

`blender/lemo_style_guard/profiles/` 保存单独审校的中文合同：8 套、150 条规则。合同区分原文约束、规则强度、适用条件、原文短引和 Blender 转译建议。本库的中文整理、规则组织与实施建议属于新增或改编内容；它们不代表上游作者亲自给出的 Blender 参数。

99 套原文条目中，其余 91 套目前为 `reference_only`。原文数量不代表已经完成相同数量的 Blender 材质、场景或自动复刻。

## 许可对应关系

根 [LICENSE](../LICENSE) 给出完整范围；[NOTICE.md](../NOTICE.md) 汇总归属和修改说明。上游依据为固定版本的[原始许可](../source/lemo-opuscar/LICENSE)和[逐文件许可映射](../source/lemo-opuscar/REUSE.toml)。

| 内容 | 许可 |
|---|---|
| 原始 `STYLE.md`、美术章节摘录、翻译、中文合同与改编规则 | [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)，并保留对应权利人的额外影片制作许可 |
| 上游 `style.json` 元数据 | MIT，版权与例外依据上游原始文件 |
| 本库新增文档及 Blender 转译建议 | CC BY-NC 4.0；本库贡献者对自有部分另授予影片制作许可 |
| 本库新写的 Python 工具、Blender 面板和阅读器实现 | [MIT](../LICENSES/MIT.txt)；嵌入或导出的规则文本继续适用文档许可 |

`contract.json` 包含文档翻译与改编，文件扩展名不会改变这些内容的许可。HTML 阅读器、AI 上下文和 ZIP 包中的规则文本也保留文档许可。

### 公开非商业分享

CC BY-NC 4.0 允许按其条件复制、改编和公开非商业分享文档。因此，公开提供原作风格资料与中文整理，可以使用这项许可。分享时保留作者、源链接、许可链接、适用版权与免责声明，并注明摘录、翻译或改编。

本库的[CC BY-NC 4.0 全文](../LICENSES/CC-BY-NC-4.0.txt)与上游副本相同。条款的正式说明见 [Creative Commons 法律文本](https://creativecommons.org/licenses/by-nc/4.0/legalcode.en)。

### 制作影片的额外许可

上游 `LICENSE` 的 **ADDITIONAL PERMISSION FOR THE DOCS** 另行允许本人及共同制作相应影片的员工、承包方、客户，为自有影片、商业影片和客户影片阅读、遵循、复制与改编文档，并在对应影片工程交付中包含原文或改编。上游还说明，使用该库制作的影片归制作人，成片无需因使用该库而署名；影片所用第三方素材仍按各自条款处理。

这项额外许可针对影片制作和对应工程交付。文档的其他公开非商业传播继续适用 CC BY-NC 4.0；额外许可没有撤回该权利。超出额外影片许可的商业文档用途，按上游 **COMMERCIAL USE OF THE DOCS** 条款处理。

本库贡献者对新增文档、中文整理与实施建议中自己拥有的权利，也授予[同等影片用途的额外许可](../LICENSES/ADDITIONAL-FILM-PERMISSION.txt)。这项新增授权不扩大上游或其他第三方的权利许可；混合内容分别适用各权利人的授权。

## 可重复提取

参考层可不联网重新生成章节摘录与目录：

```bash
python tools/extract_style_sources.py
```

工具先校验原始文件的 SHA-256 与 Git blob；源资料被改动时会报错。提取只处理文本资料，不执行上游代码、不获取媒体。来源校验和合同读取测试反映文件与运行状态；画面中的美术效果需要在具体项目中另行核对。
