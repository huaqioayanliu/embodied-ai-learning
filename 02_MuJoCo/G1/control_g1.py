"""Unitree G1: kinematic demo of left shoulder pitch motion.

The script writes directly to qpos and calls mj_forward().
This is NOT actuator-based dynamic control or a balancing controller.
"""
import time
from pathlib import Path

import mujoco
import mujoco.viewer
import numpy as np

MODEL_PATH = Path.home() / "robotics/02_robot_models/g1/scene.xml"

if not MODEL_PATH.is_file():
    raise FileNotFoundError(f"G1 scene not found: {MODEL_PATH}")

model = mujoco.MjModel.from_xml_path(str(MODEL_PATH))
data = mujoco.MjData(model)

stand_id = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_KEY, "stand")
if stand_id >= 0:
    mujoco.mj_resetDataKeyframe(model, data, stand_id)

joint_name = "left_shoulder_pitch_joint"
joint_id = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_JOINT, joint_name)
if joint_id < 0:
    raise ValueError(f"Joint not found: {joint_name}")

qpos_id = model.jnt_qposadr[joint_id]
initial_angle = float(data.qpos[qpos_id])
print("Joint:", joint_name)
print("Initial angle (rad):", initial_angle)

mujoco.mj_forward(model, data)

with mujoco.viewer.launch_passive(model, data) as viewer:
    start_time = time.monotonic()
    while viewer.is_running():
        t = time.monotonic() - start_time
        target_angle = initial_angle + 0.3 * np.sin(t)

        if model.jnt_limited[joint_id]:
            lower, upper = model.jnt_range[joint_id]
            target_angle = np.clip(target_angle, lower, upper)

        data.qpos[qpos_id] = target_angle
        mujoco.mj_forward(model, data)
        viewer.sync()
        time.sleep(0.01)
