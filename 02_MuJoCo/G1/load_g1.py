"""Unitree G1: initialize the standing pose and display the robot.

Model: https://github.com/google-deepmind/mujoco_menagerie/tree/main/unitree_g1
This example displays a static pose; it does not advance dynamics.
"""
import time
from pathlib import Path

import mujoco
import mujoco.viewer

MODEL_PATH = Path.home() / "robotics/02_robot_models/g1/scene.xml"

if not MODEL_PATH.is_file():
    raise FileNotFoundError(f"G1 scene not found: {MODEL_PATH}")

model = mujoco.MjModel.from_xml_path(str(MODEL_PATH))
data = mujoco.MjData(model)

stand_id = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_KEY, "stand")
if stand_id >= 0:
    mujoco.mj_resetDataKeyframe(model, data, stand_id)
    print("Loaded G1 'stand' keyframe")
else:
    print("No 'stand' keyframe; using the default state")

mujoco.mj_forward(model, data)
print("Joints:", model.njnt)
print("Actuators:", model.nu)
print("qpos size:", model.nq)

with mujoco.viewer.launch_passive(model, data) as viewer:
    while viewer.is_running():
        viewer.sync()
        time.sleep(0.01)
