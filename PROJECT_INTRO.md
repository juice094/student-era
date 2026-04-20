# 教务数据可视化管理系统 — 项目说明文档

> **课程名称**：《大数据可视化》课程设计  
> **技术栈**：Vue 3.5 + Vite 6 + TypeScript 5.7 + Pinia 3 + Vue Router 4 + Element Plus 2.13 + ECharts 5.6  
> **版本**：v2.0.0

---

## 一、项目概述

本项目是一个面向高校的**教务数据可视化管理系统**，采用 Vue 3 生态全家桶构建。系统覆盖教务管理的核心业务流程，包括学生/教师/课程/成绩的基础 CRUD、学生选课、课程排课、教学评价、操作审计以及数据可视化大屏展示。

相较于传统基于 Vue 2 + Vue CLI + Vuex 的教务系统，本项目在构建速度、类型安全、代码组织、图表性能等方面进行了全面升级。

---

## 二、技术架构

### 2.1 核心依赖

| 依赖 | 版本 | 用途 |
|------|------|------|
| Vue | 3.5.13 | 渐进式前端框架，Composition API |
| Vite | 6.3.2 | 下一代前端构建工具，ESM 原生支持 |
| TypeScript | 5.7.3 | 静态类型检查，全链路类型安全 |
| Pinia | 3.0.1 | 状态管理，直接修改、DevTools 友好 |
| Vue Router | 4.5.0 | 单页路由，Hash 模式，路由守卫 |
| Element Plus | 2.9.7 | UI 组件库，企业级后台界面 |
| ECharts | 5.6.0 | 数据可视化图表库 |
| vue-echarts | 7.0.3 | ECharts 的 Vue 声明式封装 |
| xlsx | 0.18.5 | Excel 文件读写（导入/导出） |
| Axios | 1.8.4 | HTTP 客户端（预留后端对接） |

### 2.2 架构分层

```
┌─────────────────────────────────────────────┐
│              用户层 (User Layer)              │
│   管理员(admin)  教师(teacher)  学生(student)  │
└──────────────────┬──────────────────────────┘
                   │
┌──────────────────▼──────────────────────────┐
│            视图层 (View Layer)               │
│  Login │ Home │ Student │ Teacher │ Course   │
│  Score │ CourseSelect │ Schedule │ Evaluation│
│  OperationLog │ About                          │
└──────────────────┬──────────────────────────┘
                   │
┌──────────────────▼──────────────────────────┐
│          组件层 (Component Layer)            │
│  AppLayout │ ChartPanel │ DataCard           │
│  Breadcrumb │ StudentFormDialog              │
└──────────────────┬──────────────────────────┘
                   │
┌──────────────────▼──────────────────────────┐
│          状态层 (Pinia Store Layer)          │
│  user │ student │ teacher │ course │ score   │
│  courseSelect │ log │ dict                   │
└──────────────────┬──────────────────────────┘
                   │
┌──────────────────▼──────────────────────────┐
│           工具层 (Utility Layer)             │
│  auth │ permission │ export │ format         │
│  request (Axios + interceptors)              │
└─────────────────────────────────────────────┘
```

### 2.3 构建产物分块策略

```
assets/
├── index-xxx.js              (11.5 kB)    业务入口 + Router
├── vue-vendor-xxx.js         (109 kB)     Vue + Router + Pinia
├── ui-vendor-xxx.js          (1,033 kB)   Element Plus
├── echarts-vendor-xxx.js     (526 kB)     ECharts + vue-echarts
├── export-xxx.js             (425 kB)     xlsx 库（按需加载）
├── student-xxx.js            (39 kB)      StudentView 懒加载 chunk
└── [view]-xxx.js             (2~11 kB)    其他视图懒加载 chunk
```

> `ui-vendor` 体积较大是因为 Element Plus 全量组件的 gzipped 体积约 326 KB，在可接受范围内。如需进一步优化，可改用 `unplugin-element-plus` 按需引入。

---

## 三、功能模块

