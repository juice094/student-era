# Student Era — 学生时代课程设计归档

[![Vue 3](https://img.shields.io/badge/Vue-3.4-4FC08D?logo=vuedotjs)](https://vuejs.org/)
[![Vite](https://img.shields.io/badge/Vite-5.0-646CFF?logo=vite)](https://vitejs.dev/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.4-3178C6?logo=typescript)](https://www.typescriptlang.org/)
[![Python](https://img.shields.io/badge/Python-3.13-3776AB?logo=python)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.12-EE4C2C?logo=pytorch)](https://pytorch.org/)
[![WSL2](https://img.shields.io/badge/WSL2-Ubuntu%2FKali-4EAA25?logo=linux)](https://docs.microsoft.com/windows/wsl/)

> Student-era course design archive — Vue 3 + ECharts dashboards, PyTorch computer vision, Hadoop/Spark/Kafka big data stack, GIS/remote sensing, numerical methods, network security, and information retrieval. Built on WSL2.

## 项目索引

| 学期 | 课程 | 类型 | 路径 | 技术栈 |
|------|------|------|------|--------|
| 2026 Spring | 大数据可视化 | Project | [`projects/bigdata-visualization`](./projects/bigdata-visualization) | Vue 3 + TypeScript + ECharts |
| 2026 Spring | 机器学习 | Project | [`projects/ml-apple-detection`](./projects/ml-apple-detection) | PyTorch + ResNet18 + OpenCV |
| 2026 Spring | 网络信息安全 | Project | [`projects/network-security`](./projects/network-security) | Kali Linux + nmap + John |
| 2026 Spring | 遥感图像处理 | Project | [`projects/gis-remote-sensing`](./projects/gis-remote-sensing) | ERDAS 9.2 |
| 2026 Spring | GIS地图制作 | Project | [`projects/gis-supermap`](./projects/gis-supermap) | SuperMap iDesktop 10 |
| 2026 Spring | 计算方法 | Project | [`projects/computational-methods`](./projects/computational-methods) | Python + NumPy + Matplotlib |
| 2026 Spring | 信息检索与搜索引擎 | Project | [`projects/information-retrieval`](./projects/information-retrieval) | HTML5 导航站 |
| 2026 Spring | 农业信息技术 | Demo | [`demos/agri-kg-demo`](./demos/agri-kg-demo) | HTML5 + CSS3 |
| 2026 Spring | 网络安全 | Demo | [`demos/cyber-security-webui`](./demos/cyber-security-webui) | HTML5 + CSS3 + PWA |

## 环境概览

| 环境 | 发行版 | 核心组件 | 状态 |
|------|--------|----------|------|
| 大数据 / ML | Ubuntu-24.04 WSL2 | Hadoop 3.4, Spark 4.1, Kafka 4.2(KRaft), PyTorch 2.12 | [VERIFIED] |
| 网络安全 | kali-linux WSL2 | nmap, john, hping3, dnsutils | [VERIFIED] |

详见 [`docs/ENVIRONMENT.md`](./docs/ENVIRONMENT.md)。

## 项目展示主页

直接浏览器打开根目录 [`index.html`](./index.html) 查看所有课程项目的统一展示门户。

## 共享基础设施

| 包名 | 路径 | 说明 |
|------|------|------|
| `@student-era/theme` | `packages/@student-era/theme/` | 暗色主题 CSS 设计系统（提取自导航站） |
| `@student-era/echarts-config` | `packages/@student-era/echarts-config/` | ECharts 最小注册配置（按需加载） |
| `@student-era/vue-utils` | `packages/@student-era/vue-utils/` | Vue 3 组件（ChartPanel, DataCard）与工具库 |

## 快速开始

### 前端项目
```bash
pnpm install
pnpm dev:visualization    # 大数据可视化
pnpm build:visualization
```

### 计算方法实验（WSL Ubuntu-24.04）
```bash
cd projects/computational-methods/src
python exp1_root_finding.py
python exp2_linear_systems.py
python exp3_interpolation_integration.py
python exp4_ode_solver.py
```

### ML 实验（WSL Ubuntu-24.04）
```bash
cd projects/ml-apple-detection/src
python train.py --epochs 50 --batch-size 8 --lr 0.001
tensorboard --logdir=../outputs/runs
```

### 网络安全实验（WSL kali-linux）
```bash
cd /home/zjx/netsec-exp/scripts
bash exp1-info-collection.sh
bash exp2-password-cracking.sh
```

### GIS 导航站
直接浏览器打开：
- [`projects/gis-lab-navigator/index.html`](./projects/gis-lab-navigator/index.html)
- [`projects/information-retrieval/index.html`](./projects/information-retrieval/index.html)

## 仓库结构

```
.
├── index.html                  # 项目展示主页（根门户）
├── packages/                   # 共享基础设施（pnpm workspace）
│   └── @student-era/
│       ├── theme/              # 暗色主题 CSS 设计系统
│       ├── echarts-config/     # ECharts 最小注册配置
│       └── vue-utils/          # Vue 3 组件与工具库
├── projects/                   # 课程设计项目
│   ├── bigdata-visualization/  # Vue 3 数据可视化仪表盘
│   ├── ml-apple-detection/     # PyTorch 苹果质量分类
│   ├── network-security/       # Kali 网络安全实验脚本
│   ├── gis-remote-sensing/     # ERDAS 遥感图像处理
│   ├── gis-supermap/           # SuperMap 地图制作
│   ├── gis-lab-navigator/      # GIS 实验导航站
│   ├── computational-methods/  # Python 数值计算实验
│   └── information-retrieval/  # 信息检索实验导航站
├── demos/                      # 静态课堂演示
│   ├── agri-kg-demo/
│   └── cyber-security-webui/
├── docs/                       # 课程资料归档
│   ├── ENVIRONMENT.md          # 环境配置速查
│   ├── STATUS-2026-05-18.md    # 项目状态与 TODO
│   ├── ARCHITECTURE-REVIEW-2026-05-18.md  # 架构审视
│   ├── 课程资料索引.md         # 复习资料目录
│   ├── 大数据可视化/
│   ├── 农业信息技术/
│   └── 网络安全/
├── .github/workflows/          # GitHub Actions CI
├── .gitattributes              # Git LFS 配置
└── README.md                   # 本文件
```

## 今日工作摘要（2026-05-18）

1. **大数据环境升级** — Spark 4.1.1 / Flink 2.2.1 / Kafka 4.2.0 KRaft / ZooKeeper 3.9.3 / HBase 2.6.2 / Hive 4.2.0
2. **ML 环境配置** — Python 3.13 + PyTorch 2.12 + OpenCV + Matplotlib + TensorBoard + JupyterLab
3. **计算方法实验** — 4 个 Python 脚本替代 MATLAB R2019b，匹配教材例题
4. **GIS 实验** — ERDAS + SuperMap 操作说明 + 导航站
5. **信息检索实验** — 4 个实验模块导航站
6. **复习资料归档** — 大数据可视化 + 农业信息技术期末资料（Git LFS）
7. **架构审视报告** — 仓库优化建议与 Agent 协作方案
8. **共享基础设施提取** — 暗色主题 CSS + ECharts 配置 + Vue 组件库（pnpm workspace）
9. **根目录展示页** — 统一项目门户 `index.html`
10. **CI 工作流** — GitHub Actions 三阶段验证通过
11. **Release v1.0.0** — 2026 Spring 课程归档发布
12. **实验指导书归档** — 计算方法 + 信息检索原始文档入库
13. **仓库门面更新** — README 描述/Topics 同步 GitHub About，根目录 `index.html` 内容刷新

## Topics

`visualization` `engineering` `typescript` `dashboard` `frontend` `echarts` `student-projects` `course-design` `admin-system` `vue3` `vite` `element-plus` `pinia` `machine-learning` `pytorch` `bigdata` `hadoop` `spark` `numpy` `gis`
