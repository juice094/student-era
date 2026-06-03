---
title: "vue-web-worker-lab — 项目信息"
date: 2026-05-31
type: project-info
---

# vue-web-worker-lab — Vue Web Worker 数学计算实验室

## 基本信息

| 属性 | 内容 |
|---|---|
| **课程** | 课程设计（2026 春） |
| **类型** | Project / Web Frontend + Worker |
| **技术栈** | Vue 3 + TypeScript + Vite + Web Worker |
| **GitHub** | [juice094/vue-web-worker-lab](https://github.com/juice094/vue-web-worker-lab) |
| **本地路径** | `C:\Users\22414\dev\vue-web-worker-lab` |

## 角色与贡献

**周景潇（juice094）— 项目协调 / 架构设计 / 技术文档 / Git 管理**

| 职责 | 内容 | 规模 |
|---|---|---|
| 项目初始化 | Vite + Vue 3 + TypeScript 脚手架搭建 | — |
| 架构文档 | Comprehensive README（14KB+），含架构说明、技术选型 rationale、目录结构 | 14 KB+ |
| Git 管理 | 合并冲突解决、分支策略维护（README 覆盖事件） | — |
| 代码审查 | 参与 V2.1/V2.1.2 review，审查并合并队友缩放逻辑优化 | — |

**队友张瑞坤（zrkjsnb）— 核心功能开发者**

| 模块 | 文件 | 规模 |
|---|---|---|
| 计算器 | CalculatorView.vue | — |
| 方程求解器 | SolverView.vue | 18.9 KB |
| 矩阵实验室 | MatrixLabView.vue | 11 KB |
| 数据绘图 | PlotterView.vue | 11.6 KB |
| 数据分析 | DataAnalysisView.vue | 16.6 KB |
| Web Worker 核心 | 5 个 Worker（solver/matrix/stats/plot/calc） | solver.worker.ts 21.3 KB |
| Composables | useWorker/useSolver/useMatrix/useStats | — |
| 组件层 | DataUploader/EquationInput/MatrixEditor/ParamForm/ResultPanel | — |

**队友周小超** — 参与 V2.1/V2.1.2 缩放逻辑优化。

## 提交统计

- 本人(juice094)：5/9 次（56%），主要为脚手架 + 文档 + Git 管理
- 张瑞坤(zrkjsnb)：3/9 次（33%），核心功能
- 总提交：9 次
- **本人代码贡献占比约 20%，核心功能由队友实现**

## 一键启动

```powershell
cd C:\Users\22414\dev\vue-web-worker-lab
npm run dev
```

或通过统一启动脚本：
```powershell
cd C:\Users\22414\dev\course-design-web-frontend
.\start-demo.ps1 -OnlyWorker
```
