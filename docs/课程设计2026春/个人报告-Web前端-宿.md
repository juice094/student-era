---
title: "课程设计个人报告 — Web 前端项目（Vue3 + 学校主页 + Portal 系统）"
date: 2026-05-31
tags: [课程设计, 个人报告, Vue3, 前端工程化]
domain: 工程
status: 完成
---

# 课程设计个人报告 — Web 前端项目

> 项目：course-design-web-frontend（学校主页 + 个人 Portal + 后台管理）
> 角色：个人 Portal 独立开发者 / 学校主页工程化整合者
> 课程设计周期：2026-05-26 至 2026-05-31（6 天）
> GitHub：[juice094/course-design-web-frontend](https://github.com/juice094/course-design-web-frontend)
>
> **说明**：本仓库为课程设计期间的工作仓库，包含**个人 Portal 系统**（本人本次独立完成）、**学校主页**（组员负责，本人仅工程化整合）及**教务后台**（复用大数据可视化课程既有成果，非本次新建）。本次课程设计本人实际负责范围为**个人 Portal 系统全部 + 学校主页工程化整合**。

---

## 一、代码范围、功能与统计

### 1.1 负责范围

本次课程设计（2026-05-26 至 2026-05-31，共 6 天）本人负责两部分：

1. **个人 Portal 系统**：全部独立设计与实现（从架构到组件到特效）
2. **学校主页**：组员负责原始页面开发，本人负责工程化重构与整合

以下分模块详述。原仓库中的**教务后台管理模块**为大数据可视化课程既有成果复用，非本次新建。

#### 模块 A：个人 Portal 系统（本次课程设计核心成果，全部独立完成）

| 文件 | 规模 | 负责功能 |
|---|---|---|
| `src/components/portal/PortalSettings.vue` | 42.4 KB | 设置中心：拖拽布局管理器、网格系统、卡片尺寸调节、编辑模式、持久化配置 |
| `src/layouts/PortalLayout.vue` | 4.1 KB | Portal 布局框架：自适应缩放算法、navbar 固定尺寸 + 卡片区域动态缩放 |
| `src/views/portal/HomeView.vue` | 8.8 KB | Portal 首页：卡片渲染、布局响应式、嵌套导航 |
| `src/components/portal/CustomCards.vue` | 4.7 KB | 自定义卡片组件族：可配置、可拖拽、可缩放 |
| `src/components/portal/SettingsAppearance.vue` | 20.6 KB | 外观设置中心：主题切换、背景模式选择、粒子密度调节、特效开关、实时预览 |
| `src/stores/portal.ts` | 8.8 KB | Portal 状态管理：布局状态、卡片配置、持久化逻辑 |
| `src/components/portal/PortalNavbar.vue` | 5.5 KB | 导航栏：路由切换、用户状态显示、响应式折叠 |
| `src/components/portal/*.vue`（共 15+ 个） | ~60 KB 合计 | 身份卡、技能雷达、项目展示、成就时间线、文章区、相册、动态流、课程表等子组件 |

#### 模块 B：Canvas 特效渲染系统（Portal 配套，自研）

| 文件 | 规模 | 负责功能 |
|---|---|---|
| `src/components/effects/ParticleCanvas.vue` | 4.1 KB | 粒子 Canvas 画布：统一渲染入口、性能帧率控制 |
| `src/components/effects/renderers/*.ts`（6 个） | ~11 KB 合计 | 多场景粒子渲染器：弹幕(danmaku)、萤火虫(firefly)、草地(grass)、樱花(sakura)、雪花(snow)、密度控制器 |
| `src/components/effects/ClickRipple.vue` | 3.1 KB | 点击涟漪特效：鼠标点击波纹扩散动画 |
| `src/components/effects/PageTransition.vue` | 0.6 KB | 页面过渡动画：路由切换时的淡入淡出 |
| `src/components/effects/ToastContainer.vue` | 2.3 KB | 全局 Toast 通知容器 |
| `src/stores/effects.ts` | 2.0 KB | 特效状态管理：粒子开关、密度、当前渲染器选择 |

#### 模块 C：学校主页（组员两版本 + 本人工程化重构与整合）

学校主页由**两位组员分别独立实现两个版本**，本人负责两个版本的**工程化重构、标准化整合与答辩演示适配**。

**版本一：甘肃农业大学官网风格（HTML 版）— 组员 yang-k123**

| 文件/目录 | 规模 | 原始贡献者 | 本人工程化工作 |
|---|---|---|---|
| `school-homepage/gsau-style.html` | 700+ 行 | yang-k123 | 工程化重构为标准化结构：拆分为 `css/style.css`(600行)、`js/main.js`、`components/{top-bar,header,footer}` |
| `school-homepage/*.html`（8 个二级页面） | 各 100~133 行 | yang-k123 | 保留原始文件作为备份，重构后统一入口为 `index.html` |
| `school-homepage/甘肃农业大学官网-优化版.html` | 1,037 行 | yang-k123 | 保留备份，重构说明写入 `README.md` |
| `school-homepage/README.md` | 66 行 | — | **本人撰写**：工程结构说明、目录规范 |
| `school-homepage/MISSING.md` | 112 行 | — | **本人撰写**：教学案例缺失内容清单及补齐路径 |

本人工程化重构内容（`dcdfada`）：
- 将单体 36KB HTML 拆分为标准工程结构（CSS/JS/组件分离）
- 主样式表约 600 行含注释，主脚本 DOMContentLoaded 封装
- 组件拆分：top-bar、header、footer 独立为可复用片段
- 新入口 `index.html` 引用外部资源，保留原始文件作为备份

**版本二：Web技术大学（Vue 版）— 组员 Moxn**

| 文件/目录 | 规模 | 原始贡献者 | 本人工程化工作 |
|---|---|---|---|
| `school-homepage/moxn/src/home/components/*` | 45+ 个 Vue 组件 | Moxn | 从根目录提取并重定位到 `school-homepage/moxn/` 子目录，避免与主项目冲突 |
| `school-homepage/moxn/src/home/views/*` | 15+ 个页面视图 | Moxn | 保留内部路由结构，独立构建入口 |
| `school-homepage/moxn/public/images/*` | 80+ 张资源图片 | Moxn | 图片资源批量下载脚本自动化处理 |
| `school-homepage/moxn/src/router/index.js` | 141 行 | Moxn | 保留内部路由，不接入主项目路由树，保持完全隔离 |
| `school-homepage/moxn/package.json` | 23 行 | Moxn | 独立依赖管理，可单独 `npm install && npm run dev` 启动 |

本人工程化整合内容（`8bf9823`）：
- Moxn 原始提交（`72398b5`）将完整 Vue 项目直接推送到仓库**根目录**，与主项目文件（`.github/`、`docs/`、`env.d.ts`、`package.json`、`index.html` 等）产生严重冲突
- 本人提取 Moxn 的 feat 分支，将所有新增文件**重定位**到 `school-homepage/moxn/` 子目录下，作为独立子项目
- **刻意保留的隔离边界**：不合并根级文件删除、不合并 `.gitignore` / `package.json` / `index.html` 修改，确保主项目 Portal 系统零影响
- 配置独立启动路径：`cd school-homepage/moxn && npm install && npm run dev`

**答辩演示一键启动脚本**：
- 本人编写 `start-demo.ps1`（位于 web-frontend 根目录），一键同时启动：
  1. Web 前端主项目（Portal + 后台）— `pnpm dev`
  2. 学校主页 Moxn Vue 版 — `npm run dev -- --port 5174`
  3. 学校主页 HTML 版 — `npx serve --listen 5175`
  4. Canvas 游戏 — `npx serve --listen 5176`
  5. Vue Web Worker — `npm run dev -- --port 5177`
- 支持分类启动参数：`--OnlyWeb`、`--OnlyGame`、`--OnlyWorker`

#### 模块 D：工程化与架构重构（Portal 相关）

| 工作项 | 范围 | 说明 |
|---|---|---|
| Store 层重构 | `src/stores/portal.ts` + 持久化插件 | Portal 状态管理改为 `readonly` 导出 + 统一持久化插件，消除跨模块状态污染 |
| 图标系统迁移 | Portal 相关组件 | FontAwesome → Lucide Icons，减少 bundle 体积 |
| 路由重构 | `src/router/portal.ts` | Portal 嵌套路由实现 |
| Portal 与学校主页整合 | `start-demo.ps1` | 一键启动脚本，同时启动 Portal + 两个学校主页版本 |

#### 模块 E：教务后台（复用其他课程成果，非本次新建）

> 仓库中的学生/教师/课程/成绩/选课管理等业务模块，为**大数据可视化课程既有成果**复用。本次课程设计期间未新建或修改，故不纳入本次个人贡献范围。

### 1.2 代码统计（本次课程设计范围）

| 类别 | 规模 | 说明 |
|---|---|---|
| **个人 Portal 系统** | PortalSettings.vue 42KB + 15+ 子组件 + 特效系统 | 全部独立实现 |
| **学校主页整合** | 工程化重构脚本 + README + MISSING.md | 组员原始代码，本人仅负责整合 |
| **一键启动脚本** | `start-demo.ps1` | 答辩演示用，同时启动 5 个服务 |

- **本次新增/独立实现**：Portal 系统全部（含拖拽布局、特效渲染、设置中心）、工程化整合脚本
- **复用**（不纳入本次贡献）：教务后台模块（17 个 Store + 业务视图，源自大数据可视化课程）
- **整合**（非原创）：学校主页两个版本（组员原始代码）
- **技术栈**：Vue 3 + TypeScript + Vite + Pinia + Element Plus + Lucide Icons + ECharts

### 1.3 Git 提交统计

**仓库总提交（2026-05-26 前复用既有成果 + 本次课程设计期间）**：

| 贡献者 | 提交数 | 内容 |
|---|---|---|
| juice094（本人） | 51 次 | Portal 系统全部、工程化重构、业务模块（含复用成果）、整合脚本 |
| dependabot[bot] | 3 次 | 安全依赖升级 |
| Moxn | 1 次 | 学校主页 Vue 版初始导入 |
| yang-k123 | 1 次 | 学校主页 HTML 版初始导入 |

**本次课程设计期间（2026-05-26 起）本人新增提交**：
- Portal 系统拖拽布局、特效渲染、设置中心、自适应算法（全部独立实现）
- 学校主页工程化整合（Moxn 版从根目录提取到子目录 + yang-k123 版拆分重构）
- `start-demo.ps1` 一键启动脚本
- 工程化重构（Store readonly 导出、Lucide 图标迁移、Portal 路由）

> 注：仓库中 51 次提交包含大数据可视化课程既有成果（教务后台模块），本次课程设计期间新增提交集中在 Portal 系统与学校主页整合。

---

## 二、实现与测试逻辑

### 2.1 架构设计

采用**模块化分层架构**：

```
src/
  ├── components/        # 公共组件 + Portal 组件 + 特效组件
  ├── views/             # 页面级组件（按业务域拆分）
  ├── stores/            # Pinia 状态管理（按领域拆分，readonly 导出）
  ├── router/            # 嵌套路由（portal / admin / index 三文件）
  ├── api/               # API 层（请求封装 + 错误处理）
  ├── layouts/           # 布局组件（PortalLayout 自适应）
  ├── composables/       # 组合式函数
  ├── directives/        # 自定义指令（权限）
  ├── shared/persist/    # 统一持久化插件
  └── vendor/            # 第三方封装（echarts-config, vue-utils）
```

### 2.2 关键实现细节

1. **Portal 拖拽布局系统**：
   - 基于 CSS Grid 的响应式网格
   - 编辑模式下卡片可拖拽交换位置、调节尺寸（1×1 / 1×2 / 2×1 / 2×2）
   - 布局状态通过 Pinia + 持久化插件自动保存到 localStorage
   - 自适应算法：navbar 固定高度，剩余空间按比例分配给卡片区域

2. **Canvas 粒子特效系统**：
   - 统一渲染入口 `ParticleCanvas.vue`，根据当前场景切换 renderer
   - 每种 renderer 独立实现，通过统一接口（`init` / `render` / `destroy`）接入
   - 性能控制：requestAnimationFrame + 粒子数量上限（density.ts）
   - 与 Element Plus 弹窗的 z-index 冲突经过 3 轮迭代修复（ClickRipple / Toast 图层调整）

3. **Portal Store 层设计**：
   - Portal 的 Store 导出 `readonly(state)` + 显式 action 方法，避免跨模块修改
   - 统一持久化插件自动处理 localStorage 同步，布局配置刷新不丢失

4. **学校主页整合**：
   - 将 Moxn 的独立项目以子目录形式嵌入，保持代码隔离
   - 独立路由配置，不影响主项目构建
   - `start-demo.ps1` 一键启动脚本，答辩时可同时展示 5 个服务

### 2.3 测试与质量审查方式

- **UI 回归测试**：Portal 布局修复（如自适应缩放问题）均基于实际渲染测试，经过多轮迭代确认修复
- **图层冲突审查**：`ClickRipple` / `Toast` 与 Element Plus 弹窗的 z-index 冲突，通过实际弹窗触发测试验证
- **拖拽交互测试**：Portal 编辑模式下拖拽交换位置、调节尺寸，手动验证 20+ 次不同场景
- **学校主页隔离测试**：Moxn 学校主页嵌入后，验证主项目构建不受影响（独立路由、独立构建入口）
- **一键启动测试**：`start-demo.ps1` 在本地验证 5 个服务可并行启动，端口无冲突

---

## 三、后续开发、未完成工作与接手注意事项

### 3.1 已完成功能（闭环，本次课程设计范围）

- [x] **个人 Portal 系统**（拖拽布局 + 卡片管理 + 设置中心 + 自适应缩放）—— 6 天内独立完成
- [x] **Canvas 粒子特效系统**（6 种渲染器 + 统一控制面板）—— Portal 配套特效
- [x] **学校主页整合**（两个组员版本的工程化重构 + 一键启动脚本）
- [x] Store 层工程化重构（Portal 相关 Store 的 readonly + 持久化）
- [x] 图标系统迁移（Lucide）
- [x] Portal 路由重构（嵌套路由）

### 3.1.1 复用成果（非本次新建）

- [x] 教务后台管理模块（学生/教师/课程/成绩/选课）— 大数据可视化课程既有成果
- [x] 统一权限与登录系统 — 复用成果
- [x] CI/CD 与安全自动化（Dependabot + CodeQL）— 复用既有配置

### 3.2 未完成 / 可扩展项（Portal 系统）

| 优先级 | 功能 | 说明 |
|---|---|---|
| P1 | 后端 API 对接 | Portal 目前为前端 mock 数据，需接入真实后端（已有 request.ts 封装，替换 baseURL 即可） |
| P1 | 移动端适配 | Portal 布局在移动端需切换为单列堆叠，当前为桌面优先，6 天内未覆盖 |
| P2 | 单元测试覆盖 | 缺 Jest/Vitest 测试，需补 composables 和 stores 的单元测试 |
| P2 | 性能优化（Code Splitting） | 当前为单 chunk 构建，可按路由拆分 lazy load |
| P3 | 暗黑模式完整覆盖 | 部分学校主页组件未适配暗黑主题 |

### 3.3 接手注意事项

1. **pnpm 包管理**：项目使用 pnpm，npm 可能导致 lock 文件冲突。
2. **Store 只读约定**：Portal 的 Store 状态通过 `readonly()` 包装，直接修改会编译报错，必须通过 action 方法。
3. **特效系统性能**：`ParticleCanvas` 在低端设备上可能掉帧，可通过 `effects.ts` 中的密度设置降级。
4. **路由嵌套层级**：`portal` 路由为独立路由树，新增页面需确认归属正确的路由文件。
5. **学校主页隔离**：`school-homepage/moxn/` 为独立子项目，修改时注意不要破坏其内部路由和相对路径引用。此模块由 Moxn 维护，本人仅负责集成层。`school-homepage/` 的 HTML 版由 yang-k123 维护。
6. **TypeScript 严格模式**：项目开启严格模式，新增代码需处理所有类型推断，不可隐式 any。
7. **复用模块边界**：`src/views/StudentView.vue`、`TeacherView.vue`、`CourseView.vue` 等教务后台模块为大数据可视化课程既有成果，如需修改请先确认原始作者意图。

---

## 四、项目学习成长报告

### 4.1 对项目自身的理解

本次课程设计（6 天）的核心成果是**个人 Portal 系统**，从零开始独立设计并实现了一个完整的交互式布局引擎。

**时间约束下的取舍**：6 天时间内需要完成 Portal 系统 + 整合学校主页，我选择了"深度优先"策略——将 Portal 的拖拽布局、自适应缩放、特效系统做扎实，而不是横向铺开做更多模块。教务后台模块直接复用既有成果，避免重复造轮子。

**拖拽布局引擎的设计**：这是我首次独立设计交互式布局系统。从最初的手写坐标计算到最终采用 CSS Grid + Vue 响应式数据绑定，经历了 3 轮迭代。核心难点在于**浏览器布局引擎与 JS 状态的双向同步**——CSS Grid 的 `grid-template-areas` 需要与 Vue 的响应式数据实时同步，而拖拽交换位置时两者的状态一致性需要精心处理。

**学校主页整合的价值**：Moxn 和 yang-k123 的原始代码展示了两种不同的前端组织方式（Vue 单页应用 vs 传统多页面 HTML），我负责的工程化整合（目录隔离、冲突解决、一键启动）让我学会了**如何在保持代码隔离的前提下实现功能聚合**——这对于答辩演示时同时展示多个项目非常重要。

### 4.2 从合作与代码中学到的东西

- **Moxn 的学校主页代码**：学习了传统多页面站点的组件拆分策略（按页面区块拆分 vs 按功能拆分），以及大量图片资源的自动化处理方案（批量下载脚本）。Moxn 的代码风格偏向模板化（大量重复的课程详情组件），让我意识到**组件抽象的时机**——过早抽象会增加理解成本，过晚则导致维护困难。
- **Element Plus 的边界**：组件库能解决 80% 的需求，但剩下的 20%（如 z-index 冲突、自定义主题变量）需要深入源码理解其设计决策。3 轮图层冲突修复让我理解了 Vue 3 Teleport + Element Plus 层级管理的内部机制。
- **时间约束下的架构决策**：6 天时间内如果既要写 Portal 又要写后台，必然两边都做不深。选择复用既有成果（教务后台）是正确的——把时间花在 Portal 的拖拽布局上，而不是重复造轮子。这验证了**"复用不是偷懒，是资源的最优分配"**。

### 4.3 短期冲刺的流程认知与能力匹配

**6 天内能否独立完成一个完整的 Portal 系统？能。**

本次课程设计的实践证明，在明确目标（只做 Portal + 整合学校主页）和复用既有成果（教务后台）的前提下，6 天足以完成一个具备完整交互的系统。

**已验证的能力**：
1. **快速架构决策**：在第一天就确定"CSS Grid + Pinia + 持久化"的技术方案，避免了中途重构的成本。
2. **增量交付能力**：每天结束时 Portal 都是可运行的——第一天是静态布局，第二天是拖拽，第三天是特效，第四天是设置中心，第五天是整合，第六天是答辩准备。每个阶段都是一个可演示的增量。
3. **复用判断能力**：明确区分"本次需要做的"（Portal）和"可以复用的"（教务后台），不把时间花在重复造轮子上。
4. **第三方模块整合能力**：在半天内完成 Moxn 学校主页的冲突解决和目录隔离，保证主项目不受影响。
5. **工程化习惯**：即使在 6 天冲刺中，依然保持提交记录清晰（每完成一个功能就 commit），为后续审查留下可追溯的历史。

**待提升的能力**：
- **测试驱动开发**：6 天时间全部投入功能实现，缺单元测试。后续应引入 Vitest + Vue Test Utils，在功能开发的同时补测试。
- **移动端适配**：Portal 布局在移动端需要单列堆叠，当前为桌面优先，未在 6 天内覆盖。
- **后端联调**：Portal 目前使用 mock 数据，真实项目需要前后端联调能力（NestJS / 数据库设计）。

---

**报告人**：宿 (juice094)  
**日期**：2026-05-31  
**项目仓库**：[https://github.com/juice094/course-design-web-frontend](https://github.com/juice094/course-design-web-frontend)
