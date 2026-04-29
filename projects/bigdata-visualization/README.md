# Big Data Visualization — 教务可视化系统

> 大数据可视化课程设计项目：基于 Vue 3 + ECharts 的教务管理前端系统。

## 功能特性

- **数据可视化大屏**：柱状图（院系人数）、饼图（性别比例 / 课程类型）、折线图（招生趋势）
- **完整 CRUD**：学生管理、教师管理、课程管理、成绩管理、选课管理
- **权限控制**：基于角色的菜单与按钮级权限
- **工程化实践**：Pinia 状态管理、Vue Router 导航守卫、组合式函数封装、TypeScript 全栈类型安全

## 技术栈

- Vue 3 + TypeScript + Vite
- Element Plus + Element Plus Icons
- ECharts 5（按需引入渲染器与图表类型）
- Pinia（持久化存储）
- Vue Router 4

## 快速启动

```bash
pnpm install
pnpm dev
```

## 构建部署

```bash
pnpm build
```

构建产物输出至 `dist/` 目录，已配置 GitHub Pages 自动部署（`.github/workflows/deploy.yml`）。
