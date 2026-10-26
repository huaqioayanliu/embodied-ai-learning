# 具身智能学习记录

记录自己从 Python 基础、Ubuntu 环境配置到机器人仿真、控制和 ROS 2 的学习过程，逐步整理学习笔记、代码和演示视频。

## 学习方向

目前关注机器人操作，希望逐步掌握运动学、关节控制、ROS 2、遥操作和模仿学习，为后续学习人形机器人上肢与灵巧手操作打下基础。

## 当前进度

截至 2026 年 10 月 26 日：

- [x] 完成 Ubuntu 系统安装和基础开发环境配置。
- [x] 配置 Conda 的 mujoco 环境。
- [x] 在 MuJoCo 中加载 SO-101 与 Unitree G1 模型并观察关节运动。
- [x] 完成 SO-101 单关节位置控制、IK/DLS 验证和力矩 PD 摩擦对照实验。
- [x] 安装 ROS 2 Jazzy，完成 Talker/Listener 发布订阅。
- [x] 运行 Turtlesim 并使用键盘控制移动。
- [ ] 继续学习 ROS 2 Python 节点、工作空间、Service 和 Action。
- [ ] 进一步进行末端轨迹、遥操作和模仿学习实验。

## 主要目录

- [MuJoCo 仿真](02_MuJoCo/README.md)
- [ROS 2 Jazzy 学习记录](03_ROS2/README.md)
- [SO-101 运动学实验](02_MuJoCo/SO101/kinematics/README.md)
- [SO-101 力矩 PD 与摩擦实验](02_MuJoCo/SO101/control/README.md)
- [Ubuntu 安装与排错](docs/01-ubuntu-installation-troubleshooting.md)
- [Ubuntu 与 MuJoCo 环境配置](docs/02-ubuntu-mujoco-setup.md)

## 记录方式

每次实践尽量保留：

1. 本次目标与实际完成的结果。
2. 代码、运行环境和操作步骤。
3. 遇到的问题、解决方法及尚未理解的部分。
4. 截图或演示视频。

参考开源项目的代码和模型时，注明来源，并记录自己的修改。

## 已有演示视频

- [SO-101 关节控制](02_MuJoCo/videos/SO101_control.mp4)
- [Unitree G1 关节控制](02_MuJoCo/videos/G1_control.mp4)