### 3.1 基础功能（Phase 1）

| 模块 | 说明 |
|------|------|
| 登录认证 | JWT Token + LocalStorage 持久化，支持 3 种角色登录 |
| RBAC 权限 | 菜单级过滤（`checkMenu`）+ 按钮级指令（`v-permission`） |
| 动态菜单 | 侧边栏根据角色自动渲染，支持折叠/展开 |
| 字典管理 | 学院、专业、年级、性别、课程类型、学期等基础数据 |
| 布局框架 | 侧边栏 + 顶部 Header（面包屑 + 用户下拉）+ 内容区 |

### 3.2 核心业务（Phase 2）

| 模块 | 核心能力 |
|------|---------|
| 学生管理 | 新增/编辑/删除，删除后 8 秒内可撤销，成绩/专业分布图表 |
| 教师管理 | 教师信息 CRUD，与课程系统关联 |
| 课程管理 | 课程信息维护，绑定授课教师和开课学院 |
| 成绩管理 | 成绩录入（平时/期中/期末），权重动态配置，自动计算总评与 GPA，成绩分布 + 绩点饼图 |

### 3.3 高级业务（Phase 3）

| 模块 | 核心能力 |
|------|---------|
| 学生选课 | 可选课程列表展示（容量进度条），学分上限 30 分控制，一键选课/退课 |
| 排课管理 | 教室/时间段/周次安排，自动检测教室冲突和教师冲突 |
| 学生评教 | 五维评分（教学态度/内容/方法/互动/效果），参评率统计，学生留言精选 |

### 3.4 运维运营（Phase 4）

| 模块 | 核心能力 |
|------|---------|
| 审计日志 | 记录用户操作时间/人/模块/动作/状态/IP，支持多维度筛选 |
| Excel 导出 | 学生/课程/成绩数据一键导出 `.xlsx` |
| Excel 导入 | 学生/课程数据通过 Excel 批量导入 |
| 数据大屏 | 首页 Dashboard：KPI 卡片 + 院系分布 + 性别比例 + 成绩分布 + 课程类型占比 + 招生趋势 |

---

## 四、数据可视化实现

### 4.1 ECharts 5 集成方案

ECharts 5 采用**显式注册**模式，必须在 `init()` 前注册渲染器和组件：

```typescript
// main.ts
import { use } from 'echarts/core'
import { CanvasRenderer } from 'echarts/renderers'
import { BarChart, PieChart, LineChart } from 'echarts/charts'
import { GridComponent, TooltipComponent, LegendComponent, TitleComponent } from 'echarts/components'

use([CanvasRenderer, BarChart, PieChart, LineChart, GridComponent, TooltipComponent, LegendComponent, TitleComponent])
```

> ⚠️ 若未显式注册，`echarts.init()` 会**静默失败**，导致图表区域空白且 Vue 渲染被阻塞。这是从 ECharts 4 升级至 5 最常见的坑点。

### 4.2 图表组件封装

使用 `vue-echarts` 替代原生命令式 API：

```vue
<template>
  <v-chart class="chart-panel" :option="option" autoresize />
</template>
```

优势：
- 自动处理 `init` / `resize` / `dispose` 生命周期
- `autoresize` 属性自动响应容器尺寸变化
- 声明式 `option` 绑定，数据变化自动更新

### 4.3 已实现的图表

| 图表 | 类型 | 位置 | 数据源 |
|------|------|------|--------|
| 各院系学生人数分布 | 柱状图 | HomeView | Mock 数据 |
| 学生性别比例 | 饼图 | HomeView | Store 动态计算 |
| 近五年招生趋势 | 折线图（面积） | HomeView | Mock 数据 |
| 成绩分段分布 | 柱状图（多色） | StudentView / ScoreView | Store 动态计算 |
| 专业人数占比 | 饼图 | StudentView | Mock 数据 |
| 绩点分布 | 环形图 | ScoreView | Store 动态计算 |
| 课程类型占比 | 饼图 | HomeView | Store 动态计算 |

---

