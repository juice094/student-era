# edu-admin-pro

> 基于 Vue 3 + Vite + TypeScript 的教务数据可视化管理系统，可作为高校教务系统前端重构的标准工程基座。

<p align="center">
  <img src="https://img.shields.io/badge/Vue-3.5-4FC08D?logo=vue.js" alt="Vue 3.5" />
  <img src="https://img.shields.io/badge/Vite-6-646CFF?logo=vite" alt="Vite 6" />
  <img src="https://img.shields.io/badge/TypeScript-5.7-3178C6?logo=typescript" alt="TypeScript" />
  <img src="https://img.shields.io/badge/ECharts-5.6-EE6666?logo=apache-echarts" alt="ECharts" />
  <img src="https://img.shields.io/badge/Element_Plus-2.13-409EFF?logo=element" alt="Element Plus" />
</p>

<p align="center">
  <a href="#-在线预览">在线预览</a> •
  <a href="#-功能特性">功能特性</a> •
  <a href="#-快速开始">快速开始</a> •
  <a href="#-项目结构">项目结构</a> •
  <a href="#-后端对接">后端对接</a>
</p>

---

## ✨ 在线预览

> 本地一键预览：
>
> ```bash
> git clone https://github.com/juice094/edu-admin-pro.git
> cd edu-admin-pro
> pnpm install
> pnpm dev
> ```
>
> 浏览器访问 `http://localhost:5173`

---

## 🎯 功能特性

### 数据可视化大屏
- **首页概览 Dashboard**：KPI 数据卡片 + 院系分布柱状图 + 性别比例饼图 + 招生趋势折线图
- **学生管理看板**：成绩分段分布图 + 专业人数占比图
- ECharts 5 按需引入，自动适配容器尺寸，组件销毁时自动释放实例

### 学生信息 CRUD
- **新增学生**：表单对话框，字段级校验（学号唯一性、姓名长度、必填项）
- **编辑学生**：数据回填，学号锁定（主键保护），实时更新表格
- **删除学生**：二次确认对话框 + **撤销回溯机制**（8 秒内可恢复）
- **表格展示**：Element Plus `el-table`，支持固定列、斑马纹、边框

### 工程化架构
- ⚡ **Vite 6**：冷启动 < 300ms，HMR 毫秒级响应
- 🔒 **TypeScript 5**：全链路类型约束，接口/Props/Store 强类型检查
- 🗂️ **分层架构**：`api` / `stores` / `composables` / `views` / `components` 职责分离
- 🛡️ **代码规范**：ESLint 9 Flat Config + Prettier，保存自动格式化
- 📦 **构建优化**：Rollup 手动分块（vue-vendor / ui-vendor / echarts-vendor），长期缓存更稳定

---

## 🚀 快速开始

### 环境要求

- Node.js >= 18.0.0
- pnpm >= 8.0.0（推荐）

### 安装依赖

```bash
# 克隆项目
git clone https://github.com/juice094/edu-admin-pro.git

# 进入项目目录
cd edu-admin-pro

# 安装依赖（推荐 pnpm）
pnpm install

# 或使用 npm
npm install
```

### 开发调试

```bash
pnpm dev
```

开发服务器启动后，浏览器自动打开 `http://localhost:5173`

### 生产构建

```bash
pnpm build
```

构建产物输出至 `dist/` 目录，可直接部署到 Nginx、Vercel、GitHub Pages 等静态托管平台。

### 代码检查

```bash
pnpm lint      # ESLint 检查并自动修复
pnpm format    # Prettier 格式化全部文件
```

---

## 📁 项目结构

