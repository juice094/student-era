"""
实验三：函数插值与数值积分
核心算法：拉格朗日插值、牛顿插值、复合辛普生求积公式
"""

import os
import numpy as np

if os.environ.get('DISPLAY') is None and os.name != 'nt':
    import matplotlib
    matplotlib.use('Agg')
import matplotlib.pyplot as plt


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
        coeffs: 差商系数 [f[x0], f[x0,x1], ..., f[x0,...,xn]]
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
    coeffs = divided_differences(x_nodes, y_nodes)
    n = len(x_nodes)
    result = coeffs[-1]
    for i in range(n - 2, -1, -1):
        result = result * (x - x_nodes[i]) + coeffs[i]
    return result


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
    plt.savefig(f'../outputs/exp3_{method}.png', dpi=150)
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
    plt.savefig('../outputs/exp3_simpson_convergence.png', dpi=150)
    plt.show()
    print("Figure saved to ../outputs/exp3_simpson_convergence.png")


def main():
    print("=" * 50)
    print("实验三：函数插值与数值积分")
    print("=" * 50)

    # TODO: 根据教师给出的具体函数和节点修改这里
    # 示例：f(x) = 1 / (1 + 25*x^2)  （龙格函数）
    def f(x):
        return 1 / (1 + 25 * x**2)

    # 等距节点
    n = 10
    x_nodes = np.linspace(-1, 1, n + 1)
    y_nodes = f(x_nodes)

    # 插值
    print(f"\n【插值】节点数: {n+1}")
    print("拉格朗日插值与牛顿插值在理论上等价，数值实现略有差异")

    # 数值积分
    print("\n【复合辛普生求积】")
    a, b = -1, 1
    exact = np.arctan(5) * 2 / 5  # f(x)=1/(1+25x^2) 的精确积分
    for n in [4, 8, 16, 32]:
        approx = composite_simpson(f, a, b, n)
        err = abs(approx - exact)
        print(f"n={n:3d}: 近似值={approx:.10f}, 误差={err:.2e}")

    # 可视化
    plot_interpolation(f, x_nodes, y_nodes, method='lagrange')
    plot_simpson_convergence(f, a, b, exact)


if __name__ == "__main__":
    main()