## 五、权限控制设计

### 5.1 菜单权限

```typescript
// permission.ts
export const MENU_PERMISSIONS: Record<UserRole, string[]> = {
  admin:   ['Home', 'Student', 'Teacher', 'Course', 'Score', 'CourseSelect', 'Schedule', 'Evaluation', 'OperationLog', 'About'],
  teacher: ['Home', 'Student', 'Teacher', 'Course', 'Score', 'Evaluation', 'About'],
  student: ['Home', 'Course', 'Score', 'CourseSelect', 'Evaluation', 'About']
}
```

### 5.2 按钮权限

使用自定义指令 `v-permission` 控制按钮显隐：

```vue
<el-button v-permission="'student:add'">新增学生</el-button>
```

指令内部读取当前用户角色，匹配 `BUTTON_PERMISSIONS` 配置，无权限时自动移除 DOM 元素。

### 5.3 路由守卫

```typescript
router.beforeEach((to, from, next) => {
  // 1. 设置页面标题
  // 2. 公开页面直接放行
  // 3. 未登录跳登录页
  // 4. 检查菜单权限，无权限重定向首页
})
```

---

## 六、运行指南

### 6.1 本地启动

```bash
# 安装依赖
pnpm install

# 启动开发服务器
pnpm dev

# 浏览器访问 http://localhost:5173
```

### 6.2 登录账号

| 角色 | 账号 | 密码 |
|------|------|------|
| 管理员 | admin | admin123 |
| 教师 | teacher | teacher123 |
| 学生 | student | student123 |

### 6.3 生产构建

```bash
pnpm build
```

产物位于 `dist/` 目录，可直接部署到 Nginx / Vercel / GitHub Pages。

---

## 七、项目健康状态

| 检查项 | 状态 | 说明 |
|--------|------|------|
| 生产构建 | ✅ 通过 | `pnpm build` 7.78s 完成 |
| 类型检查 | ✅ 通过 | `vue-tsc --noEmit` 0 错误 |
| 代码规范 | ✅ 通过 | ESLint 9 + Prettier 已配置 |
| 路由导航 | ✅ 正常 | Hash 模式 + 手动 `router.push()` + `:key` 强制刷新 |
| ECharts 渲染 | ✅ 正常 | CanvasRenderer 显式注册 + vue-echarts 封装 |
| 权限控制 | ✅ 正常 | 3 角色菜单过滤 + 按钮指令生效 |
| Excel 导入导出 | ✅ 正常 | xlsx 库按需加载 chunk |

---

## 八、与 Vue 2 传统方案的对比

| 维度 | Vue 2 传统教务系统 | 本项目 (Vue 3) |
|------|-------------------|---------------|
| 构建工具 | Webpack（冷启动 2.5s+） | Vite 6（冷启动 < 300ms） |
| 响应式系统 | `Object.defineProperty` | `Proxy` + `ref/reactive` |
| 逻辑复用 | Mixins（命名冲突风险） | Composables（高内聚、树摇友好） |
| 状态管理 | Vuex（Mutation/Action 冗余） | Pinia（直接修改、TS 完美支持） |
| 图表引入 | ECharts 4 全量打包 | ECharts 5 按需引入，体积减少 60%+ |
| 代码规范 | ESLint + Prettier 分离配置 | ESLint 9 Flat Config 一体化 |
| 路由模式 | History 模式（需服务端配合） | Hash 模式（纯静态部署即可） |

---

## 九、可扩展方向

1. **后端 API 对接**：`request.ts` 已配置拦截器，Store 中替换 Mock 数据即可
2. **真实数据库**：接入 MySQL / PostgreSQL，使用 Prisma / Sequelize ORM
3. **部署上线**：配置 GitHub Actions CI/CD，自动构建并部署到 Vercel
4. **性能优化**：Element Plus 按需引入、路由懒加载已配置，可进一步开启 Gzip/Brotli 压缩
5. **移动端适配**：当前为桌面端优先，可补充响应式断点适配平板/手机
