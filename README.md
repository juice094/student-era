# Student Era — 学生时代课程设计归档

[![Vue 3](https://img.shields.io/badge/Vue-3.4-4FC08D?logo=vuedotjs)](https://vuejs.org/)
[![Vite](https://img.shields.io/badge/Vite-5.0-646CFF?logo=vite)](https://vitejs.dev/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.4-3178C6?logo=typescript)](https://www.typescriptlang.org/)
[![ECharts](https://img.shields.io/badge/ECharts-5.0-AA344D?logo=apacheecharts)](https://echarts.apache.org/)
[![Element Plus](https://img.shields.io/badge/Element%20Plus-2.9-409EFF)](https://element-plus.org/)

> A curated archive of student-era course designs and classroom demos. Covers data visualization, agricultural IT, and cyber security — from Vue 3 dashboards to pure HTML5 prototypes.

**Featured Projects**
- [`projects/bigdata-visualization`](./projects/bigdata-visualization) — Academic admin dashboard with Vue 3, Vite, TypeScript, ECharts. Features data visualization, complete CRUD, form validation, undo-delete, and enterprise-level engineering practices.
- [`projects/ml-apple-detection`](./projects/ml-apple-detection) — 8-class apple quality classification using PyTorch and ResNet18. Includes data exploration, training pipeline with TensorBoard, and inference scripts.
- [`projects/network-security`](./projects/network-security) — Network information security experiments on Kali Linux WSL2. Covers info collection, password cracking, DoS attack demo, and system hardening.
- [`projects/gis-remote-sensing`](./projects/gis-remote-sensing) — Remote sensing image processing with ERDAS 9.2: RGB-IHS conversion, resolution merge, and convolution enhancement.
- [`projects/gis-supermap`](./projects/gis-supermap) — Map production with SuperMap iDesktop 10: data query, buffer analysis, overlay analysis, and thematic mapping.
- [`projects/gis-lab-navigator`](./projects/gis-lab-navigator) — Web navigation portal for GIS experiments with quick links to software downloads, docs, and tutorials.
- [`projects/computational-methods`](./projects/computational-methods) — Numerical computing experiments (root finding, linear systems, interpolation/integration, ODE solvers) in Python + NumPy + Matplotlib, replacing MATLAB R2019b.
- [`demos/agri-kg-demo`](./demos/agri-kg-demo) — Agricultural knowledge graph visualization.
- [`demos/cyber-security-webui`](./demos/cyber-security-webui) — Cyber security Web UI demo with PWA support.

## Project Index

| Semester | Course | Type | Path | Tech Stack |
|----------|--------|------|------|------------|
| 2026 Spring | Big Data Visualization | Project | [`projects/bigdata-visualization`](./projects/bigdata-visualization) | Vue 3 + TypeScript + ECharts + Element Plus |
| 2026 Spring | Machine Learning | Project | [`projects/ml-apple-detection`](./projects/ml-apple-detection) | PyTorch + ResNet18 + OpenCV |
| 2026 Spring | Network Information Security | Project | [`projects/network-security`](./projects/network-security) | Kali Linux + nmap + John the Ripper |
| 2026 Spring | Remote Sensing Image Processing | Project | [`projects/gis-remote-sensing`](./projects/gis-remote-sensing) | ERDAS 9.2 |
| 2026 Spring | GIS Map Production | Project | [`projects/gis-supermap`](./projects/gis-supermap) | SuperMap iDesktop 10 |
| 2026 Spring | GIS Lab Navigator | Project | [`projects/gis-lab-navigator`](./projects/gis-lab-navigator) | HTML5 + CSS3 |
| 2026 Spring | Computational Methods | Project | [`projects/computational-methods`](./projects/computational-methods) | Python + NumPy + SciPy + Matplotlib |
| 2026 Spring | Agricultural Information Technology | Demo | [`demos/agri-kg-demo`](./demos/agri-kg-demo) | HTML5 + CSS3 + Vanilla JS |
| 2026 Spring | Cyber Security | Demo | [`demos/cyber-security-webui`](./demos/cyber-security-webui) | HTML5 + CSS3 + Vanilla JS + PWA |

## Quick Start

```bash
# Install root dependencies
pnpm install

# Start the bigdata-visualization project
pnpm dev:visualization

# Build for production
pnpm build:visualization
```

## Repository Structure

```
.
├── packages/                   # Shared packages (future extensions)
├── projects/                   # Build-required course design projects
│   ├── bigdata-visualization/  # Academic admin dashboard with data viz
│   │   ├── src/
│   │   ├── docs/               # Course design reports
│   │   └── dist/               # Build output
│   ├── ml-apple-detection/     # Apple quality classification (PyTorch)
│   │   ├── data/               # Training and test datasets
│   │   ├── src/                # train.py, predict.py
│   │   ├── notebooks/          # Jupyter exploration
│   │   └── models/             # Saved checkpoints
│   ├── network-security/       # Network security experiments
│   │   ├── scripts/            # Experiment shell scripts
│   │   ├── exp1-info-collection/
│   │   ├── exp2-password-cracking/
│   │   ├── exp3-dos-attack/
│   │   └── exp4-system-hardening/
│   ├── gis-remote-sensing/     # Remote sensing image processing (ERDAS 9.2)
│   │   ├── data/               # water.img / 1.img
│   │   └── README.md           # Experiment guide
│   ├── gis-supermap/           # Map production (SuperMap iDesktop 10)
│   │   └── README.md           # Experiment guide
│   ├── gis-lab-navigator/      # Web portal for GIS experiment links
│   │   └── index.html          # Navigation page
│   └── computational-methods/  # Numerical computing (Python replaces MATLAB)
│       ├── src/                # exp1-4.py
│       ├── outputs/            # Figures and results
│       ├── .vscode/            # VS Code workspace config
│       └── README.md           # Experiment guide
├── demos/                      # Static classroom demos (open index.html directly)
│   ├── agri-kg-demo/           # Agricultural knowledge graph visualization
│   └── cyber-security-webui/   # Cyber security Web UI demo
├── docs/                       # Course design reports archive
│   ├── 大数据可视化/
│   ├── 农业信息技术/
│   ├── 网络安全/
│   └── ENVIRONMENT.md          # Environment setup reference
├── package.json                # Workspace root
└── pnpm-workspace.yaml
```

## Topics

`visualization` `education` `engineering` `crud` `typescript` `dashboard` `frontend` `echarts` `admin-system` `vue3` `vite` `element-plus` `pinia`
