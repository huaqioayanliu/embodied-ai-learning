"""用于理解阻尼最小二乘逆运动学的最小测试。

这是学习用测试代码，不是对真实 SO-101 的完整控制器。
运行：
    python test_dls_ik.py
"""

import numpy as np


def damped_pseudoinverse(jacobian: np.ndarray, damping: float) -> np.ndarray:
    """计算 J^T (J J^T + λ²I)^-1。"""
    rows = jacobian.shape[0]
    identity = np.eye(rows)
    return jacobian.T @ np.linalg.inv(
        jacobian @ jacobian.T + damping**2 * identity
    )


def test_dls_reduces_position_error() -> None:
    """验证一次 DLS 更新能够减小一个平面位置误差。"""
    jacobian = np.array(
        [
            [1.0, 0.0],
            [0.0, 0.5],
        ]
    )
    error_before = np.array([0.2, -0.1])
    damping = 0.01

    delta_q = damped_pseudoinverse(jacobian, damping) @ error_before
    error_after = error_before - jacobian @ delta_q

    assert np.linalg.norm(error_after) < np.linalg.norm(error_before)


def test_dls_handles_near_singular_jacobian() -> None:
    """验证加入阻尼后，接近奇异的雅可比仍能得到有限结果。"""
    jacobian = np.array(
        [
            [1.0, 1.0],
            [1.0, 1.0 + 1e-8],
        ]
    )
    delta_q = damped_pseudoinverse(jacobian, 0.05) @ np.array([0.1, 0.1])

    assert np.all(np.isfinite(delta_q))


if __name__ == "__main__":
    test_dls_reduces_position_error()
    test_dls_handles_near_singular_jacobian()
    print("DLS tests passed")
