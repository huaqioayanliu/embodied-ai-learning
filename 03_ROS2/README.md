# ROS 2 Jazzy 学习记录

## 已完成内容（2026-10-26）

- 在 Ubuntu 上安装 ROS 2 Jazzy。
- 运行 Talker/Listener 发布与订阅示例。
- 使用 `ros2 node list`、`ros2 topic list` 和 `ros2 topic echo` 查看节点与话题。
- 运行 Turtlesim，并使用键盘控制小乌龟移动。
- 理解 `/turtle1/cmd_vel` 话题和 `geometry_msgs/msg/Twist` 消息。
- 区分键盘方向控制使用的 Topic 与 `gbvcdert` 控制旋转时使用的 Action。

## 基本命令

```bash
ros2 node list
ros2 topic list
ros2 topic echo /turtle1/cmd_vel
ros2 run turtlesim turtlesim_node
ros2 run turtlesim turtle_teleop_key
```

## 学习理解

ROS 2 中，节点负责运行具体功能；Topic 用于连续发布和订阅消息；Action 适合需要反馈和执行过程的任务。当前先使用 Python 学习 ROS 2 节点，C++ 与 Python 并行补充。

## 后续计划

- 学习 Python ROS 2 工作空间和自定义节点。
- 学习 Service、Action 和参数。
- 将 ROS 2 通信与 SO-101 仿真控制逐步结合。
