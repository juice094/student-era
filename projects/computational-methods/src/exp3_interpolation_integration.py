"""
实验三：函数插值与数值积分
核心算法：拉格朗日插值、牛顿插值、复合辛普生求积公式
编写者：20231304002_周景潇 日期：2026/05/20
"""

import os
import numpy as np

if os.environ.get('DISPLAY') is None and os.name != 'nt':
    import matplotlib
    matplotlib.use('Agg')
try:
    import matplotlib.pyplot as plt
except ImportError:
    plt = None


def lagrange_interpolation(x_nodes, y_nodes, x):
    """
    拉格朗日插值多项式

    L_n(x) = sum_{i=0}^{n} y_i * l_i(x)
    其中 l_i(x) = prod_{j!=i} (x - x_j) / (x_i - x_j)
    """
    n = len(x_nodes)
    result = 0.0
    for i in range(n):
        li = 1.0
        for j in range(n):
            if j != i:
                li *= (x - x_nodes[j]) / (x_nodes[i] - x_nodes[j])
        result += y_nodes[i] * li
    return result


def divided_differences(x_nodes, y_nodes):
    """
    计算差商表

    Returns:
        coefficients: 差商系数 [f[x0], f[x0,x1], ..., f[x0,...,xn]]
    """
    n = len(x_nodes)
    table = np.zeros((n, n))
    table[:, 0] = y_nodes

    for j in range(1, n):
        for i in range(n - j):
            table[i, j] = (table[i + 1, j - 1] - table[i, j - 1]) / (x_nodes[i + j] - x_nodes[i])

    return table[0, :]


def newton_interpolation(x_nodes, y_nodes, x):
    """
    牛顿插值多项式（基于差商）

    N_n(x) = f[x0] + f[x0,x1](x-x0) + ... + f[x0,...,xn](x-x0)...(x-x_{n-1})
    """
    coefficients = divided_differences(x_nodes, y_nodes)
    n = len(x_nodes)
    result = coefficients[-1]
    for i in range(n - 2, -1, -1):
        result = result * (x - x_nodes[i]) + coefficients[i]
    return result


def composite_trapezoidal(f, a, b, n):
    """
    复合梯形求积公式

    公式：T_n = h/2 * [f(a) + 2*sum_{i=1}^{n-1} f(x_i) + f(b)]
    其中 h = (b - a) / n, x_i = a + i*h
    """
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)

    T = y[0] + y[-1]
    T += 2 * np.sum(y[1:-1])

    return T * h / 2


def composite_simpson(f, a, b, n):
    """
    复合辛普生求积公式

    要求 n 为偶数
    公式：S_n = h/3 * [f(a) + 4*sum_{奇数} f(x_i) + 2*sum_{偶数} f(x_i) + f(b)]
    """
    if n % 2 != 0:
        raise ValueError("n must be even for Simpson's rule")

    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)

    S = y[0] + y[-1]
    S += 4 * np.sum(y[1:-1:2])
    S += 2 * np.sum(y[2:-1:2])

    return S * h / 3


def plot_interpolation(f, x_nodes, y_nodes, method='lagrange'):
    """绘制插值效果，对比龙格现象"""
    x_fine = np.linspace(min(x_nodes) - 0.5, max(x_nodes) + 0.5, 500)
    y_true = f(x_fine)

    if method == 'lagrange':
        y_interp = [lagrange_interpolation(x_nodes, y_nodes, xi) for xi in x_fine]
        title = 'Lagrange Interpolation'
    else:
        y_interp = [newton_interpolation(x_nodes, y_nodes, xi) for xi in x_fine]
        title = 'Newton Interpolation'

    plt.figure(figsize=(10, 5))
    plt.plot(x_fine, y_true, 'k-', label='Original f(x)', linewidth=1.5)
    plt.plot(x_fine, y_interp, 'r--', label=title, linewidth=1.5)
    plt.scatter(x_nodes, y_nodes, color='blue', zorder=5, label='Nodes')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'{title} (n={len(x_nodes)-1})')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    # ensure output directory exists
    outdir = os.path.join(os.path.dirname(__file__), '..', 'outputs')
    os.makedirs(outdir, exist_ok=True)
    plt.savefig(os.path.join(outdir, f'exp3_{method}.png'), dpi=150)
    plt.show()
    print(f"Figure saved to ../outputs/exp3_{method}.png")


def plot_simpson_convergence(f, a, b, exact_value):
    """绘制复合辛普生公式的收敛过程"""
    n_values = [2, 4, 8, 16, 32, 64, 128, 256]
    errors = []

    for n in n_values:
        approx = composite_simpson(f, a, b, n)
        errors.append(abs(approx - exact_value))

    plt.figure(figsize=(8, 5))
    plt.loglog(n_values, errors, 'o-', markersize=6)
    plt.xlabel('n (number of subintervals)')
    plt.ylabel('Absolute Error')
    plt.title("Composite Simpson's Rule Convergence")
    plt.grid(True, which='both', linestyle='--', alpha=0.6)
    plt.tight_layout()
    # ensure output directory exists
    outdir = os.path.join(os.path.dirname(__file__), '..', 'outputs')
    os.makedirs(outdir, exist_ok=True)
    plt.savefig(os.path.join(outdir, 'exp3_simpson_convergence.png'), dpi=150)
    plt.show()
    print("Figure saved to ../outputs/exp3_simpson_convergence.png")


