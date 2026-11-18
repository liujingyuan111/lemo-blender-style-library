"""Lemo art rules inside Blender. No scene, story, motion or demo generator."""
bl_info = {
    'name':'Lemo 美术风格约束', 'author':'lemo-blender-style-library contributors',
    'version':(0,4,0), 'blender':(4,3,0),
    'location':'3D View > Sidebar > Lemo 风格',
    'description':'读取原文美术限制、保留来源、记录逐条人工验收',
    'category':'3D View',
}

import hashlib
import json
import textwrap
import uuid
import bpy
from bpy.app.handlers import persistent
from bpy.props import (BoolProperty, CollectionProperty, EnumProperty,
                       PointerProperty, StringProperty)
from .contracts import (CATEGORIES, LEVELS, load_profile, list_profiles,
                        rule_card, source_url, validate_profile, hex_to_linear_rgba)

_PROFILE_ITEMS = []


def profile_items(_self=None, _context=None):
    global _PROFILE_ITEMS
    if not _PROFILE_ITEMS:
        _PROFILE_ITEMS = [(p['style_id'],p['title_zh'],p['scope']['blender_route'])
                          for p in list_profiles()]
    return _PROFILE_ITEMS


def loaded_contract(scene):
    raw = scene.get('lemo_contract_json')
    if not raw:
        raise ValueError('请先载入一套风格约束')
    return validate_profile(json.loads(raw))


def _owner(scene):
    key = scene.get('lemo_style_owner_id')
    if not key or any(s != scene and s.get('lemo_style_owner_id') == key for s in bpy.data.scenes):
        key = str(uuid.uuid4())
        scene['lemo_style_owner_id'] = key
    return key


def _write_owned_text(scene, property_key, basename, body):
    owner = _owner(scene)
    name = scene.get(property_key, '')
    block = bpy.data.texts.get(name)
    if block is None or block.get('lemo_owner') != owner:
        block = bpy.data.texts.new(basename)
        block['lemo_owner'] = owner
        scene[property_key] = block.name
    block.clear()
    block.write(body)
    block.use_fake_user = True
    return block


def _save_reviews(scene):
    if scene.get('lemo_updating_reviews') or not hasattr(scene,'lemo_style'):
        return
    scene['lemo_reviews_json'] = json.dumps({r.rule_id:r.reviewed
                                            for r in scene.lemo_style.rules})


def _review_changed(self, _context):
    if isinstance(self.id_data, bpy.types.Scene):
        _save_reviews(self.id_data)


def _populate_reviews(scene, data, previous):
    scene['lemo_updating_reviews'] = True
    try:
        state = scene.lemo_style
        state.rules.clear()
        state.loaded_style_id = data['style_id']
        for rule in data['rules']:
            item = state.rules.add()
            item.rule_id = rule['id']
            item.category = rule['category']
            item.level = rule['level']
            item.label = rule['rule_zh']
            item.translation = rule['blender_translation']
            item.reviewed = bool(previous.get(rule['id'], False))
    finally:
        scene['lemo_updating_reviews'] = False
    _save_reviews(scene)


def load_style(scene, style_id):
    """Load a rule card only. Leaves geometry, materials, camera and render settings intact."""
    data, digest = load_profile(style_id)
    previous = {}
    if scene.get('lemo_contract_digest') == digest:
        previous = json.loads(scene.get('lemo_reviews_json','{}'))
    scene['lemo_contract_json'] = json.dumps(data, ensure_ascii=False)
    scene['lemo_contract_digest'] = digest
    _populate_reviews(scene, data, previous)
    scene.lemo_style.profile = style_id
    text = _write_owned_text(scene, 'lemo_rule_text',
                             'LEMO_' + style_id + '_美术约束.md', rule_card(data))
    return {'style_id':style_id,'rules':len(data['rules']),'text':text.name,
            'creates_scene_objects':False,'applies_materials':False}


def _valid_swatch(material, rgba):
    if not material.use_nodes or material.node_tree is None:
        return False
    nodes = material.node_tree.nodes
    emission = nodes.get('LEMO_REFERENCE_COLOR')
    output = nodes.get('LEMO_REFERENCE_OUTPUT')
    if emission is None or output is None or len(nodes) != 2:
        return False
    if emission.bl_idname != 'ShaderNodeEmission' or output.bl_idname != 'ShaderNodeOutputMaterial':
        return False
    links = list(material.node_tree.links)
    linked = len(links)==1 and links[0].from_node==emission and links[0].to_node==output
    return (linked and abs(emission.inputs['Strength'].default_value-1)<1e-6
            and all(abs(a-b)<1e-6 for a,b in zip(emission.inputs['Color'].default_value,rgba)))


