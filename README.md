# Lemo 美术风格约束库 · Blender / 本地 AI

将 **Lemo-Opuscar 原作的美术风格限制**带入 Blender：配色、材质、轮廓、构图、光影、摄影机、文字和跨镜头一致性。

**v0.4.0：99 套原始风格资料与美术章节摘录，8 套 Blender 中文约束，共 150 条可追溯规则。**

本仓库当前提供完整源码分发包。全部 Markdown、JSON、源资料、工具和验证记录都在源码包内，解压后可供本地 AI 直接读取；不需要联网、API Key 或先安装 Blender。

## 下载

- [完整源码包：lemo-blender-style-library-v0.4.0.zip](lemo-blender-style-library-v0.4.0.zip)
- [Blender 面板：lemo_style_guard-v0.4.0.zip](lemo_style_guard-v0.4.0.zip)

在 GitHub 打开 ZIP 文件后选择下载。完整包包含五个 AI 入口、单风格检索与导出工具、离线阅读器及独立插件安装包。

## 给本地 GPT、Codex、Claude 等 AI 使用

安装 Python 3.10 或更新版本，从终端执行：

```bash
git clone https://github.com/liujingyuan111/lemo-blender-style-library.git
cd lemo-blender-style-library
python -m zipfile -e lemo-blender-style-library-v0.4.0.zip .
cd lemo-blender-style-library
python tools/ai_context.py list --blender-only
python tools/ai_context.py search "剪影"
python tools/ai_context.py export spy-titles --format md --output spy-titles-context.md
```

源码包有一个同名顶层目录，因此解压后第二次进入 `lemo-blender-style-library`。在已有目录中解压前请先确认其中没有要保留的同名文件。

然后把解压后的目录交给能读取本地文件的 AI，明确告诉它：

> 先读取 AGENTS.md 和 AI_START_HERE.md。本次采用 spy-titles 风格，按需读取这一套 RULES.md、contract.json 和原文依据。保留必须与禁止项的适用条件；示例和建议不要升级成硬性规定。先建立 Blender 实施检查表，再按我的主题制作，最后对照实际渲染逐条核对。原文要求与 Blender 实施建议分开说明。

把风格 ID 换成自己的选择。只能接收附件的 AI 客户端，可以直接读取导出的单风格 Markdown 或 JSON。不同客户端是否自动发现 AGENTS.md 取决于它的配置。

## 已有 Blender 约束的 8 套风格

| ID | 风格 |
|---|---|
| spy-titles | 60s 间谍片头 |
| silhouette-rhythm | 剪影律动 |
| shadow-puppet | 皮影戏 |
| paper-lantern | 纸雕灯影 |
| paper-popup | 纸片立体书 |
| backrooms | 后室录像带 |
| white-model | 白模投影 |
| lowpoly-island | 低多边形等距 |

其余 91 套明确标为 `reference_only`，尚未完成 Blender 中文约束整理。规则加载器用于阅读规范和记录人工核验，不会自动完成材质、光照、构图或美术复刻。

## Blender 安装

在 Blender 4.3 或更新版本中，从 `Edit → Preferences → Add-ons → Install from Disk` 安装 `lemo_style_guard-v0.4.0.zip`，启用 **Lemo 美术风格约束**。在 3D 视图按 N，打开 **Lemo 风格**。

实际验证版本为 Blender 4.3.2：8 套约束加载、工程状态保持、核验记录保存重开与 ZIP 安装检查通过。10 组 AI 上下文测试覆盖全部 99 套风格。详细记录和测试代码在完整源码包的 `validation/` 与 `tests/` 中；技术通过不代表美术自动验收。

## 归属与许可

原作者：**[Lemo-Opuscar by Lemomo (LemoLab)](https://github.com/lemomo-ai/lemo-opuscar)**。上游固定提交：`00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4`。

- 原始风格文档、摘录、中文规则和合同 JSON：**[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)**，保留上游额外的影片制作许可。
- 上游配置 `style.json`：上游 MIT。
- 本库新增的 Blender 加载器、检索导出和验证代码：MIT。

文档可按非商业条款公开分享。上游额外许可另允许制作自有或客户影片（包括商业影片）及相应项目交付；具体范围见[固定版本的上游 LICENSE](https://github.com/lemomo-ai/lemo-opuscar/blob/00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4/LICENSE)。本库自有新增文档部分也提供同等影片用途的附加许可。完整范围、免责声明和许可全文保存在两个分发包中。

原文文件保持不变；章节摘录只选取原文；中文规则为翻译和整理；Blender 建议与工具是本库新增内容。外部贡献署名：**Memphis Diorama — EianLu**；**Crayon World 3D — 2nd1st**。本库是独立适配，不代表上游官方维护或认可。
