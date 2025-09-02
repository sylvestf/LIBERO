#!/bin/bash

export PYOPENGL_PLATFORM=egl
export MUJOCO_GL=egl

export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6

python scripts/collect_demonstration.py --bddl-file /home/ps/LIBERO/notebooks/custom_pddl/KITCHEN_DEMO_SCENE_libero_demo_behaviors.bddl --device keyboard
