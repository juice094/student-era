"""
实验四：常微分方程初值问题的数值解法
核心算法：改进欧拉法（预测-校正法）、四阶经典龙格-库塔法
"""

import os
import numpy as np

if os.environ.get('DISPLAY') is None and os.name != 'nt':
    import matplotlib
    matplotlib.use('Agg')
import matplotlib.pyplot as plt


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
    plt.savefig('../outputs/exp4_ode_solutions.png', dpi=150)
    plt.show()
    print("Figure saved to ../outputs/exp4_ode_solutions.png")


def plot_step_size_effect(f, t0, y0, t_end, y_exact_func):
    """展示不同步长对精度的影响"""
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

    plt.figure(figsize=(8, 5))
    plt.loglog(h_values, errors_ie, 'o-', label='Improved Euler', markersize=6)
    plt.loglog(h_values, errors_rk4, 's-', label='RK4', markersize=6)
    plt.xlabel('Step size h')
    plt.ylabel('Error at t_end')
    plt.title('Step Size vs. Accuracy')
    plt.legend()
    plt.grid(True, which='both', linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.savefig('../outputs/exp4_step_size.png', dpi=150)
    plt.show()
    print("Figure saved to ../outputs/exp4_step_size.png")


def main():
    print("=" * 50)
    print("实验四：常微分方程初值问题的数值解法")
    print("=" * 50)

    # TODO: 根据教师给出的具体微分方程修改这里
    # 示例：dy/dt = -2*t*y, y(0)=1, 精确解 y(t) = exp(-t^2)
    def f(t, y):
        return -2 * t * y

    def y_exact(t):
        return np.exp(-t**2)

    t0, y0 = 0, 1
    t_end = 2
    h = 0.1
    n_steps = int((t_end - t0) / h)

    print(f"\n求解区间: [{t0}, {t_end}], 步长 h={h}, 步数 n={n_steps}")

    # 改进欧拉法
    t_ie, y_ie = improved_euler(f, t0, y0, h, n_steps)
    print(f"\n【改进欧拉法】t={t_end} 时 y={y_ie[-1]:.10f}")
    print(f"精确值: {y_exact(t_end):.10f}")
    print(f"误差: {abs(y_ie[-1] - y_exact(t_end)):.2e}")

    # 四阶龙格-库塔法
    t_rk, y_rk = rk4(f, t0, y0, h, n_steps)
    print(f"\n【四阶 RK 法】t={t_end} 时 y={y_rk[-1]:.10f}")
    print(f"精确值: {y_exact(t_end):.10f}")
    print(f"误差: {abs(y_rk[-1] - y_exact(t_end)):.2e}")

    # 可视化
    t_fine = np.linspace(t0, t_end, 500)
    y_fine = y_exact(t_fine)
    plot_solutions(t_ie, y_ie, t_rk, y_rk, t_fine, y_fine)
    plot_step_size_effect(f, t0, y0, t_end, y_exact)


if __name__ == "__main__":
    main()