def make_palette_swatches(scene):
    """Create colour-reference materials, never assign them to scene objects."""
    data = loaded_contract(scene)
    result = []
    for index, color in enumerate(data['palette'].get('colors', [])):
        rgba = hex_to_linear_rgba(color['hex'])
        signature = data['style_id'] + ':' + str(index) + ':' + color['hex'].upper()
        material = next((m for m in bpy.data.materials
                         if m.get('lemo_swatch_signature') == signature
                         and _valid_swatch(m,rgba)), None)
        if material is None:
            material = bpy.data.materials.new('LEMO色板.' + data['style_id'] + '.' + str(index+1))
            material.use_nodes = True
            material.node_tree.nodes.clear()
            node = material.node_tree.nodes.new('ShaderNodeEmission')
            node.name = 'LEMO_REFERENCE_COLOR'
            node.inputs['Color'].default_value = rgba
            node.inputs['Strength'].default_value = 1
            output = material.node_tree.nodes.new('ShaderNodeOutputMaterial')
            output.name = 'LEMO_REFERENCE_OUTPUT'
            material.node_tree.links.new(node.outputs['Emission'],output.inputs['Surface'])
            material.diffuse_color = rgba
            material['lemo_swatch_signature'] = signature
            material['lemo_style_id'] = data['style_id']
            material['lemo_hex_srgb'] = color['hex'].upper()
            material['lemo_color_role'] = str(color.get('role',''))
            material['lemo_palette_origin'] = data['palette']['status']
            material['lemo_use'] = 'Colour reference only; not a finished surface shader'
            material.use_fake_user = True
        result.append(material)
    return result


def audit_scene(scene, write_text=True):
    """Audit provenance/swatches and collect human reviews; never claim automatic art approval."""
    data = loaded_contract(scene)
    checks = []
    try:
        _current, digest = load_profile(data['style_id'])
        checks.append({'id':'profile_version','status':'pass' if digest==scene.get('lemo_contract_digest') else 'notice',
                       'meaning':'载入的规则与当前安装版本一致；旧版本仍保存在工程里'})
    except ValueError:
        checks.append({'id':'profile_version','status':'notice','meaning':'使用工程内保存的旧风格约束'})
    for mat in bpy.data.materials:
        if mat.get('lemo_style_id') != data['style_id'] or not mat.get('lemo_swatch_signature'):
            continue
        expected = hex_to_linear_rgba(mat['lemo_hex_srgb'])
        checks.append({'id':'reference_colour','material':mat.name,
                       'status':'pass' if _valid_swatch(mat,expected) else 'notice',
                       'meaning':'仅核对参考色材质是否被修改；不代表场景配色通过'})
    reviewed = json.loads(scene.get('lemo_reviews_json','{}'))
    items = [{'id':r['id'],'level':r['level'],'rule':r['rule_zh'],
              'review':'user_marked_reviewed' if reviewed.get(r['id']) else 'needs_manual_review'}
             for r in data['rules']]
    report = {'schema_id':'lemo-style-review/v1','style_id':data['style_id'],
              'source':source_url(data),'blender_version':bpy.app.version_string,
              'automatic_art_approval':False,
              'reviewed_by_user':sum(bool(reviewed.get(r['id'])) for r in data['rules']),
              'rule_count':len(items),'technical_checks':checks,'art_rules':items,
              'scope':'技术检查只核对规范版本与参考色材质。构图、光影、轮廓和风格一致性须看实际画面逐条判断。'}
    if write_text:
        block = _write_owned_text(scene,'lemo_report_text','LEMO_风格核对.json',
                                  json.dumps(report,ensure_ascii=False,indent=2))
        scene.lemo_style.last_report = block.name
    return report


@persistent
def _restore_after_load(_dummy):
    for scene in bpy.data.scenes:
        if not scene.get('lemo_contract_json') or not hasattr(scene,'lemo_style'):
            continue
        try:
            data = loaded_contract(scene)
            reviews = json.loads(scene.get('lemo_reviews_json','{}'))
            _populate_reviews(scene,data,reviews)
            if any(item[0]==data['style_id'] for item in profile_items()):
                scene.lemo_style.profile = data['style_id']
        except (ValueError,KeyError,TypeError):
            continue


def _restore_when_ready():
    # Blender restricts bpy.data while enabling an add-on from Preferences.
    if not hasattr(bpy.types.Scene,'lemo_style'):
        return None
    if not hasattr(bpy.data,'scenes'):
        return .05
    _restore_after_load(None)
    return None


class LEMO_PG_Rule(bpy.types.PropertyGroup):
    rule_id: StringProperty()
    category: StringProperty()
    level: StringProperty()
    label: StringProperty()
    translation: StringProperty()
    reviewed: BoolProperty(name='已人工核对画面',default=False,update=_review_changed,
                           description='看过实际画面后登记；软件不会自动判断这条美术规则是否通过')


class LEMO_PG_State(bpy.types.PropertyGroup):
    profile: EnumProperty(name='原始风格',items=profile_items)
    loaded_style_id: StringProperty()
    rules: CollectionProperty(type=LEMO_PG_Rule)
    category: EnumProperty(name='规则类别',items=[('all','全部','')]+[(k,v,'') for k,v in CATEGORIES.items()])
    show_translation: BoolProperty(name='显示Blender转译建议',default=True)
    last_report: StringProperty()


