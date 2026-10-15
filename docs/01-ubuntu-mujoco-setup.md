# Ubuntu 与 MuJoCo 环境配置记录

整理日期：2026 年 10 月 15 日

这篇笔记记录我为学习机器人仿真而搭建 Ubuntu 开发环境的过程。内容根据此前的安装与排错记录整理；未保留完整操作的部分只记录结果，不补写成已经执行过的命令。后续以电脑上的实际查询结果为准。

## 1. 配置目标与当前结果

目标是在 Ubuntu 中使用 VS Code 编写 Python 程序，通过 MuJoCo 加载机器人模型，并观察和控制关节运动。

目前已完成 Ubuntu 安装、Miniconda 和 mujoco 环境配置，并已在后续实践中打开机器人模型的可视化窗口。模型加载与关节控制代码将在另一篇笔记中整理。

| 项目 | 当前记录 |
| --- | --- |
| 系统 | Ubuntu，与 Windows 保留为双系统；具体发行版本待查询补充 |
| Ubuntu 磁盘空间 | 约 500 GB |
| 内存 | 16 GB |
| 交换空间 | 已调整为 16 GB；工具可能显示约 15 GiB |
| 显卡 | NVIDIA GeForce RTX 5050，8 GB 显存 |
| 编辑器 | VS Code |
| Python 环境管理 | Miniconda |
| Conda 环境名 | mujoco |
| Python | 3.10.22，历史安装记录 |
| MuJoCo Python 包 | 3.15.0，历史验证记录 |

这里的版本是个人安装记录，不代表其他电脑必须使用相同版本。

## 2. Ubuntu 安装与磁盘安排

使用 Ventoy 制作启动 U 盘，为 Ubuntu 预留约 500 GB 磁盘空间，安装后保留 Windows。

后续机器人学习与开发默认在 Ubuntu 中进行。Windows 原有的 Anaconda 和虚拟环境与 Ubuntu 中新安装的环境分别管理，不会因为安装双系统就自动共用。

这次配置过程中，我逐渐理解到：Linux 下不需要照搬 Windows 的习惯，为每个软件手动建立一个“安装目录”。日常更需要整理的是自己的项目、代码、模型和笔记。

### 交换空间

电脑内存为 16 GB，安装记录中已将 swap 从 4 GB 调整为 16 GB，并配置开机启用。

已有配置记录：

```text
/swap.img none swap sw 0 0
```

这是一条 /etc/fstab 配置记录，不是需要在终端执行的命令，也不需要重复追加。

查看当前内存与 swap：

```bash
free -h
swapon --show
```

swap 是磁盘上的交换空间，不能当作与物理内存性能相同的额外内存。

## 3. 网络与软件源

校园网需要身份认证。配置期间出现过认证页面未正常弹出、零信任客户端影响软件源访问的问题，之后恢复了网络访问。

当时用下面的命令测试过网络：

```bash
ping -c 4 baidu.com
```

历史记录中测试成功。但 ping 成功只说明该目标可访问，下载软件所需的其他网站仍可能受网络限制。

安装过程中讨论并配置过镜像源。Ubuntu 软件源、Conda 软件源和 pip 软件源分别服务于不同的包管理工具，不能把其中一个修改理解为全部修改。由于没有完整保留最终配置，这里先不列出固定的镜像配置文件。

查看现有配置时可使用：

```bash
conda config --show-sources
python -m pip config list
```

## 4. NVIDIA 显卡驱动

通过下面的命令检查显卡与驱动：

```bash
nvidia-smi
```

历史输出能够识别 RTX 5050，记录的驱动版本为 595.99.02，界面显示 CUDA Version 为 13.2。

需要区分：nvidia-smi 中的 CUDA Version 反映驱动支持的 CUDA 版本信息，不能据此确认已经安装相应版本的 CUDA Toolkit。这篇笔记不将 CUDA Toolkit 或 GPU 训练环境记为已完成。

## 5. 开发工具及其作用

环境配置中安装或涉及了以下工具：

| 工具 | 用途 |
| --- | --- |
| VS Code | 编写、运行和调试代码 |
| Git | 管理代码版本，后续与 GitHub 仓库同步 |
| Miniconda | 创建并管理相互独立的 Python 环境 |
| pip | 安装 Python 包 |
| build-essential | 提供常见 C/C++ 编译工具 |
| CMake、Ninja | 配置和执行部分项目的构建流程 |
| pkg-config | 帮助构建工具查找系统库 |
| FFmpeg | 处理视频、音频及相关数据 |
| pipx、Poetry | 分别用于隔离安装 Python 命令行工具、管理 Python 项目依赖；当前 MuJoCo 入门主要使用 Conda 和 pip |