def main():
    print("=" * 60)
    print("实验三：函数插值与数值积分")
    print("=" * 60)

    # ==================== 例 7.8.1 拉格朗日插值 ====================
    print("\n【例 7.8.1 拉格朗日插值】")
    print("已知: x₀=[100, 121, 144], y₀=[10, 11, 12]")
    print("求:  f(115)")
    x_nodes_781 = np.array([100, 121, 144], dtype=float)
    y_nodes_781 = np.array([10, 11, 12], dtype=float)
    x_target = 115.0

    result_lagrange = lagrange_interpolation(x_nodes_781, y_nodes_781, x_target)
    exact_sqrt115 = np.sqrt(115)
    print(f"\n拉格朗日插值结果: L₂(115) = {result_lagrange:.14f}")
    print(f"精确值 (√115)   = {exact_sqrt115:.14f}")
    print(f"绝对误差        = {abs(result_lagrange - exact_sqrt115):.2e}")

    # ==================== 例 7.8.1 牛顿插值对比 ====================
    result_newton = newton_interpolation(x_nodes_781, y_nodes_781, x_target)
    print(f"\n牛顿插值结果:    N₂(115) = {result_newton:.14f}")
    print(f"绝对误差        = {abs(result_newton - exact_sqrt115):.2e}")
    print("结论: 拉格朗日与牛顿插值理论上等价，数值结果一致")

    # ==================== 例 8.6.1 复合梯形求积 ====================
    print("\n" + "=" * 60)
    print("【例 8.6.1 复合梯形求积】")
    print("积分: ∫₁⁸ sin(x)/x dx,  n = 8")

    def f_integral(x):
        return np.sin(x) / x

    a1, b1, n1 = 1.0, 8.0, 8
    # 精确值: Si(8) - Si(1), 其中 Si(x) = ∫₀ˣ sin(t)/t dt
    try:
        from scipy.special import sici
        exact_861 = sici(b1)[0] - sici(a1)[0]
    except ImportError:
        # fallback: 高精度辛普森近似
        exact_861 = composite_simpson(f_integral, a1, b1, 100000)

    trapz_861 = composite_trapezoidal(f_integral, a1, b1, n1)
    print(f"\n复合梯形 (n=8):  {trapz_861:.10f}")
    print(f"参考精确值:       {exact_861:.10f}")
    print(f"绝对误差:         {abs(trapz_861 - exact_861):.2e}")

    # ==================== 例 8.6.2 复合辛普森求积 ====================
    print("\n" + "=" * 60)
    print("【例 8.6.2 复合辛普森求积】")
    print("积分: ∫₁⁴ sin(x)/x dx,  n = 4")

    a2, b2, n2 = 1.0, 4.0, 4
    try:
        exact_862 = sici(b2)[0] - sici(a2)[0]
    except ImportError:
        exact_862 = composite_simpson(f_integral, a2, b2, 100000)

    simpson_862 = composite_simpson(f_integral, a2, b2, n2)
    print(f"\n复合辛普森 (n=4): {simpson_862:.10f}")
    print(f"参考精确值:        {exact_862:.10f}")
    print(f"绝对误差:          {abs(simpson_862 - exact_862):.2e}")

    # ==================== 方法对比 ====================
    print("\n" + "=" * 60)
    print("【方法对比】")
    print("=" * 60)

    # 对同一积分用不同方法对比
    a_test, b_test = 1.0, 4.0
    n_values = [4, 8, 16, 32]
    try:
        exact_test = sici(b_test)[0] - sici(a_test)[0]
    except ImportError:
        exact_test = composite_simpson(f_integral, a_test, b_test, 100000)

    print(f"\n积分: ∫₁⁴ sin(x)/x dx, 精确值 ≈ {exact_test:.10f}")
    print(f"{'n':>4} | {'复合梯形':>14} | {'误差(梯形)':>12} | {'复合辛普森':>14} | {'误差(辛普森)':>12}")
    print("-" * 72)
    for n in n_values:
        t = composite_trapezoidal(f_integral, a_test, b_test, n)
        s = composite_simpson(f_integral, a_test, b_test, n)
        err_t = abs(t - exact_test)
        err_s = abs(s - exact_test)
        print(f"{n:4d} | {t:14.10f} | {err_t:12.2e} | {s:14.10f} | {err_s:12.2e}")

    print("\n结论:")
    print("  1. 辛普森公式精度显著高于同 n 的梯形公式（O(h⁴) vs O(h²)）")
    print("  2. 梯形公式对奇数/偶数 n 无限制，辛普森要求 n 为偶数")

    # ==================== 原有示例（龙格函数）====================
    print("\n" + "=" * 60)
    print("【附加示例：龙格函数插值与积分】")
    print("=" * 60)

    def f_runge(x):
        return 1 / (1 + 25 * x**2)

    n = 10
    x_nodes = np.linspace(-1, 1, n + 1)
    y_nodes = f_runge(x_nodes)

    a, b = -1, 1
    exact_runge = np.arctan(5) * 2 / 5
    for n in [4, 8, 16, 32]:
        approx = composite_simpson(f_runge, a, b, n)
        err = abs(approx - exact_runge)
        print(f"n={n:3d}: 近似值={approx:.10f}, 误差={err:.2e}")

    # 可视化（仅在 matplotlib 可用时）
    if plt is not None:
        plot_interpolation(f_runge, x_nodes, y_nodes, method='lagrange')
        plot_simpson_convergence(f_runge, a, b, exact_runge)
    else:
        print("\n[matplotlib 不可用，跳过绘图]")


if __name__ == "__main__":
    main()
