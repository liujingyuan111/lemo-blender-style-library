# Blender风格约束数据约定

本仓库提取 Lemo 美术风格约束，为 Blender 制作提供来源明确的规则和实施建议。

每个 `blender/lemo_style_guard/profiles/<slug>/contract.json` 采用如下字段：

- `schema_id`: `lemo-blender-style/v1`
- `style_id`, `title_zh`, `title_original`
- `source`: `{repo,commit,path,sha256}`，固定 `00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4`
- `attribution`: 原作者、版权、固定来源 URL、CC BY-NC 4.0、影片额外许可及改动说明；合同 JSON 属于文档改编内容。
- `scope`: `{original_engine,blender_route,adaptation_limit}`，明确二维/三维转译范围。
- `rules`: `[{id,category,level,rule_zh,source_section,source_quote,blender_translation,review}]`
  - `category`: `palette|material|shape|composition|lighting|camera|typography|consistency`
  - `level`: `required|forbidden|recommended|optional|example`
  - `source_quote`: 原文中一条可核对的短句，必须是连续原文字串，勿加省略号改写。每条建议20词以内。
  - `blender_translation`: 如何在Blender实现/检查的建议，明确是转译，不伪称上游Blender参数。
  - `review`: 固定 `manual`；未检查的美术规则不能自动通过。
- `palette`: `{status,editable,colors:[{name,hex,role}],notes}`
  - `status`: `source_fixed|source_example|adapter_starting_point`；原文示例配色不能改称唯一允许配色。
  - 原文无HEX就不可伪造为原文值。可留colors空数组。
- `material_recipe`: `{family,color_management_suggestion,explanation,origin}`
  - `family`: `flat_ink|matte_paper|translucent_cutout|matte_white|lowpoly_matte|environment_reference`
  - `color_management_suggestion`: `Standard|AgX|none`
  - `origin`: `blender_adapter_suggestion`。只建立参考材质，不能宣称完整复刻原风格。
- `not_automated`: 字符串数组，指出仍需人工构图/光影/轮廓判断的事项。

同目录 `RULES.md`：中文风格卡（硬规则、允许变化、禁用项、Blender做法、适配边界、固定源链接）。不混入新故事/演示分镜。所有数字必须能追溯到原文，Blender推导值标为建议。每个风格约12–20条规则，以原文实际丰富程度为准；审美约束优先，音乐/故事/演示剧情不提取。