这些工具服务于不同需求，不代表每次运行 MuJoCo 都要使用全部工具。具体安装版本可在后续需要时补充。

## 6. Miniconda 与 mujoco 环境

已经在 Ubuntu 中安装 Miniconda，并建立名为 mujoco 的 Conda 环境。

这里有两个名称相同但含义不同的对象：

- mujoco 环境：由 Conda 管理，包含 Python 和项目依赖。
- mujoco 包：安装在该环境中的 Python 包，用于在程序里调用 MuJoCo。

进入已创建的环境：

```bash
conda activate mujoco
```

查看当前使用的 Python：

```bash
python --version
which python
```

正常情况下，Python 的路径应指向 Miniconda 下的 envs/mujoco/bin/python。历史记录中的 Python 版本为 3.10.22。

新终端没有显示 (base)，不等于 Miniconda 没有安装。当前电脑已确认能够使用 conda activate mujoco 进入目标环境。

Windows 中原有的 lerobot 环境也不等于 Ubuntu 中已经存在对应环境，需要分别记录。

## 7. MuJoCo 安装与验证

MuJoCo 的核心是物理仿真引擎。本次使用方式是在 Conda 环境中安装 Python 包，再通过 Python 接口调用引擎；可视化窗口用于观察与交互，机器人模型文件则提供机器人结构等数据。

历史记录确认已成功导入 mujoco，并输出包版本。

在 mujoco 环境中执行：

```bash
python -c "import mujoco; print(mujoco.__version__)"
```

历史记录中的输出：

```text
3.15.0
```

这说明当时所用的 Python 能找到并导入 mujoco 包。能否加载某个机器人模型、是否能正常打开窗口，还需要通过对应程序验证。

原始安装命令没有完整保留。下面仅列出安装方式供理解，不表示需要在已经可用的环境中重新执行：

```bash
python -m pip install mujoco
```

此命令未指定版本，不保证重新安装后得到与历史记录相同的版本。

## 8. VS Code 配置

安装 VS Code 后，还需要安装微软的 Python 扩展，并为项目选择正确的解释器。

操作步骤：

1. 打开 Python 项目。
2. 按 Ctrl + Shift + P。
3. 搜索 Python: Select Interpreter。
4. 选择 mujoco 环境对应的 Python。
5. 在 VS Code 终端检查 Python 路径，并测试导入 mujoco。

VS Code 选择的运行解释器与终端激活的环境需要分别检查，不能只根据终端前面的环境名称判断所有运行方式都已经使用同一个 Python。

如果出现 No module named mujoco，先检查实际运行程序的解释器，以及包是否安装在该解释器对应的环境里。

## 9. 日常启动与核验

环境已经搭建完成后，日常通常只需要激活环境并运行项目，无需重复安装。

```bash
conda activate mujoco
python --version
which python
python -c "import mujoco; print(mujoco.__version__)"
```

随后在 VS Code 中打开自己的项目，并确认解释器仍指向 mujoco 环境。

需要补充完整系统信息时，可分别查询：

```bash
cat /etc/os-release
git --version
nvidia-smi
free -h
```

这些命令用于查询当前状态；本文没有将它们全部记为本次重新执行并验证过。

## 10. 本阶段的理解与后续任务

通过这次配置，我开始区分操作系统、编辑器、Python 解释器、虚拟环境、Python 包和机器人模型各自的作用：

- Ubuntu 提供操作系统环境。
- VS Code 提供代码编辑与调试界面。
- Conda 管理不同项目的 Python 环境。
- Python 运行控制程序。
- mujoco 包提供调用 MuJoCo 的 Python 接口。
- 模型文件描述机器人结构及相关仿真参数。
- Viewer 显示仿真场景。

后续工作：

- [ ] 根据实际查询结果补充 Ubuntu 的发行版本。
- [ ] 归档 SO-101 模型加载和首次关节控制代码。
- [ ] 记录模型来源、项目目录及运行方式。
- [ ] 完成 G1 模型导入与关节运动展示。
- [ ] 为代码补充依赖版本与演示截图。

[返回仓库首页](../README.md)
