# Student Era — 学生时代课程设计归档

[![Vue 3](https://img.shields.io/badge/Vue-3.4-4FC08D?logo=vuedotjs)](https://vuejs.org/)
[![Vite](https://img.shields.io/badge/Vite-5.0-646CFF?logo=vite)](https://vitejs.dev/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.4-3178C6?logo=typescript)](https://www.typescriptlang.org/)
[![ECharts](https://img.shields.io/badge/ECharts-5.0-AA344D?logo=apacheecharts)](https://echarts.apache.org/)
[![Element Plus](https://img.shields.io/badge/Element%20Plus-2.9-409EFF)](https://element-plus.org/)

> A production-ready academic administration dashboard built with Vue 3, Vite, TypeScript, and ECharts. Features data visualization, complete student CRUD operations, form validation, undo-delete, and enterprise-level engineering practices.

This repository archives various course design projects and classroom demos from my student years.

## Project Index

| Semester | Course | Type | Path | Tech Stack |
|----------|--------|------|------|------------|
| 2026 Spring | Big Data Visualization | Project | [`projects/bigdata-visualization`](./projects/bigdata-visualization) | Vue 3 + TypeScript + ECharts + Element Plus |
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
│   └── bigdata-visualization/  # Academic admin dashboard with data viz
│       ├── src/
│       ├── docs/               # Course design reports
│       └── dist/               # Build output
├── demos/                      # Static classroom demos (open index.html directly)
│   ├── agri-kg-demo/           # Agricultural knowledge graph visualization
│   └── cyber-security-webui/   # Cyber security Web UI demo
├── docs/                       # Course design reports archive
│   ├── 大数据可视化/
│   ├── 农业信息技术/
│   └── 网络安全/
├── package.json                # Workspace root
└── pnpm-workspace.yaml
```

## Topics

`visualization` `education` `engineering` `crud` `typescript` `dashboard` `frontend` `echarts` `admin-system` `vue3` `vite` `element-plus` `pinia`
