#!/usr/bin/env python3
"""Build a portable rule reader and two style-only ZIP deliverables."""
from pathlib import Path
import json
import zipfile
import hashlib

ROOT=Path(__file__).resolve().parent.parent
DIST=ROOT/'dist'
ADDON=ROOT/'blender/lemo_style_guard'
VERSION=(ROOT/'VERSION').read_text(encoding='utf-8').strip()

HTML=r"""<!doctype html>
<html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Lemo 美术风格约束 · Blender</title>
<style>
:root{font-family:system-ui,"Microsoft YaHei",sans-serif;color:#24292f;background:#f6f7f8;line-height:1.65}
*{box-sizing:border-box}body{margin:0}header,main,footer{max-width:1160px;margin:auto;padding:28px}
header{padding-bottom:16px}h1{font-size:30px;line-height:1.2;margin:8px 0 14px}h2{font-size:24px;margin:0 0 12px}
h3{font-size:18px;margin:20px 0 8px}.small{font-size:13px;color:#616974}.eyebrow{font-size:12px;letter-spacing:.12em;color:#656d76}
a{color:#2856a0;text-underline-offset:3px}button,input{font:inherit}button{cursor:pointer;border:1px solid #d6dce2;border-radius:7px;background:white;padding:9px 13px;text-align:left}
button.active{background:#26394a;color:white;border-color:#26394a}.nav{display:flex;gap:8px;flex-wrap:wrap;margin:18px 0}
.sheet{background:white;border:1px solid #dce0e5;border-radius:12px;padding:26px}.grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px}
.rule{border-top:1px solid #e9ecf0;padding:16px 0}.label{font-size:12px;font-weight:650;color:#65717e}.forbidden{color:#a44236}.required{color:#2856a0}
.rule p{margin:7px 0}summary{font-size:13px;color:#596778;cursor:pointer}blockquote{border-left:3px solid #ccd5de;margin:12px 0;padding:0 12px;color:#59636e;font-size:14px}
.palette{display:flex;gap:12px;flex-wrap:wrap}.chip{display:flex;align-items:center;gap:8px;font-size:12px}.color{width:22px;height:22px;border:1px solid #ccd0d5;border-radius:50%}
.note{background:#f3f5f7;padding:14px 18px;border-radius:8px}.sourcegrid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:9px}
.source{border:1px solid #e0e4e9;background:white;padding:12px;border-radius:7px}.source a{font-size:12px;margin-right:10px}
input{width:100%;padding:12px;border:1px solid #cfd7df;border-radius:7px;margin:12px 0 18px}
@media(max-width:760px){header,main,footer{padding:18px}.sheet{padding:18px}.grid,.sourcegrid{grid-template-columns:1fr}h1{font-size:25px}}
</style>
<header><div class="eyebrow">LEMO → BLENDER · STYLE CONSTRAINTS · V@@VERSION@@</div>
<h1>把原作的美术限制，带进自己的工程。</h1>
<p>8套中文Blender约束 · 150条可追溯规则 · 99套原文美术摘录</p>
<p class="small">本入口展示风格规则与转译建议。故事、资产和场景由你的具体项目决定。</p>
<p><a href="dist/lemo_style_guard-v@@VERSION@@.zip">下载 Blender 约束面板</a>　<a href="README.md">使用说明</a>　<a href="docs/SOURCE_NOTICE.md">来源与许可</a></p>
<nav id="nav" class="nav"></nav></header>
<main><section id="profile" class="sheet"></section>
<section style="margin-top:36px"><h2>99套原文风格资料</h2><p class="small">标注“原文参考”的91套尚未做成Blender中文约束。资料数量不代表自动实现数量。</p>
<input id="query" placeholder="按中文名、风格ID或分类搜索" aria-label="搜索原文风格">
<div id="sources" class="sourcegrid"></div></section></main>
<footer class="small">Lemo-Opuscar by Lemomo (LemoLab) · 原文固定提交 00a7f9ec · Blender转译建议单独标记 · 文档与内嵌规则 CC BY-NC 4.0（含上游影片制作额外许可） · <a href="NOTICE.md">署名与改动</a></footer>
<script>
const DATA=@@DATA@@;
const cats={palette:"配色",material:"材质",shape:"轮廓与造型",composition:"构图",lighting:"光影",camera:"摄影机",typography:"文字",consistency:"一致性"};
const levels={required:"必须",forbidden:"禁止",recommended:"建议",optional:"可选",example:"示例"};
function el(tag,text,cls){const n=document.createElement(tag);if(text!==undefined)n.textContent=text;if(cls)n.className=cls;return n}
function link(label,url){const a=el("a",label);a.href=url;return a}
function show(id){
 const p=DATA.profiles.find(x=>x.style_id===id);const box=document.getElementById("profile");box.replaceChildren();
 document.querySelectorAll("#nav button").forEach(b=>b.classList.toggle("active",b.dataset.id===id));
 box.append(el("div",p.style_id,"eyebrow"),el("h2",p.title_zh));
 box.append(el("p",p.scope.blender_route),el("p",p.scope.adaptation_limit,"note small"));
 box.append(link("中文规则卡","blender/lemo_style_guard/profiles/"+id+"/RULES.md"),document.createTextNode("　"),link("原文依据",p.source.repo+"/blob/"+p.source.commit+"/"+p.source.path));
 box.append(el("h3","配色来源"));
 box.append(el("p",p.palette.status==="source_example"?"以下为原文示例，颜色的角色约束仍须保留。":p.palette.status,"small"));
 const colors=el("div",undefined,"palette");
 for(const c of p.palette.colors){const row=el("div",undefined,"chip"),swatch=el("i",undefined,"color");swatch.style.backgroundColor=c.hex;row.append(swatch,el("span",c.name+" "+c.hex));colors.append(row)}
 box.append(colors,el("p",p.palette.colors.length?String(p.palette.notes):"原文没有指定可直接使用的HEX，按文字配色约束自行选色。","small"));
 const groups=el("div",undefined,"grid");
 for(const [cat,label] of Object.entries(cats)){
  const rules=p.rules.filter(r=>r.category===cat);if(!rules.length)continue;
  const group=el("section");group.append(el("h3",label));
  for(const r of rules){const item=el("article",undefined,"rule");item.append(el("div",levels[r.level]+" · "+r.id,"label "+r.level),el("p",r.rule_zh));
   const d=el("details");d.append(el("summary","查看原文与Blender转译"),el("p",r.source_section,"small"),el("blockquote",r.source_quote),el("p","Blender建议："+r.blender_translation,"small"));item.append(d);group.append(item)}
  groups.append(group)}
 box.append(groups);
}
function sourceList(){
 const q=document.getElementById("query").value.toLowerCase().trim(),out=document.getElementById("sources");out.replaceChildren();
 for(const s of DATA.styles){if(q&&![s.style_id,s.title_zh,s.category_zh].join(" ").toLowerCase().includes(q))continue;
 const row=el("article",undefined,"source");row.append(el("strong",s.title_zh),el("div",s.style_id+" · "+s.category_zh,"small"),el("div",s.blender_status==="contract_available"?"Blender中文约束已整理":"原文参考","small"));
 row.append(link("美术摘录",s.art_rules_path),link("原始STYLE",s.source_path),link("GitHub原文",s.source_url));out.append(row)}
}
const nav=document.getElementById("nav");for(const p of DATA.profiles){const b=el("button",p.title_zh);b.dataset.id=p.style_id;b.addEventListener("click",()=>show(p.style_id));nav.append(b)}
document.getElementById("query").addEventListener("input",sourceList);show("spy-titles");sourceList();
</script></html>
"""

