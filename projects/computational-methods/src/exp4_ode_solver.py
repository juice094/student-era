"""
实验四：常微分方程初值问题的数值解法
核心算法：改进欧拉法（预测-校正法）、四阶经典龙格-库塔法
编写者：20231304002_周景潇 日期：2026/05/20
"""

import os
import numpy as np

try:
    if os.environ.get('DISPLAY') is None and os.name != 'nt':
        import matplotlib
        matplotlib.use('Agg')
    import matplotlib.pyplot as plt
except ImportError:
    plt = None


def _get_output_path(filename):
    output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'outputs'))
    os.makedirs(output_dir, exist_ok=True)
    return os.path.join(output_dir, filename)


def euler(f, t0, y0, h, n_steps):
    """
    基本欧拉法（显式 Euler）

    y_{k+1} = y_k + h * f(t_k, y_k)

    局部截断误差：O(h²)，整体误差：O(h)

    Args:
        f: dy/dt = f(t, y)
        t0, y0: 初值
        h: 步长
        n_steps: 迭代步数

    Returns:
        t, y: 时间序列和解序列
    """
    t = np.zeros(n_steps + 1)
    y = np.zeros(n_steps + 1)
    t[0], y[0] = t0, y0

    for k in range(n_steps):
        y[k + 1] = y[k] + h * f(t[k], y[k])
        t[k + 1] = t[k] + h

    return t, y


def improved_euler(f, t0, y0, h, n_steps):
    """
    改进欧拉法（Heun 方法 / 预测-校正法）

    预测：y_p = y_k + h * f(t_k, y_k)
    校正：y_{k+1} = y_k + h/2 * [f(t_k, y_k) + f(t_{k+1}, y_p)]

    局部截断误差：O(h^3)，整体误差：O(h^2)

    Args:
        f: dy/dt = f(t, y)
        t0, y0: 初值
        h: 步长
        n_steps: 迭代步数

    Returns:
        t, y: 时间序列和解序列
    """
    t = np.zeros(n_steps + 1)
    y = np.zeros(n_steps + 1)
    t[0], y[0] = t0, y0

    for k in range(n_steps):
        k1 = f(t[k], y[k])
        y_pred = y[k] + h * k1
        k2 = f(t[k] + h, y_pred)
        y[k + 1] = y[k] + h / 2 * (k1 + k2)
        t[k + 1] = t[k] + h

    return t, y


def rk4(f, t0, y0, h, n_steps):
    """
    四阶经典龙格-库塔法

    k1 = f(t_k, y_k)
    k2 = f(t_k + h/2, y_k + h*k1/2)
    k3 = f(t_k + h/2, y_k + h*k2/2)
    k4 = f(t_k + h, y_k + h*k3)
    y_{k+1} = y_k + h/6 * (k1 + 2*k2 + 2*k3 + k4)

    局部截断误差：O(h^5)，整体误差：O(h^4)

    Args:
        f: dy/dt = f(t, y)
        t0, y0: 初值
        h: 步长
        n_steps: 迭代步数

    Returns:
        t, y: 时间序列和解序列
    """
    t = np.zeros(n_steps + 1)
    y = np.zeros(n_steps + 1)
    t[0], y[0] = t0, y0

    for k in range(n_steps):
        k1 = f(t[k], y[k])
        k2 = f(t[k] + h / 2, y[k] + h * k1 / 2)
        k3 = f(t[k] + h / 2, y[k] + h * k2 / 2)
        k4 = f(t[k] + h, y[k] + h * k3)
        y[k + 1] = y[k] + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        t[k + 1] = t[k] + h

    return t, y


def plot_solutions(t_ieu, y_ieu, t_rk4, y_rk4, t_exact=None, y_exact=None):
    """绘制数值解与精确解对比"""
    if plt is None:
        print('matplotlib 不可用，无法绘图。')
        return

    output_path = _get_output_path('exp4_ode_solutions.png')
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.plot(t_ieu, y_ieu, 'o-', label='Improved Euler', markersize=3)
    plt.plot(t_rk4, y_rk4, 's-', label='RK4', markersize=3)
    if t_exact is not None and y_exact is not None:
        plt.plot(t_exact, y_exact, 'k-', label='Exact', linewidth=1.5)
    plt.xlabel('t')
    plt.ylabel('y')
    plt.title('Numerical Solutions')
    plt.legend()
    plt.grid(True)

    plt.subplot(1, 2, 2)
    if t_exact is not None and y_exact is not None:
        err_ieu = np.abs(np.interp(t_exact, t_ieu, y_ieu) - y_exact)
        err_rk4 = np.abs(np.interp(t_exact, t_rk4, y_rk4) - y_exact)
        plt.semilogy(t_exact, err_ieu, 'o-', label='Improved Euler', markersize=3)
        plt.semilogy(t_exact, err_rk4, 's-', label='RK4', markersize=3)
        plt.ylabel('Absolute Error (log)')
        plt.title('Error Comparison')
    else:
        plt.text(0.5, 0.5, 'Exact solution not provided', ha='center', va='center')
    plt.xlabel('t')
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.show()
    print(f"Figure saved to {output_path}")


