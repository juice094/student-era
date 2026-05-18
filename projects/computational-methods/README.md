# 计算方法实验

> 基于 Python + NumPy/SciPy/Matplotlib 的数值计算实验，对应《计算方法》课程四个核心模块。
> 原课程要求 MATLAB R2019b，本项目使用 Python 科学计算栈实现等价功能。

## 实验环境

| 组件 | 版本 | 用途 |
|------|------|------|
| Python | 3.13.13 | 编程语言 |
| NumPy | 2.4.4 | 矩阵运算、数值计算 |
| SciPy | 1.17.1 | 科学计算库 |
| Matplotlib | 3.10.9 | 数据可视化 |

## 实验清单

| 实验 | 主题 | 核心算法 | 文件 |
|------|------|----------|------|
| 实验一 | 方程求根 | 二分法、牛顿迭代法 | `src/exp1_root_finding.py` |
| 实验二 | 线性方程组求解 | 列主元高斯消去法、雅可比/高斯-塞德尔迭代法 | `src/exp2_linear_systems.py` |
| 实验三 | 函数插值与数值积分 | 拉格朗日/牛顿插值、复合辛普生求积 | `src/exp3_interpolation_integration.py` |
| 实验四 | 常微分方程初值问题 | 改进欧拉法、四阶龙格-库塔法 | `src/exp4_ode_solver.py` |

## 快速开始

```bash
cd ~/dev/student-era/projects/computational-methods/src

# 实验一
python exp1_root_finding.py

# 实验二
python exp2_linear_systems.py

# 实验三
python exp3_interpolation_integration.py

# 实验四
python exp4_ode_solver.py
```

## 目录结构

```
.
├── src/                          # 实验源码
│   ├── exp1_root_finding.py      # 实验一：方程求根
│   ├── exp2_linear_systems.py    # 实验二：线性方程组
│   ├── exp3_interpolation_integration.py  # 实验三：插值与积分
│   └── exp4_ode_solver.py        # 实验四：ODE 初值问题
├── outputs/                      # 实验输出（图表、结果）
├── docs/                         # 实验报告与补充文档
└── README.md                     # 本文件
```

## 实验报告要求

每个实验报告应包含：
1. 实验目的与原理
2. 程序代码与关键注释
3. 实验结果（数值结果 + 可视化图表）
4. 结果分析与总结（误差分析、方法对比）
