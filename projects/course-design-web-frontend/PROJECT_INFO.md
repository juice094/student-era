---
title: "course-design-web-frontend — 项目信息"
date: 2026-05-31
type: project-info
---

# course-design-web-frontend — 学校主页 + 个人 Portal + 后台管理

## 基本信息

| 属性 | 内容 |
|---|---|
| **课程** | 课程设计（2026 春） |
| **类型** | Project / Web Frontend |
| **技术栈** | Vue 3 + TypeScript + Vite + Pinia + Element Plus + Lucide Icons + ECharts |
| **GitHub** | [juice094/course-design-web-frontend](https://github.com/juice094/course-design-web-frontend) |
| **本地路径** | `C:\Users\22414\dev\course-design-web-frontend` |

## 角色与贡献

**周景潇（juice094）— 个人 Portal 独立开发者 / 学校主页工程化整合者**

| 模块 | 规模 | 说明 |
|---|---|---|
| 模块 A：个人 Portal 系统 | 42KB+（PortalSettings.vue） | 拖拽布局管理器、网格系统、自适应缩放、编辑模式、持久化配置 |
| 模块 B：Canvas 特效渲染系统 | 自研 6 种粒子渲染器 | 弹幕/萤火虫/草地/樱花/雪花/密度控制器，统一渲染入口 |
| 模块 D：工程化整合 | 一键启动脚本 + 目录隔离 | 学校主页工程化重构、答辩演示适配 |

**学校主页（两位组员版本 + 本人工程化整合）**

| 版本 | 原始作者 | 本人工作 |
|---|---|---|
| 甘肃农业大学官网（HTML 版） | **yang-k123** | 工程化重构：单体 36KB HTML → CSS/JS/组件分离，撰写 README + MISSING.md |
| Web 技术大学（Vue 版） | **Moxn** | 工程化整合：从根目录提取并隔离到 `school-homepage/moxn/` 子目录，确保主项目零影响 |

**复用成果（非本次新建）**

- 教务后台管理模块（学生/教师/课程/成绩/选课）— 大数据可视化课程既有成果
- 统一权限与登录系统 — 复用成果
- CI/CD 配置（Dependabot + CodeQL）— 复用既有配置

**课程设计周期**：2026-05-26 至 2026-05-31（6 天）

**说明**：本仓库为课程设计期间工作仓库，包含既有复用成果。本次课程设计本人实际负责范围为**个人 Portal 系统全部 + 学校主页工程化整合**。

## 一键启动

```powershell
cd C:\Users\22414\dev\course-design-web-frontend
# 主项目
pnpm dev

# 学校主页 Moxn Vue 版（独立子项目）
cd school-homepage/moxn && npm run dev -- --port 5174

# 学校主页 HTML 版
cd school-homepage && npx serve --listen 5175 --single

# 统一启动全部服务（含 Canvas 游戏 + Web Worker）
.\start-demo.ps1
```

统一启动脚本 `start-demo.ps1` 同时启动 5 个演示服务：
1. `localhost:5173` — Web 前端主项目（Portal + 后台）
2. `localhost:5174` — 学校主页 Moxn Vue 版
3. `localhost:5175` — 学校主页 HTML 版
4. `localhost:5176` — Canvas 游戏（Hero Catch Monster）
5. `localhost:5177` — Vue Web Worker 数学实验室

支持参数：`--OnlyWeb`、`--OnlyGame`、`--OnlyWorker`