def plot_step_size_effect(f, t0, y0, t_end, y_exact_func):
    """展示不同步长对精度的影响"""
    if plt is None:
        print('matplotlib 不可用，无法绘图。')
        return

    h_values = [0.2, 0.1, 0.05, 0.025, 0.01]
    errors_ie = []
    errors_rk4 = []

    for h in h_values:
        n = int((t_end - t0) / h)
        _, y_ie = improved_euler(f, t0, y0, h, n)
        _, y_rk = rk4(f, t0, y0, h, n)
        y_true = y_exact_func(t0 + n * h)
        errors_ie.append(abs(y_ie[-1] - y_true))
        errors_rk4.append(abs(y_rk[-1] - y_true))

    output_path = _get_output_path('exp4_step_size.png')
    plt.figure(figsize=(8, 5))
    plt.loglog(h_values, errors_ie, 'o-', label='Improved Euler', markersize=6)
    plt.loglog(h_values, errors_rk4, 's-', label='RK4', markersize=6)
    plt.xlabel('Step size h')
    plt.ylabel('Error at t_end')
    plt.title('Step Size vs. Accuracy')
    plt.legend()
    plt.grid(True, which='both', linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.show()
    print(f"Figure saved to {output_path}")


def main():
    print("=" * 60)
    print("实验四：常微分方程初值问题的数值解法")
    print("=" * 60)

    # ==================== 例 9.6.1 基本欧拉法 ====================
    print("\n【例 9.6.1 基本欧拉法】")
    print("微分方程: dy/dx = x - y,  0 ≤ x ≤ 1")
    print("初值:     y(0) = 0")
    print("步长:     h = 0.1")

    def f_961(t, y):
        return t - y

    def y_exact_961(t):
        """精确解: y = x - 1 + e^(-x)"""
        return t - 1 + np.exp(-t)

    t0, y0 = 0, 0
    h = 0.1
    n_steps = 10  # x 从 0 到 1

    # 基本欧拉法
    t_euler, y_euler = euler(f_961, t0, y0, h, n_steps)
    y_euler_at_1 = y_euler[-1]
    y_exact_at_1 = y_exact_961(1.0)

    print(f"\n基本欧拉法:  y(1.0) = {y_euler_at_1:.14f}")
    print(f"精确值:      y(1.0) = {y_exact_at_1:.14f}  (= e⁻¹ ≈ 0.36787944117)")
    print(f"绝对误差:    {abs(y_euler_at_1 - y_exact_at_1):.2e}")
    print(f"教材参考值:  y(1.0) ≈ 0.34867844010000")

    # 改进欧拉法对比
    t_ieu, y_ieu = improved_euler(f_961, t0, y0, h, n_steps)
    y_ieu_at_1 = y_ieu[-1]
    print(f"\n改进欧拉法:  y(1.0) = {y_ieu_at_1:.14f}")
    print(f"绝对误差:    {abs(y_ieu_at_1 - y_exact_at_1):.2e}")

    # 四阶 RK 法对比
    t_rk, y_rk = rk4(f_961, t0, y0, h, n_steps)
    y_rk_at_1 = y_rk[-1]
    print(f"四阶 RK 法:  y(1.0) = {y_rk_at_1:.14f}")
    print(f"绝对误差:    {abs(y_rk_at_1 - y_exact_at_1):.2e}")

    # 步进过程表
    print(f"\n{'k':>3} | {'x_k':>6} | {'欧拉 y_k':>14} | {'改进欧拉 y_k':>14} | {'RK4 y_k':>14} | {'精确 y':>14}")
    print("-" * 85)
    for k in range(n_steps + 1):
        xk = t_euler[k]
        ye = y_euler[k]
        yi = y_ieu[k]
        yr = y_rk[k]
        yx = y_exact_961(xk)
        print(f"{k:3d} | {xk:6.1f} | {ye:14.10f} | {yi:14.10f} | {yr:14.10f} | {yx:14.10f}")

    print("\n结论:")
    print("  1. 基本欧拉法 O(h) 精度最低，误差约 2e-2")
    print("  2. 改进欧拉法 O(h²) 精度中等，误差约 2e-4")
    print("  3. 四阶 RK 法 O(h⁴) 精度最高，误差约 3e-7")
    print("  4. 步长 h=0.1 时，RK4 已足够精确")

    # ==================== 原有示例（dy/dt = -2ty）====================
    print("\n" + "=" * 60)
    print("【附加示例：dy/dt = -2ty 的数值解对比】")
    print("=" * 60)

    def f_demo(t, y):
        return -2 * t * y

    def y_exact_demo(t):
        return np.exp(-t**2)

    t0_d, y0_d = 0, 1
    t_end_d = 2
    h_d = 0.1
    n_steps_d = int((t_end_d - t0_d) / h_d)

    t_e_d, y_e_d = euler(f_demo, t0_d, y0_d, h_d, n_steps_d)
    t_ie_d, y_ie_d = improved_euler(f_demo, t0_d, y0_d, h_d, n_steps_d)
    t_rk_d, y_rk_d = rk4(f_demo, t0_d, y0_d, h_d, n_steps_d)

    print(f"\nt={t_end_d} 时:")
    print(f"  基本欧拉:   y={y_e_d[-1]:.10f}, 误差={abs(y_e_d[-1] - y_exact_demo(t_end_d)):.2e}")
    print(f"  改进欧拉:   y={y_ie_d[-1]:.10f}, 误差={abs(y_ie_d[-1] - y_exact_demo(t_end_d)):.2e}")
    print(f"  四阶 RK:    y={y_rk_d[-1]:.10f}, 误差={abs(y_rk_d[-1] - y_exact_demo(t_end_d)):.2e}")
    print(f"  精确值:     y={y_exact_demo(t_end_d):.10f}")

    t_fine = np.linspace(t0_d, t_end_d, 500)
    y_fine = y_exact_demo(t_fine)
    plot_solutions(t_ie_d, y_ie_d, t_rk_d, y_rk_d, t_fine, y_fine)
    plot_step_size_effect(f_demo, t0_d, y0_d, t_end_d, y_exact_demo)


if __name__ == "__main__":
    main()
