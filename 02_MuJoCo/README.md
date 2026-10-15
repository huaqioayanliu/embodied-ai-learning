# MuJoCo 机器人仿真记录：SO-101 与 Unitree G1

本目录记录在 Ubuntu 上学习 MuJoCo、加载两种机器人模型，以及让关节产生可见运动的实验。

## 运行环境

- Ubuntu（独立安装的 Linux）
- Conda 环境：`mujoco`
- Python 3.10.22
- MuJoCo 3.15.0
- 可选：NVIDIA 独显 OpenGL 渲染

## 文件

| 路径 | 功能 |
| --- | --- |
| `SO101/load_so101.py` | 加载 SO-101 并推进物理仿真 |
| `SO101/control_so101.py` | 用 position actuator 设置 shoulder_pan 目标位置 |
| `G1/load_g1.py` | 加载 G1 站立姿态，静态显示 |
| `G1/control_g1.py` | 直接调整左肩 `qpos` 并刷新运动学，展示周期摆动 |

## 模型来源

- SO-101: [johnsutor/so101-nexus](https://github.com/johnsutor/so101-nexus)，使用 `src/so101_nexus/assets/SO101_menagerie/scene.xml`。
- G1: [google-deepmind/mujoco_menagerie](https://github.com/google-deepmind/mujoco_menagerie)，使用 `unitree_g1/scene.xml` 及其 `assets`。

第三方模型及其 mesh 不包含在本学习仓库中；请自行获取并遵循原项目许可。

示例默认使用以下本地路径：

```text
~/robotics/so101-nexus/src/so101_nexus/assets/SO101_menagerie/scene.xml
~/robotics/02_robot_models/g1/scene.xml
```

如果文件位置不同，需要调整脚本中的 `MODEL_PATH`。

## 运行方式

在 Ubuntu 终端中：

```bash
conda activate mujoco
python -m pip install mujoco numpy
```

在仓库根目录执行：

```bash
python 02_MuJoCo/SO101/load_so101.py
python 02_MuJoCo/SO101/control_so101.py
python 02_MuJoCo/G1/load_g1.py
python 02_MuJoCo/G1/control_g1.py
```

如果 Ubuntu 混合显卡默认选择了 Intel GPU，可以试：

```bash
__NV_PRIME_RENDER_OFFLOAD=1 __GLX_VENDOR_LIBRARY_NAME=nvidia python 02_MuJoCo/G1/load_g1.py
```

## 理解与记录

- `import mujoco` 让 Python 调用 MuJoCo 引擎，MJCF/XML 描述机器人和场景，Viewer 显示仿真状态。
- `MjModel` 保存模型结构，`MjData` 保存当前仿真状态。
- SO-101 的 `data.ctrl` 是位置执行器的目标输入；`mj_step()` 推进物理计算。
- G1 的示例通过 `jnt_qposadr` 找到关节位置，直接修改 `qpos` 并调用 `mj_forward()`，属于运动学演示，不是 G1 的平衡或行走控制。
- 在独立 Viewer 中使用 Control 滑块进行动力学测试时，未配平衡控制的 G1 可能倾斜或跌倒。


## 学习进度更新

2026年10月15日

- 完成 SO-101 机械臂 MuJoCo 模型加载。
- 实现 SO-101 肩部关节位置控制。
- 完成宇树 G1 人形机器人模型加载。
- 使用 Python 实现 G1 左肩关节周期性运动演示。
- 使用 MuJoCo Viewer 的 Control 面板操作 G1。
- 观察到 G1 在没有平衡控制器时会发生倾斜或摔倒。

下一步：学习机器人位置控制、PD 控制以及正逆运动学。

## 后续

补充运行截图、操作视频以及本机最终版代码；进一步学习 FK、IK、PD 控制与 G1 全身运动控制。
