# SO-101 测试代码说明

这里保存学习过程中编写的最小测试代码，用于先验证数学关系，再连接到完整的 SO-101 和 MuJoCo 模型。

## 当前测试

`test_dls_ik.py` 包含两个测试：

1. 验证一次阻尼最小二乘更新可以减小末端位置误差。
2. 验证接近奇异雅可比时，加入阻尼后仍能得到有限的关节增量。

## 运行方式

在 Ubuntu 中执行：

```bash
conda activate mujoco
cd 02_MuJoCo/SO101/tests
python test_dls_ik.py
```

输出：

```text
DLS tests passed
```

后续会继续加入 FK 与 MuJoCo 模型末端位置的一致性测试，以及 PD 控制的目标角度和稳态误差测试。
