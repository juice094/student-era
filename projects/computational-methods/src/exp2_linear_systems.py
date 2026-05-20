"""
实验二：解线性方程组的直接法与迭代法
核心算法：列主元高斯消去法、雅可比迭代法、高斯-塞德尔迭代法
编写者：20231304002_周景潇 日期：2026/05/20
"""

import os
import numpy as np

if os.environ.get('DISPLAY') is None and os.name != 'nt':
    import matplotlib
    matplotlib.use('Agg')
try:
    import matplotlib.pyplot as plt
except Exception:
    # matplotlib may not be available in the environment (or Pylance cannot resolve it).
    # Fallback: set plt to None and handle plotting functions accordingly.
    plt = None


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
    if plt is None:
        print("matplotlib is not available; skipping plot_residuals.")
        return

    plt.figure(figsize=(8, 5))
    plt.semilogy(range(1, len(jacobi_hist) + 1), jacobi_hist, 'o-', label='Jacobi', markersize=3)
    plt.semilogy(range(1, len(gs_hist) + 1), gs_hist, 's-', label='Gauss-Seidel', markersize=3)
    plt.xlabel('Iteration')
    plt.ylabel('Residual ||Ax - b|| (log scale)')
    plt.title('Convergence of Iterative Methods')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    out_path = os.path.join(os.path.dirname(__file__), '..', 'outputs', 'exp2_residuals.png')
    out_dir = os.path.dirname(out_path)
    os.makedirs(out_dir, exist_ok=True)
    plt.savefig(out_path, dpi=150)
    # Only call plt.show() when an interactive display is available
    if not (os.environ.get('DISPLAY') is None and os.name != 'nt'):
        plt.show()
    print(f"Figure saved to {out_path}")


def main():
    print("=" * 60)
    print("实验二：解线性方程组的直接法与迭代法")
    print("=" * 60)

    # ==================== 例 5.6.1 列主元高斯消去法 ====================
    A1 = np.array([
        [12, -3, 3],
        [-18, 3, -1],
        [1, 1, 1]
    ], dtype=float)
    b1 = np.array([15, -15, 6], dtype=float)

    print("\n【例 5.6.1 列主元高斯消去法】")
    print("方程组 Ax = b")
    print("A = [[12, -3, 3], [-18, 3, -1], [1, 1, 1]]")
    print("b = [15, -15, 6]")

    x_direct1 = gauss_elimination_pivot(A1, b1)
    print(f"\n解向量: {x_direct1}")
    print(f"残差 ||Ax - b|| = {np.linalg.norm(A1 @ x_direct1 - b1):.2e}")
    print("验证: 精确解应为 [1, 2, 3]")

    # ==================== 例 6.5.1 雅可比迭代法 ====================
    A2 = np.array([
        [10, -1, -2],
        [-1, 10, -2],
        [-1, -1, 5]
    ], dtype=float)
    b2 = np.array([72, 83, 42], dtype=float)

    print("\n【例 6.5.1 雅可比迭代法】")
    print("方程组 Ax = b")
    print("A = [[10, -1, -2], [-1, 10, -2], [-1, -1, 5]]")
    print("b = [72, 83, 42]")
    print("初值 x0 = [0, 0, 0], 精度 eps = 1e-6")

    x_jacobi, hist_j = jacobi(A2, b2, eps=1e-6)
    print(f"\n解向量: {x_jacobi}")
    print(f"迭代次数: {len(hist_j)}")
    print("验证: 精确解应为 [11, 12, 13]")

    # ==================== 例 6.5.2 高斯-塞德尔迭代法 ====================
    print("\n【例 6.5.2 高斯-塞德尔迭代法】")
    print("方程组 Ax = b (同上)")
    print("初值 x0 = [0, 0, 0], 精度 eps = 1e-6")

    x_gs, hist_gs = gauss_seidel(A2, b2, eps=1e-6)
    print(f"\n解向量: {x_gs}")
    print(f"迭代次数: {len(hist_gs)}")
    print("验证: 精确解应为 [11, 12, 13]")

    # ==================== 同方程组直接法对比 ====================
    # 用列主元高斯消去法也解 A2, b2，以便直接法 vs 迭代法对比
    print("\n【同方程组直接法求解（对比用）】")
    print("对例 6.5.x 的方程组使用列主元高斯消去法:")
    x_direct2 = gauss_elimination_pivot(A2, b2)
    print(f"解向量: {x_direct2}")
    print(f"残差 ||Ax - b|| = {np.linalg.norm(A2 @ x_direct2 - b2):.2e}")

    # ==================== 结果对比总结 ====================
    print("\n" + "=" * 60)
    print("【方法对比总结】")
    print("=" * 60)

    print("\n方程组 1 (例 5.6.1):")
    print(f"  列主元高斯消去法: x = {x_direct1}")

    print("\n方程组 2 (例 6.5.x):")
    print(f"  列主元高斯消去法: x = {x_direct2}")
    print(f"  雅可比迭代法:      x = {x_jacobi}, 迭代 {len(hist_j)} 次")
    print(f"  高斯-塞德尔法:     x = {x_gs}, 迭代 {len(hist_gs)} 次")

    print("\n结论:")
    print(f"  1. 直接法在有限步内理论上可得精确解（此处残差 {np.linalg.norm(A2 @ x_direct2 - b2):.2e}）")
    print(f"  2. 高斯-塞德尔法比雅可比法收敛更快（{len(hist_gs)} 次 vs {len(hist_j)} 次）")
    print("  3. 迭代法适合大型稀疏矩阵，直接法适合中低阶稠密方程组")

    plot_residuals(hist_j, hist_gs)


if __name__ == "__main__":
    main()
