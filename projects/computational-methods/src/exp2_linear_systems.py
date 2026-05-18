"""
实验二：解线性方程组的直接法与迭代法
核心算法：列主元高斯消去法、雅可比迭代法、高斯-塞德尔迭代法
"""

import os
import numpy as np

if os.environ.get('DISPLAY') is None and os.name != 'nt':
    import matplotlib
    matplotlib.use('Agg')
import matplotlib.pyplot as plt


def gauss_elimination_pivot(A, b):
    """
    列主元高斯消去法求解 Ax = b

    Args:
        A: n x n 系数矩阵 (NumPy ndarray)
        b: n x 1 右端向量

    Returns:
        x: 解向量
    """
    n = len(b)
    # 构造增广矩阵 [A|b]
    Ab = np.hstack([A.astype(float), b.reshape(-1, 1).astype(float)])

    # 前向消元
    for k in range(n - 1):
        # 列主元选取
        max_idx = np.argmax(np.abs(Ab[k:n, k])) + k
        if max_idx != k:
            Ab[[k, max_idx]] = Ab[[max_idx, k]]

        if abs(Ab[k, k]) < 1e-14:
            raise ValueError("Matrix is singular or nearly singular")

        for i in range(k + 1, n):
            factor = Ab[i, k] / Ab[k, k]
            Ab[i, k:] -= factor * Ab[k, k:]

    # 回代
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (Ab[i, -1] - np.dot(Ab[i, i + 1:n], x[i + 1:n])) / Ab[i, i]

    return x


def jacobi(A, b, x0=None, eps=1e-6, max_iter=1000):
    """
    雅可比迭代法求解 Ax = b

    迭代公式：x_i^{(k+1)} = (b_i - sum_{j!=i} a_{ij} x_j^{(k)}) / a_{ii}

    Returns:
        (x, history): 解向量和残差历史 [||Ax-b||]
    """
    n = len(b)
    x = np.zeros(n) if x0 is None else x0.copy()
    x_new = np.zeros(n)
    history = []

    for _ in range(max_iter):
        for i in range(n):
            x_new[i] = (b[i] - np.dot(A[i, :i], x[:i]) - np.dot(A[i, i + 1:], x[i + 1:])) / A[i, i]

        residual = np.linalg.norm(A @ x_new - b)
        history.append(residual)

        if residual < eps:
            return x_new, history

        x[:] = x_new

    return x, history


def gauss_seidel(A, b, x0=None, eps=1e-6, max_iter=1000):
    """
    高斯-塞德尔迭代法求解 Ax = b

    与雅可比法的区别：计算 x_i^{(k+1)} 时立即使用已更新的分量

    Returns:
        (x, history): 解向量和残差历史 [||Ax-b||]
    """
    n = len(b)
    x = np.zeros(n) if x0 is None else x0.copy()
    history = []

    for _ in range(max_iter):
        for i in range(n):
            x[i] = (b[i] - np.dot(A[i, :i], x[:i]) - np.dot(A[i, i + 1:], x[i + 1:])) / A[i, i]

        residual = np.linalg.norm(A @ x - b)
        history.append(residual)

        if residual < eps:
            return x, history

    return x, history


def plot_residuals(jacobi_hist, gs_hist):
    """绘制迭代法残差收敛曲线"""
    plt.figure(figsize=(8, 5))
    plt.semilogy(range(1, len(jacobi_hist) + 1), jacobi_hist, 'o-', label='Jacobi', markersize=3)
    plt.semilogy(range(1, len(gs_hist) + 1), gs_hist, 's-', label='Gauss-Seidel', markersize=3)
    plt.xlabel('Iteration')
    plt.ylabel('Residual ||Ax - b|| (log scale)')
    plt.title('Convergence of Iterative Methods')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('../outputs/exp2_residuals.png', dpi=150)
    plt.show()
    print("Figure saved to ../outputs/exp2_residuals.png")


def main():
    # TODO: 根据教师给出的具体方程组修改这里
    # 示例方程组
    A = np.array([
        [10, -1, 2, 0],
        [-1, 11, -1, 3],
        [2, -1, 10, -1],
        [0, 3, -1, 8]
    ], dtype=float)
    b = np.array([6, 25, -11, 15], dtype=float)

    print("=" * 50)
    print("实验二：解线性方程组的直接法与迭代法")
    print("=" * 50)

    # 直接法
    print("\n【列主元高斯消去法】")
    x_direct = gauss_elimination_pivot(A, b)
    print(f"解向量: {x_direct}")
    print(f"残差 ||Ax - b|| = {np.linalg.norm(A @ x_direct - b):.2e}")

    # 迭代法
    print("\n【雅可比迭代法】")
    x_jacobi, hist_j = jacobi(A, b, eps=1e-6)
    print(f"解向量: {x_jacobi}")
    print(f"迭代次数: {len(hist_j)}")

    print("\n【高斯-塞德尔迭代法】")
    x_gs, hist_gs = gauss_seidel(A, b, eps=1e-6)
    print(f"解向量: {x_gs}")
    print(f"迭代次数: {len(hist_gs)}")

    # 与 NumPy 精确解对比
    x_exact = np.linalg.solve(A, b)
    print(f"\n【NumPy 参考解】{x_exact}")
    print(f"直接法误差: {np.linalg.norm(x_direct - x_exact):.2e}")
    print(f"雅可比法误差: {np.linalg.norm(x_jacobi - x_exact):.2e}")
    print(f"GS 法误差: {np.linalg.norm(x_gs - x_exact):.2e}")

    plot_residuals(hist_j, hist_gs)


if __name__ == "__main__":
    main()
