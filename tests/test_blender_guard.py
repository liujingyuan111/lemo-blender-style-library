"""Meaningful integration check: style loading must not generate or restyle a film."""
from pathlib import Path
import json
import sys
import bpy

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'blender'))
import lemo_style_guard as guard


def fingerprint(scene):
    return {
        'objects':[(o.name,o.type,tuple(o.location),tuple(o.rotation_euler),tuple(o.scale),
                    tuple(slot.material.name if slot.material else None for slot in o.material_slots))
                   for o in scene.objects],
        'camera':scene.camera.name if scene.camera else None,
        'engine':scene.render.engine,'resolution':(scene.render.resolution_x,scene.render.resolution_y),
        'fps':scene.render.fps,'view_transform':scene.view_settings.view_transform,
        'world':scene.world.name if scene.world else None,
    }


guard.register()
scene=bpy.context.scene
before=fingerprint(scene)
material_count=len(bpy.data.materials)
results=[]
profiles=guard.list_profiles()
assert len(profiles)==8
for profile in profiles:
    result=guard.load_style(scene,profile['style_id'])
    assert fingerprint(scene)==before,'Loading a contract mutated the existing scene'
    assert len(bpy.data.materials)==material_count,'Loading a contract created materials'
    assert len(scene.lemo_style.rules)==len(profile['rules'])
    assert all(not r.reviewed for r in scene.lemo_style.rules)
    report=guard.audit_scene(scene)
    assert report['automatic_art_approval'] is False and report['reviewed_by_user']==0
    results.append({'style_id':profile['style_id'],'load_without_scene_mutation':'passed',
                    'manual_checks_start_unreviewed':True,'rules':len(profile['rules'])})

guard.load_style(scene,'spy-titles')
scene.lemo_style.rules[0].reviewed=True
guard.load_style(scene,'spy-titles')
assert scene.lemo_style.rules[0].reviewed,'Same contract reload lost manual record'
mats=guard.make_palette_swatches(scene)
assert mats and fingerprint(scene)==before,'Swatches were assigned or scene was changed'
count=len(bpy.data.materials)
assert [m.name for m in mats]==[m.name for m in guard.make_palette_swatches(scene)]
assert len(bpy.data.materials)==count,'Reference swatches were duplicated'
mats[0].node_tree.nodes['LEMO_REFERENCE_COLOR'].inputs['Color'].default_value=(.2,.3,.4,1)
report=guard.audit_scene(scene)
assert any(c['id']=='reference_colour' and c['status']=='notice' for c in report['technical_checks'])
old_modified_color=tuple(mats[0].node_tree.nodes['LEMO_REFERENCE_COLOR'].inputs['Color'].default_value)
guard.make_palette_swatches(scene)
assert tuple(mats[0].node_tree.nodes['LEMO_REFERENCE_COLOR'].inputs['Color'].default_value)==old_modified_color
assert fingerprint(scene)==before
old_contract=scene['lemo_contract_json']
try:guard.load_style(scene,'../../bad')
except ValueError:pass
else:raise AssertionError('Invalid style path accepted')
assert scene['lemo_contract_json']==old_contract

other=scene.copy()
guard.load_style(other,'silhouette-rhythm')
assert other['lemo_rule_text']!=scene['lemo_rule_text'],'Two scenes shared and overwrote a rule card'
assert scene.lemo_style.rules[0].reviewed
assert all(not r.reviewed for r in other.lemo_style.rules)
bpy.data.scenes.remove(other)

scratch=ROOT.parent/'style_guard_test_work';scratch.mkdir(exist_ok=True)
blend=scratch/'rule_roundtrip.blend'
bpy.ops.wm.save_as_mainfile(filepath=str(blend))
bpy.ops.wm.open_mainfile(filepath=str(blend))
scene=bpy.context.scene
assert scene.lemo_style.loaded_style_id=='spy-titles'
assert scene.lemo_style.rules[0].reviewed,'Saved manual record was lost'
assert scene.get('lemo_rule_text') in bpy.data.texts
assert fingerprint(scene)==before

report={'schema_id':'lemo-blender-guard-validation/v1','status':'passed',
        'blender_version':bpy.app.version_string,'profiles':results,
        'checks':['all eight contracts load without geometry, material, camera or render mutations',
                  'all art checks initially require manual review',
                  'same-version reload preserves human review',
                  'reference swatches do not assign themselves to objects',
                  'unchanged swatches are reused',
                  'changed swatch is detected and never overwritten',
                  'unknown style paths are refused before mutation',
                  'separate scenes keep independent rule cards and human reviews',
                  'save/reopen preserves rules and review state'],
        'visual_style_reproduction_claimed':False,'generated_scene_assets_delivered':False}
(ROOT/'validation/blender_guard_report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'status':'passed','profiles':len(profiles),'blender':bpy.app.version_string}))
