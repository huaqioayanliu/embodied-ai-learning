"""SO-101 键盘控制研究版示例。

开源库：
- MuJoCo Python bindings: https://github.com/google-deepmind/mujoco
- SO-101 模型参考： https://github.com/johnsutor/so101-nexus
- 键盘控制逻辑参考：so101-classical-robotics（开源项目）

说明：
这是根据开源项目控制逻辑整理的学习示例，不是原项目文件的直接复制。
它展示“按键 -> 更新目标关节角 -> 位置执行器 -> mj_step”的基本链路。
运行前请确认模型中的执行器名称和关节名称与本机 XML 一致。
"""

import time
from pathlib import Path

import mujoco
import mujoco.viewer


MODEL_PATH = Path("model/scene.xml")
JOINT_NAME = "shoulder_pan"
TARGET_STEP = 0.05


def main() -> None:
    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            f"找不到模型文件：{MODEL_PATH}。请根据本机模型路径修改 MODEL_PATH。"
        )

    model = mujoco.MjModel.from_xml_path(str(MODEL_PATH))
    data = mujoco.MjData(model)
    joint_id = mujoco.mj_name2id(
        model, mujoco.mjtObj.mjOBJ_JOINT, JOINT_NAME
    )
    if joint_id < 0:
        raise ValueError(f"模型中不存在关节：{JOINT_NAME}")

    qpos_id = model.jnt_qposadr[joint_id]
    target = float(data.qpos[qpos_id])

    print("键盘控制研究示例")
    print("a/d：减小或增大目标角度；Esc：退出")

    with mujoco.viewer.launch_passive(model, data) as viewer:
        while viewer.is_running():
            # 终端输入仅用于展示控制链路。
            # 不同终端环境的非阻塞按键读取方式不同，实际项目中应替换这里。
            command = input("输入 a / d / q：").strip().lower()
            if command == "q":
                break
            if command == "a":
                target -= TARGET_STEP
            elif command == "d":
                target += TARGET_STEP
            else:
                print("未识别的输入")
                continue

            target = float(np_clip(target, -3.14, 3.14))
            data.ctrl[0] = target
            mujoco.mj_step(model, data)
            viewer.sync()
            time.sleep(0.02)


def np_clip(value: float, low: float, high: float) -> float:
    """避免额外引入 NumPy，仅用于限制目标角度。"""
    return max(low, min(high, value))


if __name__ == "__main__":
    main()
