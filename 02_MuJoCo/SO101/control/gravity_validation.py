"""SO-101 重力项验证脚本。

开源库：
- MuJoCo Python bindings: https://github.com/google-deepmind/mujoco
- SO-101 模型参考： https://github.com/johnsutor/so101-nexus
- 研究参考：so101-classical-robotics（用于理解参数和动力学代码）

说明：
本文件是学习和验证代码，不是对第三方项目的原始代码复制。
脚本通过 MuJoCo 的逆动力学接口，在固定姿态和零速度、零加速度条件下
读取重力相关广义力，并打印关节名称与结果。
"""

from pathlib import Path

import mujoco
import numpy as np


MODEL_PATH = Path("model/scene_torque.xml")


def main() -> None:
    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            f"找不到模型文件：{MODEL_PATH}。请从 SO-101 模型项目获取 scene_torque.xml。"
        )

    model = mujoco.MjModel.from_xml_path(str(MODEL_PATH))
    data = mujoco.MjData(model)

    # 固定当前姿态，令速度和加速度为零。
    # mj_inverse 在此条件下可用于观察重力等动力学项。
    data.qvel[:] = 0.0
    data.qacc[:] = 0.0
    mujoco.mj_forward(model, data)
    mujoco.mj_inverse(model, data)

    print("SO-101 MuJoCo 重力项检查")
    print(f"nq={model.nq}, nv={model.nv}")
    print("-" * 60)

    for joint_id in range(model.njnt):
        name = mujoco.mj_id2name(
            model, mujoco.mjtObj.mjOBJ_JOINT, joint_id
        )
        dof_id = model.jnt_dofadr[joint_id]
        if name is not None and dof_id < model.nv:
            print(f"{name:20s} dof={dof_id:2d}  qfrc_inverse={data.qfrc_inverse[dof_id]: .8f}")

    print("-" * 60)
    print("说明：结果需要与自己的 RNEA 重力递推结果按关节顺序逐项对照。")


if __name__ == "__main__":
    main()