def clean_files(folder):
    for path in sorted(folder.rglob('*')):
        if path.is_file() and not any(part in {'.git','__pycache__','dist'} for part in path.relative_to(folder).parts) and path.suffix not in {'.pyc','.log'}:
            yield path

def main():
    DIST.mkdir(exist_ok=True)
    profiles=[json.loads(p.read_text(encoding='utf-8')) for p in sorted((ADDON/'profiles').glob('*/contract.json'))]
    catalog=json.loads((ROOT/'catalog/styles.json').read_text(encoding='utf-8'))
    styles=catalog['styles']
    payload=json.dumps({'profiles':profiles,'styles':styles},ensure_ascii=False).replace('<',r'\u003c')
    (ROOT/'START_HERE.html').write_text(HTML.replace('@@DATA@@',payload).replace('@@VERSION@@',VERSION),encoding='utf-8')
    addon=DIST/f'lemo_style_guard-v{VERSION}.zip'
    addon_readme="""Lemo 美术风格约束 / Blender 4.3
Install from Disk this ZIP and enable Lemo 美术风格约束.
3D View > N sidebar > Lemo 风格.
Choose a style and load its art rules. No scene objects are generated.
The eight rule sets are translated/adapted from the pinned Lemo STYLE documents.
The source quotes, source commit, and palette provenance are recorded per rule.
Colour swatches are references only, never a completed material setup.
The original docs and their adaptations retain CC BY-NC 4.0 and the upstream
additional permission for making your own films, including commercial/client films.
See licenses/LICENSE for the complete original terms.
Source: https://github.com/lemomo-ai/lemo-opuscar
Pinned: 00a7f9ec99c8686265a8ca4ed9a3fdaaf27ea6f4
Original author: Lemomo (LemoLab).
The Blender loader is independently adapted code under MIT, not upstream Blender code.
See LICENSE, NOTICE.md and LICENSES/MIT.txt for this package; source terms remain
in licenses/LICENSE. Rule JSON and translated cards remain CC BY-NC 4.0.
"""
    with zipfile.ZipFile(addon,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
        for p in clean_files(ADDON):z.write(p,'lemo_style_guard/'+p.relative_to(ADDON).as_posix())
        z.writestr('lemo_style_guard/README.txt',addon_readme)
        for p in [ROOT/'LICENSE',ROOT/'NOTICE.md']:
            z.write(p,'lemo_style_guard/'+p.name)
        for p in clean_files(ROOT/'LICENSES'):
            z.write(p,'lemo_style_guard/LICENSES/'+p.name)
        for p in [ROOT/'source/lemo-opuscar/LICENSE', ROOT/'source/lemo-opuscar/REUSE.toml']:
            z.write(p,'lemo_style_guard/licenses/'+p.name)
        for p in clean_files(ROOT/'source/lemo-opuscar/LICENSES'):
            z.write(p,'lemo_style_guard/licenses/LICENSES/'+p.name)
        for p in profiles:
            src=ROOT/'source/lemo-opuscar'/p['source']['path']
            z.write(src,'lemo_style_guard/profiles/'+p['style_id']+'/SOURCE_STYLE.md')
    full=DIST/f'lemo-blender-style-library-v{VERSION}.zip'
    with zipfile.ZipFile(full,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
        for p in clean_files(ROOT):z.write(p,'lemo-blender-style-library/'+p.relative_to(ROOT).as_posix())
        z.write(addon,'lemo-blender-style-library/dist/'+addon.name)
    for p in [addon,full]:
        with zipfile.ZipFile(p) as z:
            assert z.testzip() is None
            assert not any(Path(i.filename).suffix.lower() in {'.blend','.mp4','.mov','.wav','.svg','.png','.jpg'} for i in z.infolist())
    print(json.dumps({'files':[{'path':str(p),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in [full,addon]],
                      'profiles':len(profiles),'rules':sum(len(p['rules']) for p in profiles)},ensure_ascii=False))

if __name__=='__main__':main()

