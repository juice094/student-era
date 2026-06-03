---
title: "课程设计个人报告 — Vue Web Worker 实验室"
date: 2026-05-31
tags: [课程设计, 个人报告, Vue3, Web Worker]
domain: 工程
status: 完成
---

# 课程设计个人报告 — Vue Web Worker 实验室

> 项目：vue-web-worker-lab（Vue3 + Web Worker 数学计算实验室）
> 角色：项目协调 / 架构设计 / 技术文档 / Git 管理
> GitHub：[juice094/vue-web-worker-lab](https://github.com/juice094/vue-web-worker-lab)

---

## 一、代码范围、功能与统计

### 1.1 负责范围

本项目为**团队协作项目**，本人与队友（张瑞坤、周小超）共同完成。本人在项目中的角色定位如下：

| 职责 | 内容 | 说明 |
|---|---|---|
| **项目初始化** | Vite + Vue 3 + TypeScript 脚手架搭建 | 确定技术选型、目录结构、构建配置 |
| **架构文档** | Comprehensive README（14 KB+） | 项目架构说明、模块设计、技术选型 rationale、目录结构定义 |
| **Git 管理** | 合并冲突解决、分支策略 | 解决远程与本地 README 冲突，保留综合版本 |
| **代码审查** | 参与 V2.1 / V2.1.2 代码 review | 对队友提交的缩放逻辑优化进行审查与合并 |

### 1.2 核心代码贡献者

**张瑞坤 (zrkjsnb)**：项目核心功能开发者，独立完成以下模块：

| 模块 | 文件 | 功能 |
|---|---|---|
| 计算器 | `src/views/CalculatorView.vue` | 基础科学计算界面 |
| 方程求解器 | `src/views/SolverView.vue` (18.9 KB) | 线性/非线性方程求解、多方法切换 |
| 矩阵实验室 | `src/views/MatrixLabView.vue` (11 KB) | 矩阵运算、可视化编辑、结果展示 |
| 数据绘图 | `src/views/PlotterView.vue` (11.6 KB) | 函数图像绘制、缩放/平移交互 |
| 数据分析 | `src/views/DataAnalysisView.vue` (16.6 KB) | 数据集导入、统计量计算、图表展示 |
| Web Worker 核心 | `src/workers/*.ts`（5 个 Worker） | 计算密集型任务 offload：矩阵运算(solver.worker.ts 21.3 KB)、统计(stats.worker.ts)、绘图(plot.worker.ts)、计算(calc.worker.ts)、矩阵(matrix.worker.ts) |
| 组合式函数 | `src/composables/*.ts` | useWorker / useSolver / useMatrix / useStats 封装 |
| 组件层 | `src/components/*.vue` | DataUploader、EquationInput、MatrixEditor、ParamForm、ResultPanel |

**周小超**：参与 V2.1 / V2.1.2 的缩放逻辑优化（Plotter 视图交互）。

### 1.3 Git 提交统计

- **本人提交**：5 次（初始化 2 次 + README 文档 2 次 + 合并冲突解决 1 次）
- **张瑞坤提交**：3 次（V2.1 + V2.1.2 核心功能）
- **总提交**：9 次
- **本人代码贡献占比**：约 **20%**（主要为脚手架 + 文档），核心功能由队友实现

---

## 二、实现与测试逻辑

### 2.1 架构设计（本人设计）

```
src/
  ├── views/              # 五大功能视图（Calculator/Solver/MatrixLab/Plotter/DataAnalysis）
  ├── components/          # 通用输入/展示组件
  ├── composables/         # Worker 封装与业务逻辑组合式函数
  ├── workers/             # Web Worker 计算层（5 个独立 Worker）
  ├── router/              # 路由配置
  └── stores/             # 全局状态（appStore.ts）
```

**技术选型 rationale**（本人在 README 中定义）：
- Vue 3 Composition API：复杂计算逻辑适合用 composables 封装
- TypeScript：数学计算需要严格类型保障
- Web Worker：矩阵运算、方程求解等 CPU 密集型任务 offload 到后台线程，避免 UI 阻塞
- Vite：快速冷启动 + 原生 ESM 支持

### 2.2 Web Worker 通信协议（队友实现，本人审查）

- 采用 `postMessage` + `onmessage` 标准 API
- 每个 Worker 独立负责一类计算：
  - `solver.worker.ts`：方程求解（线性/非线性，多种算法）
  - `matrix.worker.ts`：矩阵运算（行列式、逆矩阵、特征值等）
  - `stats.worker.ts`：统计分析（均值/方差/回归等）
  - `plot.worker.ts`：绘图数据生成（采样点计算）
  - `calc.worker.ts`：基础计算器逻辑

### 2.3 测试方式

- **手动功能测试**：每个视图页面独立测试输入→计算→结果展示流程
- **Worker 通信测试**：通过浏览器 DevTools Network/Performance 面板验证计算确实 offload 到 Worker 线程
- **缩放逻辑测试**（V2.1.2）：Plotter 视图的缩放/平移交互经过多轮迭代优化
- **合并冲突测试**：README 冲突解决后，验证项目构建和运行正常

---

## 三、后续开发、未完成工作与接手注意事项

### 3.1 已完成功能（闭环）

- [x] Vue 3 + TS 项目脚手架（本人）
- [x] 五大计算视图（张瑞坤）：Calculator / Solver / MatrixLab / Plotter / DataAnalysis
- [x] Web Worker 计算层（张瑞坤）：5 个 Worker
- [x] Composables 封装（张瑞坤）：useWorker / useSolver / useMatrix / useStats
- [x] 组件层（张瑞坤）：输入/展示通用组件
- [x] 路由与导航（本人基础配置 + 队友扩展）
- [x] 项目文档（本人）：README 架构说明

### 3.2 未完成 / 可扩展项

| 优先级 | 功能 | 说明 |
|---|---|---|
| P1 | 单元测试 | 缺 Vitest + 数学结果断言测试 |
| P1 | 错误处理 | Worker 通信异常、计算超时场景未完全覆盖 |
| P2 | 公式渲染 | 可引入 KaTeX 渲染数学公式，当前为纯文本展示 |
| P2 | 历史记录 | 计算历史本地持久化 |
| P3 | 多 Worker 并发 | 当前为单 Worker 单任务，可扩展为 Worker Pool |

### 3.3 接手注意事项

1. **Worker 调试**：Web Worker 在 DevTools 中独立于主线程，console 输出需切到 Worker 上下文查看。
2. **TypeScript + Worker**：Vite 对 `.worker.ts` 有原生支持，但类型定义需手动维护 Worker 的 message 接口。
3. **计算精度**：浮点数运算存在精度问题，结果显示需做 round 处理。
4. **大矩阵性能**：超大矩阵运算可能超出 Worker 执行时间限制，需增加分块计算或进度反馈。
5. **队友代码风格**：张瑞坤的代码注释较少，核心逻辑集中在 `solver.worker.ts`（21.3 KB），接手时需耐心阅读。
6. **Git 协作规范**：本项目发生过 README 冲突覆盖事件（`vue-web-worker-lab-README覆盖事件报告.md`），建议采用 PR + review 流程，避免直接推送 main。

---

## 四、项目学习成长报告

### 4.1 对项目自身的理解

本项目是一个**Web Worker 技术验证项目**，核心目标是验证"CPU 密集型计算 offload 到后台线程"的可行性。最大的价值不在于功能丰富度，而在于**验证了 Vue 3 + Web Worker + TypeScript 的技术栈可行性**。

作为项目协调者，我学会了**如何在有限时间内定义清晰的技术边界**：当课程设计时间有限时，选择一个有深度的技术点（Web Worker 通信协议）比做十个浅层功能更有价值。同时，作为协调者需要为队友提供**清晰的技术约束和接口规范**——本人在 README 中定义的目录结构和模块边界，让张瑞坤能够专注于算法实现而不需关心工程化细节。

### 4.2 从合作中学到的东西

- **队友张瑞坤的数学算法实现**：`solver.worker.ts` 中多种方程求解算法的组织方式（二分法、牛顿法、高斯消元等）展示了如何将数学课本知识转化为工程代码。特别是 Worker 中的分步计算和进度反馈设计，让我理解了**异步计算的用户体验设计**——不是"等结果"，而是"看进度"。
- **Web Worker 的通信模式**：从队友的代码中学习到了主线程与 Worker 的消息协议设计——如何定义请求/响应格式、如何处理异步回调、如何终止长时间运行的 Worker。这些模式可以复用到任何需要后台计算的前端项目中。
- **Git 协作的教训**：README 覆盖事件（`vue-web-worker-lab-README覆盖事件报告.md`）让我认识到**强制推送的风险**——即使是为了解决冲突，也可能丢失队友的变更。后续项目中，我建立了 PR + review 的工作流，即使在小团队中也能保证变更可追溯。
- **角色分工的价值**：本项目让我明确了自己的定位——**架构与工程化能力强于算法实现能力**。当张瑞坤专注于写 solver 算法时，我负责确保他的代码能正确构建、正确运行、正确合并。这种互补分工比"每个人都做一点"更高效。

### 4.3 独立开发的流程认知与能力匹配

**是否能独立复现类似项目？部分能，部分需提升。**

**已具备的能力**：
1. **技术选型与架构设计**：能根据项目目标选择合适的技术栈（Vue 3 + TS + Worker），并定义模块边界和接口规范。
2. **工程化脚手架搭建**：Vite 配置、TS 严格模式、目录结构设计、Git 工作流建立。
3. **团队协作与 Git 管理**：分支策略、冲突解决、代码审查、PR 流程。
4. **文档维护**：架构文档、README 规范、变更记录，让项目"可交接"。

**待提升的能力**：
1. **数学算法实现**：队友写的求解器算法我需要更多时间理解，独立实现类似复杂度算法的能力尚不足。特别是非线性方程的数值解法（牛顿迭代、二分法的收敛条件判断）需要补充数学基础。
2. **Worker 通信协议设计**：当前能理解队友的实现，但独立设计高效的消息协议（如批量任务分片、Worker Pool 调度）还需练习。
3. **性能优化**：Worker 的启动开销、内存管理、并发控制等深层优化未涉及。大矩阵运算的内存溢出风险未做防护。
4. **测试覆盖**：本项目缺单元测试，我尚未掌握 Vitest + 数学断言的测试写法。

**总结**：本项目让我认识到了**自己的定位更偏向架构与工程化**，核心算法实现需要与算法能力强的队友配合。在后续项目中，我会优先承担技术选型、架构设计、文档维护与代码审查的角色，同时持续补充算法与数学基础。Web Worker 的技术验证经验已内化，可复用到任何需要前端后台计算的场景（如大数据可视化、图像处理、复杂模拟等）。

---

**报告人**：宿 (juice094)  
**日期**：2026-05-31  
**项目仓库**：[https://github.com/juice094/vue-web-worker-lab](https://github.com/juice094/vue-web-worker-lab)