class LEMO_OT_Load(bpy.types.Operator):
    bl_idname='lemo.load_style'
    bl_label='载入美术风格约束'
    bl_description='将本套原文限制和中文规则卡保存到当前工程'
    bl_options={'REGISTER','UNDO'}
    def execute(self,context):
        try:
            result=load_style(context.scene,context.scene.lemo_style.profile)
        except (ValueError,KeyError) as exc:
            self.report({'ERROR'},str(exc));return {'CANCELLED'}
        self.report({'INFO'},'已载入 '+str(result['rules'])+' 条美术规则')
        return {'FINISHED'}


class LEMO_OT_Swatches(bpy.types.Operator):
    bl_idname='lemo.make_swatches'
    bl_label='创建原文参考色板'
    bl_description='只创建取色用材质，不分配到物体；原文未给HEX时不自行补色'
    bl_options={'REGISTER','UNDO'}
    def execute(self,context):
        try:
            mats=make_palette_swatches(context.scene)
        except (ValueError,KeyError) as exc:
            self.report({'ERROR'},str(exc));return {'CANCELLED'}
        self.report({'INFO'},('已建立 '+str(len(mats))+' 个取色参考') if mats else '原文没有可直接使用的HEX色值，请依文字规则选色')
        return {'FINISHED'}


class LEMO_OT_Audit(bpy.types.Operator):
    bl_idname='lemo.audit_style'
    bl_label='生成风格核对记录'
    bl_description='保存技术检查与逐条人工核对状态，不自动评判美术质量'
    def execute(self,context):
        try:
            report=audit_scene(context.scene)
        except (ValueError,KeyError) as exc:
            self.report({'ERROR'},str(exc));return {'CANCELLED'}
        self.report({'INFO'},'已人工核对 '+str(report['reviewed_by_user'])+'/'+str(report['rule_count'])+' 条')
        return {'FINISHED'}


def _lines(layout,text,width=27):
    for line in textwrap.wrap(text,width=width,break_long_words=True,break_on_hyphens=False) or ['']:
        layout.label(text=line)


class LEMO_PT_Style(bpy.types.Panel):
    bl_label='Lemo 美术风格约束'
    bl_idname='LEMO_PT_style'
    bl_space_type='VIEW_3D'
    bl_region_type='UI'
    bl_category='Lemo 风格'
    def draw(self,context):
        layout=self.layout;scene=context.scene;state=scene.lemo_style
        layout.prop(state,'profile')
        layout.operator('lemo.load_style',icon='TEXT')
        if not scene.get('lemo_contract_json'):
            _lines(layout,'选择一套原始风格，将它的美术限制带入当前工程。')
            return
        data=loaded_contract(scene)
        layout.label(text='当前规约：'+data['title_zh'])
        _lines(layout,'规则卡保存在文本编辑器：'+scene.get('lemo_rule_text',''))
        box=layout.box()
        palette_label={'source_fixed':'原文固定色值','source_example':'原文示例配色，可按规则变化','adapter_starting_point':'适配建议色板'}[data['palette']['status']]
        _lines(box,palette_label)
        if data['palette'].get('colors'):
            box.operator('lemo.make_swatches',icon='MATERIAL')
        else:
            _lines(box,'原文没有指定HEX，按配色文字约束选色。')
        layout.prop(state,'category')
        layout.prop(state,'show_translation')
        for item in state.rules:
            if state.category!='all' and item.category!=state.category:
                continue
            box=layout.box()
            box.label(text=CATEGORIES[item.category]+' · '+LEVELS[item.level])
            _lines(box,item.label)
            if state.show_translation:
                _lines(box,'Blender建议：'+item.translation)
            box.prop(item,'reviewed')
        layout.operator('lemo.audit_style',icon='CHECKMARK')
        if state.last_report:
            _lines(layout,'核对记录：'+state.last_report)


_CLASSES=(LEMO_PG_Rule,LEMO_PG_State,LEMO_OT_Load,LEMO_OT_Swatches,LEMO_OT_Audit,LEMO_PT_Style)


def register():
    profile_items()
    for cls in _CLASSES:bpy.utils.register_class(cls)
    bpy.types.Scene.lemo_style=PointerProperty(type=LEMO_PG_State)
    if _restore_after_load not in bpy.app.handlers.load_post:
        bpy.app.handlers.load_post.append(_restore_after_load)
    if hasattr(bpy.data,'scenes'):
        _restore_after_load(None)
    elif not bpy.app.timers.is_registered(_restore_when_ready):
        bpy.app.timers.register(_restore_when_ready,first_interval=.05)


def unregister():
    if bpy.app.timers.is_registered(_restore_when_ready):
        bpy.app.timers.unregister(_restore_when_ready)
    if _restore_after_load in bpy.app.handlers.load_post:
        bpy.app.handlers.load_post.remove(_restore_after_load)
    if hasattr(bpy.types.Scene,'lemo_style'):del bpy.types.Scene.lemo_style
    for cls in reversed(_CLASSES):bpy.utils.unregister_class(cls)


if __name__=='__main__':register()
