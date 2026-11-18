# 本地 AI 入口

这是 Lemo 美术风格约束库 v0.4.0 的公开分发入口。

完整源码位于 lemo-blender-style-library-v0.4.0.zip。若当前目录尚无 tools/ai_context.py 和 catalog/styles.json，先按 README.md 将包解压到独立目录，再读取解压目录中的 AGENTS.md 和 AI_START_HERE.md。不要把这个分发入口误当作完整的风格上下文。

源码包含 99 套原文参考、8 套 Blender 中文合同和 150 条可追溯规则。先选择一个 style_id，使用 tools/ai_context.py 的 list、search、export 命令按需读取。其余 91 套是 reference_only，不要声称已经完成 Blender 适配。

保留原文规则强度、适用条件、来源、许可与改动说明。Blender 转译建议不是上游已提供的原生参数。制作文件放在用户指定项目目录；对照实际画面核验，不能以脚本成功代替美术验收。

文档保留 CC BY-NC 4.0 和对应权利人的影片制作额外许可；工具代码许可单独标明。完整许可证在分发包中。原作者为 Lemo-Opuscar by Lemomo (LemoLab)，https://github.com/lemomo-ai/lemo-opuscar。