```
edu-admin-pro/
├── public/                     # 静态资源
├── src/
│   ├── api/                    # HTTP 请求层
│   │   ├── modules/            # 按业务域拆分（student / score / report）
│   │   └── request.ts          # Axios 实例 + 拦截器（Token / 错误统一处理）
│   ├── components/             # 通用组件
│   │   ├── AppHeader.vue       # 顶部导航栏
│   │   ├── ChartPanel.vue      # ECharts 图表封装（声明式、自适应、自动销毁）
│   │   ├── DataCard.vue        # 数据概览卡片
│   │   └── StudentFormDialog.vue  # 学生信息表单对话框（新增/编辑共用）
│   ├── composables/            # 组合式逻辑复用
│   │   └── useChart.ts         # ECharts 生命周期管理（init / resize / dispose）
│   ├── router/                 # 路由配置
│   │   └── index.ts            # Vue Router 4，Hash 模式，路由懒加载
│   ├── stores/                 # Pinia 状态管理
│   │   ├── index.ts            # 应用级状态（主题、布局）
│   │   └── student.ts          # 学生业务状态 + 异步 Action
│   ├── styles/                 # 全局样式与主题变量
│   │   ├── variables.scss      # SCSS 变量（主色、辅色、图表色系）
│   │   └── index.scss          # 全局重置与基础样式
│   ├── types/                  # TypeScript 类型定义
│   │   └── index.ts            # Student / ApiResponse / ChartData 等
│   ├── utils/                  # 工具函数
│   │   └── format.ts           # 千分位、日期格式化
│   ├── views/                  # 页面级组件
│   │   ├── HomeView.vue        # 首页 Dashboard（数据卡片 + 3 图表）
│   │   ├── StudentView.vue     # 学生管理（表格 CRUD + 2 图表）
│   │   └── AboutView.vue       # 系统说明与技术栈对比
│   ├── App.vue                 # 根组件（布局框架）
│   └── main.ts                 # 应用入口（插件注册、ECharts 渲染器注册）
├── .vscode/                    # VS Code 工作区配置（推荐扩展 + 保存自动格式化）
├── env.d.ts                    # Vite 客户端类型声明
├── eslint.config.mjs           # ESLint 9 扁平化配置
├── prettier.config.mjs         # Prettier 代码风格配置
├── vite.config.ts              # Vite 构建配置（别名、代理、手动分块）
└── package.json
```

---

## 🔌 后端对接

### 1. 配置代理

修改 `vite.config.ts` 中的 `server.proxy`，指向你的后端 API 地址：

```typescript
server: {
  proxy: {
    '/api': {
      target: 'http://localhost:8080',  // ← 修改为你的后端地址
      changeOrigin: true,
      rewrite: (path) => path.replace(/^\/api/, '')
    }
  }
}
```

### 2. 修改接口地址

生产环境下，修改 `env.production` 或在 `request.ts` 中配置 `baseURL`：

```typescript
const request = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL || '/api',
  timeout: 10000
})
```

### 3. 按业务模块扩展接口

在 `src/api/modules/` 下新建文件，例如 `score.ts`：

```typescript
import request from '../request'

export function fetchScoreList(params: any) {
  return request.get('/scores', { params })
}
```

### 4. Mock 数据切换

当前学生表格使用本地 Mock 数据（位于 `StudentView.vue` 的 `mockStudents`）。接入真实后端后：

1. 移除 `mockStudents` 和 `onMounted` 中的本地注入逻辑
2. 在 `stores/student.ts` 中调用真实 API（`fetchStudentList`）
3. 表格数据源保持绑定 `studentStore.students` 即可，无需改动模板

---

## 🏗️ 工程化亮点

### 从 Vue 2 到 Vue 3 的升级映射

| 维度 | 传统教务系统（Vue 2） | edu-admin-pro（Vue 3） |
|-----|---------------------|----------------------|
| 构建工具 | Webpack（冷启动 2.5s+） | Vite 6（冷启动 < 300ms） |
| 响应式系统 | `Object.defineProperty` | `Proxy` + `ref/reactive` |
| 逻辑复用 | Mixins（命名冲突风险） | Composables（高内聚、树摇友好） |
| 状态管理 | Vuex（Mutation/Action 冗余） | Pinia（直接修改、TS 完美支持） |
| 图表引入 | ECharts 4 全量打包 | ECharts 5 按需引入，体积减少 60%+ |
| 代码规范 | ESLint + Prettier 分离配置 | ESLint 9 Flat Config 一体化 |

### 图表组件封装策略

原生 ECharts 命令式 API（`echarts.init` + `setOption`）在 Vue 单页应用中容易导致内存泄漏。本项目通过以下策略解决：

- **生命周期托管**：`useChart` composable 在 `onMounted` 初始化、`onUnmounted` 自动 `dispose`
- **响应式同步**：`watch` 监听 option 变化，自动 `setOption` 更新
- **自适应布局**：`window.addEventListener('resize')` → `chart.resize()`
- **声明式调用**：`ChartPanel` 组件只需传入 `option` 对象，无需关心底层 ECharts API

---

## 📄 开源协议

[MIT](LICENSE) © 2025 juice094
