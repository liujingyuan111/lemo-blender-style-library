# 让本地 AI 使用这套风格约束

这份指南适用于能读取本地文件的 GPT／Codex、Claude，以及其他模型或代理工具。把仓库放进它能访问的工作目录，并明确让它先读 AGENTS.md。读取权限和文件工具由你的客户端配置；仅给出仓库名，不代表模型已经读取了文件。

**使用风格资料不要求安装 Blender 面板。** 面板用于在 Blender 工程里阅读规则和记录核对结果；AI 可以直接读取 Markdown／JSON，或使用下面的单风格上下文导出。

## 第一步：选择读取方式

| 使用环境 | 做法 |
|---|---|
| AI能访问本地目录 | 在客户端中授权仓库目录，要求先读AGENTS.md，再按style_id读取对应文件 |
| AI能运行本地命令 | 使用tools/ai_context.py查询与导出；所有命令从仓库根目录执行 |
| AI只能接收文本或附件 | 将导出的单风格Markdown或JSON提供给它；是否支持附件取决于客户端 |
| 在Blender中手动制作 | 阅读RULES.md，或安装可选面板；按实际画面逐条核验 |

该仓库提供资料和读取入口，不包含模型服务、账户登录或模型训练流程。

## 第二步：找一个风格

先用目录或搜索结果选定一套风格，再载入这套风格的规则与来源。目录查询只帮助选择，不需要把99套原文一次全部放进模型上下文。

列出全部99套原文风格，或仅列出8套已有Blender中文约束的风格：

~~~bash
python tools/ai_context.py list
python tools/ai_context.py list --blender-only
python tools/ai_context.py list --json
~~~

按名称或关键词搜索：

~~~bash
python tools/ai_context.py search "剪影"
python tools/ai_context.py search paper --json
~~~

目录的两种状态有不同含义：

| 状态 | 当前提供的内容 |
|---|---|
| contract_available | 已有RULES.md与contract.json，包含中文约束、原文依据和Blender转译建议 |
| reference_only | 有原始STYLE和美术章节摘录；尚未整理为Blender中文合同 |

首批8套是 spy-titles、silhouette-rhythm、shadow-puppet、paper-lantern、paper-popup、backrooms、white-model 和 lowpoly-island。它们合计150条规则。其余91套可用于研究和后续适配。

## 第三步：导出单风格上下文

默认向终端输出，便于交给能运行本地命令的AI读取：

~~~bash
python tools/ai_context.py export spy-titles
python tools/ai_context.py export spy-titles --format json
~~~

保存为文件供聊天客户端或项目使用：

~~~bash
python tools/ai_context.py export spy-titles --format md --output style-context.md
~~~

输出文件已存在时，命令会拒绝覆盖。换一个新文件名，或在确认旧文件用途后自行处理。也可把输出放到自己的项目工作目录；目标父目录必须已存在，命令不会自动创建目录。

导出只选取指定风格，包含来源、许可、修改说明和完成状态。对于8套已有合同的风格，还包含规则等级、原文短引、Blender建议、配色来源和人工验收要求。对于reference_only风格，导出保留其原文参考状态，不补造已完成的Blender合同。

## 可直接复制给 AI 的指令

下面这段可用于有本地文件访问能力的工具。将主题、工程目录和style_id改成自己的内容：

~~~text
请使用这个仓库的美术风格约束完成我的Blender项目。

先读取仓库根目录的AGENTS.md，然后读取catalog/styles.json。
本次style_id是spy-titles。读取该风格的RULES.md、contract.json、
原文章节和来源说明；也可以运行tools/ai_context.py导出同一风格上下文。

我的主题：在这里填写主题。
我的项目目录：在这里填写已授权的工作目录。

先把适用的必须项、禁止项、建议和可选项列成项目检查表，
保留各条规则的ID及适用条件，并写明准备如何在Blender里落实。
原文规则与实施建议分别标注，示例色板不要当成唯一合法色值。

根据我的主题设计新的内容。需要改变或融合风格时，明确记录变化
和冲突处理，不改写源参考文件。

完成后对照实际渲染画面逐条核对，提供具体帧或图像依据。
没有渲染或无法查看画面的条目标为未核验，不能用脚本运行成功
代替美术验收。读取完成后先说明本次选中的风格、来源版本和适配状态。
~~~

如果AI只能接收文本或附件，先提供导出的style-context.md，再要求它按其中的规则等级、来源与验收要求工作。项目文件访问和Blender执行能力仍由当前工具环境决定。

## 项目检查表应包含什么

检查表属于你的项目，可放在项目目录中。建议至少记录以下字段：

| 字段 | 用途 |
|---|---|
| rule_id | 回查本次使用的具体规则 |
| level | 保留required／forbidden／recommended／optional／example的区别 |
| applicable_when | 这条规则在什么内容或图层存在时适用 |
| implementation | 本项目采用的Blender实现决定 |
| evidence | 对应的渲染帧、截图或可复核观察 |
| status | 待实现、待核验、已核验、需要修改或不适用，并说明理由 |

构图、剪影可读性、材质观感、灯光关系和跨镜头一致性需要看实际画面。技术校验与艺术审阅分别记录。

## 规则读取顺序

1. [AGENTS.md](AGENTS.md)：仓库内使用与维护约定。
2. [catalog/styles.json](catalog/styles.json)：选择style_id，确认是否已有Blender合同。
3. 所选风格的RULES.md和contract.json：读取规则及其强度。
4. 对应的art_rules摘录、原始STYLE和来源链接：核对上下文、条件与术语。
5. [docs/SOURCE_NOTICE.md](docs/SOURCE_NOTICE.md)与根许可证说明：保留出处和使用条件。
6. 在自己的项目里建立检查表，再进入制作和画面核验。

## 许可与归属

原始风格文档、艺术章节摘录和中文合同保留对应的文档许可与修改说明。合同采用JSON格式，不会因此变成MIT工具代码。

上游的额外影片制作许可包含自有影片、商业影片和客户影片的相应制作与项目交付用途；资料的公开分享与进一步使用仍按其适用条款处理。不要把“保留非商业资料许可”误写成“禁止制作商业影片”，也不要把影片许可扩大为整套资料可无条件商业再分发。具体边界以根许可证说明、原始LICENSE和SOURCE_NOTICE为准。

