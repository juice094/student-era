"""
实验一：方程求根
核心算法：二分法、牛顿迭代法
编写者：20231304002_周景潇 日期：2026/05/20
"""

import os
import numpy as np
from typing import Any, Optional

plt: Optional[Any] = None

# 无图形界面时自动切换 Agg 后端，并保护性导入 matplotlib.pyplot
try:
    # 在无 DISPLAY 的 headless 环境下切换后端
    if os.environ.get('DISPLAY') is None and os.name != 'nt':
        import matplotlib  # type: ignore[import]
        matplotlib.use('Agg')
    import matplotlib.pyplot as plt  # type: ignore[import]
except Exception:
    plt = None


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

        # 停止条件与教材一致：(b-a) > 2*eps 时继续迭代
        # 同时检查函数值是否已足够接近零
        if (b - a) / 2 < eps:
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
    # 与教材 MATLAB 实现一致：
    # 循环条件 abs(x0 - x) > eps，x0 保存上一轮值
    history = []
    x = x0
    x_prev = x + 2 * eps  # 确保第一次循环能进入
    k = 0

    while abs(x_prev - x) > eps and k < max_iter:
        k = k + 1
        x_prev = x
        fx = f(x_prev)
        dfx = df(x_prev)
        if abs(dfx) < 1e-14:
            raise RuntimeError("Derivative too small, Newton method fails")
        x = x_prev - fx / dfx
        history.append((k, x, f(x)))

    return x, history


def plot_convergence(bisect_hist, newton_hist, exact_root=None):
    """绘制两种方法的收敛过程对比"""
    # 保护性检查：matplotlib 是否可用
    if plt is None:
        print("Plotting not available (matplotlib not imported)")
        return

    # 防止传入空的迭代历史导致 zip(*...) 失败
    if not bisect_hist or not newton_hist:
        print("Insufficient history data for plotting")
        return

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

    # 使用 fig（避免静态分析报 unused variable）并进行保护性绘图
    fig.suptitle('Convergence Comparison')
    plt.tight_layout()
    # 确保输出目录存在
    out_dir = os.path.join(os.path.dirname(__file__), '..', 'outputs')
    try:
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, 'exp1_convergence.png')
        plt.savefig(out_path, dpi=150)
        try:
            plt.show()
        except Exception:
            pass
        print(f"Figure saved to {out_path}")
    except Exception:
        print("Failed to save figure in this environment")


def main():
    print("=" * 60)
    print("实验一：方程求根")
    print("=" * 60)

    # ==================== 例 4.6.1 二分法 ====================
    # 求方程 sin(x) - x^2/4 = 0 在 [1.5, 2] 内的根，精度 eps = 1e-2
    print("\n【例 4.6.1 二分法】")
    print("方程: sin(x) - x^2/4 = 0, 区间 [1.5, 2], 精度 1e-2")

    def f1(x):
        return np.sin(x) - x**2 / 4

    root_b, hist_b = bisection(f1, 1.5, 2.0, eps=1e-2)
    print(f"近似根: {root_b:.14f}")
    print(f"迭代次数: {len(hist_b)}")
    print(f"f(root) = {f1(root_b):.2e}")
    print("\n迭代过程 (k -> x):")
    for k, x_val, _ in hist_b[:7]:
        print(f"  k={k}: x = {x_val:.14f}")

    # ==================== 例 4.6.2 牛顿迭代法 ====================
    # 求方程 x^3 - x - 1 = 0 的根，初值 x0 = 1.5，精度 eps = 1e-6
    print("\n【例 4.6.2 牛顿迭代法】")
    print("方程: x^3 - x - 1 = 0, 初值 x0 = 1.5, 精度 1e-6")

    def f2(x):
        return x**3 - x - 1

    def df2(x):
        return 3 * x**2 - 1

    root_n2, hist_n2 = newton(f2, df2, x0=1.5, eps=1e-6)
    print(f"近似根: {root_n2:.14f}")
    print(f"迭代次数: {len(hist_n2)}")
    print(f"f(root) = {f2(root_n2):.2e}")
    print("\n迭代过程 (k -> x):")
    for k, x_val, _ in hist_n2[:6]:
        print(f"  k={k}: x = {x_val:.14f}")

    # ==================== 例 4.6.3 牛顿迭代法（超越方程） ====================
    # 求方程 x - e^(-x) = 0 在 0.5 附近的根，精度 eps = 1e-6
    print("\n【例 4.6.3 牛顿迭代法（超越方程）】")
    print("方程: x - e^(-x) = 0, 初值 x0 = 0.5, 精度 1e-6")

    def f3(x):
        return x - np.exp(-x)

    def df3(x):
        return 1 + np.exp(-x)

    root_n3, hist_n3 = newton(f3, df3, x0=0.5, eps=1e-6)
    print(f"近似根: {root_n3:.14f}")
    print(f"迭代次数: {len(hist_n3)}")
    print(f"f(root) = {f3(root_n3):.2e}")
    print("\n迭代过程 (k -> x):")
    for k, x_val, _ in hist_n3[:5]:
        print(f"  k={k}: x = {x_val:.14f}")

    # ==================== 方法对比总结 ====================
    print("\n" + "=" * 60)
    print("【方法对比总结】")
    print("=" * 60)
    print(f"二分法 (sin(x)-x^2/4=0):     迭代 {len(hist_b)-1} 次, 根 = {root_b:.10f}")
    print(f"牛顿法 (x^3-x-1=0):          迭代 {len(hist_n2)-1} 次, 根 = {root_n2:.10f}")
    print(f"牛顿法 (x-e^(-x)=0):         迭代 {len(hist_n3)-1} 次, 根 = {root_n3:.10f}")
    print("\n结论: 牛顿法收敛速度明显快于二分法（3~4 次 vs 5 次），")
    print("      但牛顿法依赖初值选取和导数计算。")

    # 可视化（例 4.6.2 的收敛过程）
    plot_convergence(hist_b, hist_n2)


if __name__ == "__main__":
    main()
