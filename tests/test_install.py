"""Validate the actual install ZIP in an isolated Blender user-scripts directory."""
from pathlib import Path
import os
import json
import bpy

ROOT=Path(__file__).resolve().parents[1]
version=(ROOT/'VERSION').read_text(encoding='utf-8').strip()
archive=ROOT/f'dist/lemo_style_guard-v{version}.zip'
assert 'style_guard_install_test' in os.environ.get('BLENDER_USER_SCRIPTS','')
bpy.ops.preferences.addon_install(filepath=str(archive),overwrite=True)
bpy.ops.preferences.addon_enable(module='lemo_style_guard')
import lemo_style_guard as guard
assert Path(guard.__file__).resolve().is_relative_to(Path(os.environ['BLENDER_USER_SCRIPTS']).resolve())
assert len(guard.list_profiles())==8
scene=bpy.context.scene
count=len(scene.objects)
scene.lemo_style.profile='spy-titles'
assert bpy.ops.lemo.load_style()=={'FINISHED'}
assert len(scene.objects)==count
assert bpy.ops.lemo.audit_style()=={'FINISHED'}
assert scene.lemo_style.last_report in bpy.data.texts
icons={item.identifier for item in bpy.types.UILayout.bl_rna.functions['operator'].parameters['icon'].enum_items}
assert {'TEXT','MATERIAL','CHECKMARK'}<=icons
report={'status':'passed','blender_version':bpy.app.version_string,
        'installed_from_zip':True,'isolated_user_scripts':True,'profiles':8,
        'operators_executed':['lemo.load_style','lemo.audit_style'],
        'panel_icon_identifiers_valid':True,'scene_object_count_unchanged':True,
        'scope':'Actual ZIP installation, enabling and operator calls; no claim of interactive screenshot review.'}
(ROOT/'validation/install_report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report))
