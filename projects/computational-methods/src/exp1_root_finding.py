"""
实验一：方程求根
核心算法：二分法、牛顿迭代法
"""

import os
import numpy as np

# 无图形界面时自动切换 Agg 后端
if os.environ.get('DISPLAY') is None and os.name != 'nt':
    import matplotlib
    matplotlib.use('Agg')
import matplotlib.pyplot as plt


def bisection(f, a, b, eps=1e-6, max_iter=100):
    """
    二分法求方程 f(x)=0 在区间 [a,b] 内的根

    前提条件：f(a) * f(b) < 0（介值定理保证根的存在性）

    Args:
        f: 目标函数
        a, b: 初始区间端点
        eps: 精度容差
        max_iter: 最大迭代次数

    Returns:
        (root, history): 近似根和迭代历史 [(iter, mid, f_mid), ...]
    """
    if f(a) * f(b) >= 0:
        raise ValueError("f(a) and f(b) must have opposite signs")

    history = []
    for k in range(max_iter):
        mid = (a + b) / 2.0
        f_mid = f(mid)
        history.append((k + 1, mid, f_mid))

        if abs(f_mid) < eps or (b - a) / 2 < eps:
            return mid, history

        if f(a) * f_mid < 0:
            b = mid
        else:
            a = mid

    return mid, history


def newton(f, df, x0, eps=1e-6, max_iter=100):
    """
    牛顿迭代法求方程 f(x)=0 的根

    迭代公式：x_{k+1} = x_k - f(x_k) / f'(x_k)
    收敛条件：|x_{k+1} - x_k| < eps 或 |f(x_k)| < eps

    Args:
        f: 目标函数
        df: 导函数 f'
        x0: 初始猜测值
        eps: 精度容差
        max_iter: 最大迭代次数

    Returns:
        (root, history): 近似根和迭代历史 [(iter, x_k, f_xk), ...]
    """
    history = []
    x = x0
    for k in range(max_iter):
        fx = f(x)
        history.append((k + 1, x, fx))

        if abs(fx) < eps:
            return x, history

        dfx = df(x)
        if abs(dfx) < 1e-14:
            raise RuntimeError("Derivative too small, Newton method fails")

        x_new = x - fx / dfx
        if abs(x_new - x) < eps:
            history.append((k + 2, x_new, f(x_new)))
            return x_new, history

        x = x_new

    return x, history


def plot_convergence(bisect_hist, newton_hist, exact_root=None):
    """绘制两种方法的收敛过程对比"""
    fig, axes = plt.subplots(1, 2, figsize=(12, 4))

    # 左图：迭代过程中的近似根
    ax = axes[0]
    b_iters, b_roots, _ = zip(*bisect_hist)
    n_iters, n_roots, _ = zip(*newton_hist)
    ax.plot(b_iters, b_roots, 'o-', label='Bisection', markersize=4)
    ax.plot(n_iters, n_roots, 's-', label='Newton', markersize=4)
    if exact_root is not None:
        ax.axhline(exact_root, color='gray', linestyle='--', label='Exact root')
    ax.set_xlabel('Iteration')
    ax.set_ylabel('Approximate root')
    ax.set_title('Root Approximation Over Iterations')
    ax.legend()
    ax.grid(True)

    # 右图：误差下降曲线（对数坐标）
    ax = axes[1]
    if exact_root is not None:
        b_errs = [abs(r - exact_root) for _, r, _ in bisect_hist]
        n_errs = [abs(r - exact_root) for _, r, _ in newton_hist]
        ax.semilogy(b_iters, b_errs, 'o-', label='Bisection', markersize=4)
        ax.semilogy(n_iters, n_errs, 's-', label='Newton', markersize=4)
        ax.set_ylabel('Absolute Error (log scale)')
    else:
        b_errs = [abs(fx) for _, _, fx in bisect_hist]
        n_errs = [abs(fx) for _, _, fx in newton_hist]
        ax.semilogy(b_iters, b_errs, 'o-', label='Bisection', markersize=4)
        ax.semilogy(n_iters, n_errs, 's-', label='Newton', markersize=4)
        ax.set_ylabel('|f(x)| (log scale)')

    ax.set_xlabel('Iteration')
    ax.set_title('Convergence Speed Comparison')
    ax.legend()
    ax.grid(True)

    plt.tight_layout()
    plt.savefig('../outputs/exp1_convergence.png', dpi=150)
    plt.show()
    print("Figure saved to ../outputs/exp1_convergence.png")


def main():
    # TODO: 根据教师给出的具体方程修改这里
    # 示例方程：f(x) = x^3 - x - 2 = 0, 精确根约为 1.521
    def f(x):
        return x**3 - x - 2

    def df(x):
        return 3*x**2 - 1

    print("=" * 50)
    print("实验一：方程求根")
    print("=" * 50)

    # 二分法
    print("\n【二分法】")
    root_b, hist_b = bisection(f, 1.0, 2.0, eps=1e-6)
    print(f"近似根: {root_b:.10f}")
    print(f"迭代次数: {len(hist_b)}")
    print(f"f(root) = {f(root_b):.2e}")

    # 牛顿法
    print("\n【牛顿迭代法】")
    root_n, hist_n = newton(f, df, x0=1.5, eps=1e-6)
    print(f"近似根: {root_n:.10f}")
    print(f"迭代次数: {len(hist_n)}")
    print(f"f(root) = {f(root_n):.2e}")

    # 可视化
    plot_convergence(hist_b, hist_n)


if __name__ == "__main__":
    main()
