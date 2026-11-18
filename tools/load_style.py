#!/usr/bin/env python3
"""Run with Blender: attach one art contract to the current file."""
from pathlib import Path
import argparse
import sys
import bpy

ROOT=Path(__file__).resolve().parent.parent
sys.path.insert(0,str(ROOT/'blender'))
import lemo_style_guard as guard


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--style',required=True)
    p.add_argument('--output',required=True,help='New .blend path; an existing path is refused')
    p.add_argument('--reference-swatches',action='store_true',help='Create unassigned colour references from source HEX values')
    a=p.parse_args(sys.argv[sys.argv.index('--')+1:] if '--' in sys.argv else [])
    output=Path(a.output).expanduser().resolve()
    if output.suffix.lower()!='.blend' or output.exists():
        raise ValueError('Use a new output .blend path; this helper does not overwrite a file')
    # Resolve the profile before any Blender mutation.
    guard.load_profile(a.style)
    if not hasattr(bpy.types.Scene,'lemo_style'):
        guard.register()
    result=guard.load_style(bpy.context.scene,a.style)
    if a.reference_swatches:guard.make_palette_swatches(bpy.context.scene)
    guard.audit_scene(bpy.context.scene)
    output.parent.mkdir(parents=True,exist_ok=True)
    bpy.ops.wm.save_as_mainfile(filepath=str(output))
    print(result)


if __name__=='__main__':main()
