"""SO-101: demonstration of shoulder_pan position-actuator control.

Model: https://github.com/johnsutor/so101-nexus
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

actuator_id = mujoco.mj_name2id(
    model, mujoco.mjtObj.mjOBJ_ACTUATOR, "shoulder_pan"
)
if actuator_id < 0:
    raise ValueError("SO-101 actuator 'shoulder_pan' not found")

with mujoco.viewer.launch_passive(model, data) as viewer:
    while viewer.is_running():
        # SO-101 uses position actuators: this requests a target of 1 rad.
        data.ctrl[actuator_id] = 1.0
        mujoco.mj_step(model, data)
        viewer.sync()
        time.sleep(0.01)
