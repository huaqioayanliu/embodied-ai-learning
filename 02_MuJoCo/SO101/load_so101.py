"""SO-101: load the MuJoCo scene and display the robot.

Model: https://github.com/johnsutor/so101-nexus
Run with a Python environment containing mujoco.
"""
import time
from pathlib import Path

import mujoco
import mujoco.viewer

MODEL_PATH = Path.home() / "robotics/so101-nexus/src/so101_nexus/assets/SO101_menagerie/scene.xml"

if not MODEL_PATH.is_file():
    raise FileNotFoundError(f"SO-101 scene not found: {MODEL_PATH}")

model = mujoco.MjModel.from_xml_path(str(MODEL_PATH))
data = mujoco.MjData(model)

with mujoco.viewer.launch_passive(model, data) as viewer:
    while viewer.is_running():
        mujoco.mj_step(model, data)
        viewer.sync()
        time.sleep(0.005)
