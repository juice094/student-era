---
title: "课程设计个人报告 — Canvas 游戏《Hero Catch Monster》"
date: 2026-05-31
tags: [课程设计, 个人报告, 游戏开发]
domain: 工程
status: 完成
---

# 课程设计个人报告 — Canvas 游戏《Hero Catch Monster》

> 项目：course-design-canvas-game（草原王者类射击游戏）
> 角色：核心开发者 / 基础系统唯一实现者
> GitHub：[juice094/course-design-canvas-game](https://github.com/juice094/course-design-canvas-game)

---

## 一、代码范围、功能与统计

### 1.1 本人负责范围（Phase 0-7 全部基础系统）

本人独立完成了游戏**全部基础架构与核心玩法系统**的设计与实现，从引擎到具体玩法逻辑，覆盖以下模块：

| 文件 | 规模 | 负责功能 |
|---|---|---|
| `src/engine.js` | 14.9 KB | 游戏主循环、状态机（MENU/PLAY/SHOP/PAUSE/GAMEOVER）、渲染管线、碰撞调度、存档/读档接口、关卡模式兼容 |
| `src/player.js` | 13.1 KB | 玩家实体：移动控制（WASD/方向键）、射击系统、动画状态机、受伤无敌帧、死亡与复活逻辑、角色绘制 |
| `src/enemy.js` | 16.3 KB | 敌人系统：Orc / Ogre / Mushroom 三种基础敌人 + Spikey 精英怪；寻路 AI、受击闪白反馈、掉落概率 |
| `src/shop.js` | 10.3 KB | 商店系统：货币经济、商品购买、属性升级（攻击/移速/血量）、状态切换渲染 |
| `src/powerup.js` | 8.2 KB | 道具系统：多种增益道具生成、拾取判定、持续时间管理与视觉反馈 |
| `src/wave-manager.js` | 6.3 KB | 波次管理：难度曲线算法、敌人生成调度器、波次间商店触发逻辑 |
| `src/map.js` | 8.3 KB | 地图/瓦片系统：Tile 碰撞检测、墙内生成安全检查（全局方法） |
| `src/audio.js` | 7.5 KB | 音频系统：Web Audio API 封装、BGM/音效混合、音量管理与暂停恢复 |
| `src/input.js` | 7.2 KB | 输入系统：键盘事件映射、触摸输入适配、重启快捷键（R键） |
| `src/main.js` | 10.4 KB → 扩展后更大 | 入口与初始化、状态机主控（新增 LEVEL_SELECT / LEVEL_CLEAR / WIN 状态兼容层） |
| `src/bullet.js` | 2.2 KB | 子弹实体：发射逻辑、生命周期、碰撞判定与销毁 |
| `src/utils.js` | 2.8 KB | 工具函数库：随机生成、距离计算、边界检查、辅助数学 |

### 1.2 队友负责范围（扩展系统）

以下模块由队友在本人 Phase 7 完成后的基础上扩展实现：

| 文件 | 作者 | 规模 | 功能 |
|---|---|---|---|
| `src/achievement.js` | **xushaoyang15** | 170 行（~5 KB） | 成就系统：8 个成就定义（初次战斗/通过试炼/生存专家/金币猎人/精明买家/坚持到底/关卡起步/通关勇者）、解锁条件检测、Toast 通知、成就列表展示、localStorage 持久化 |
| `src/main.js`（扩展） | **RTaoTao** | +245 行 | 选关系统：LEVEL_SELECT 状态、5 关配置（草原入口→魔王城堡）、无尽/关卡模式切换、键盘 1-5 选关输入处理 |
| `src/engine.js`（扩展） | **RTaoTao** | +84 行 | 本地存档系统：saveData 结构（unlockedLevel/highestClearedLevel/totalCoinsEarned）、关卡完成/游戏结束时的存档更新、关卡模式参数注入 |
| `src/player.js`（扩展） | **RTaoTao** | 角色绘制调整 | 美术资源替换实验后恢复原版绘制 |

### 1.3 开发阶段（按 Phase）

本人采用增量式迭代，从 0 到 7 共 8 个 Phase 完成基础系统：

- **Phase 0-1**（本人）：核心引擎 + 地图 + 玩家 + 射击系统
- **Phase 2**（本人）：敌人系统（3 种基础敌人）
- **Phase 3**（本人）：道具系统 + 波次管理器
- **Phase 4**（本人）：商店系统（游戏内经济闭环）
- **Phase 5**（本人）：剩余敌人种类 + HUD 优化
- **Phase 6**（本人）：音频系统 + 存档/读档 + 菜单打磨
- **Phase 7**（本人）：平衡调校 + 统计面板 + 屏幕震动 + 文档
- **维护期**（本人）：敌人卡墙修复、商店 bug 修复、波次溢出修复、生成位置检查
- **扩展期**（队友）：选关系统 + 本地存档 + 成就系统

### 1.4 Git 提交统计

- **本人提交**：22 次（Phase 0-7 + 维护修复），占比 **~79%**
- **队友提交**：4 次（RTaoTao 3 次 + xushaoyang15 2 次，含 1 次空文件占位），占比 **~21%**
- **总提交**：27 次
- 所有功能 Phase 由本人独立完成，通过 GitHub PR 合并到 main（PR #3/#4/#5 为自查合并）；队友提交直接推送到 main

---

## 二、实现与测试逻辑

### 2.1 架构设计（本人设计并实现的底层）

采用**无引擎纯手写**方案，核心架构为：

```
main.js (入口 + 状态机主控)
  → engine.js (主循环 + 游戏世界更新 + 关卡模式参数)
    → player.js (玩家更新 + 渲染)
    → enemy.js (敌人 AI + 生成)
    → bullet.js (子弹生命周期)
    → powerup.js (道具系统)
    → shop.js (商店状态 + 经济)
    → wave-manager.js (波次调度)
    → map.js (地图碰撞)
    → audio.js (音效层)
    → input.js (输入层)
  → achievement.js (成就系统 — 队友扩展)
```

状态机设计（本人原始）：`MENU → PLAY → (SHOP) → PLAY → PAUSE → GAMEOVER`

状态机扩展（队友）：新增 `LEVEL_SELECT → PLAY → LEVEL_CLEAR → WIN`，以及关卡完成后的分支逻辑。关卡模式通过 `engine.levelMode` 参数注入，兼容原有无尽模式（`endless: true`）。

### 2.2 本人关键实现细节

1. **敌人 AI**：采用简单追逐 + 随机偏移策略，根据玩家位置实时计算方向向量，避免使用复杂寻路算法以保证 Canvas 60fps 性能。
2. **波次难度曲线**：线性递增 + 精英怪插值，每 5 波插入一次 Spikey，通过 wave-manager 中的 `getWaveConfig(waveNum)` 动态生成参数。
3. **商店经济闭环**：击杀 → 金币掉落 → 波次结束自动进入商店 → 购买属性升级 → 进入下一波。货币不溢出，形成完整 gameplay loop。
4. **音频系统**：Web Audio API 自建音频图（AudioContext → GainNode → Destination），支持 BGM 与 SFX 分离音量控制。
5. **存档接口设计**：本人在 Phase 6 预留了 localStorage 基础接口（最高分/当前进度），队友在此基础上扩展了关卡解锁进度和成就持久化。

### 2.3 队友关键实现细节

**RTaoTao — 选关与存档系统**：
- 5 关递进设计：每关配置 `startWave` / `endWave`，与本人原有的 wave-manager 波次系统无缝衔接
- 存档数据结构：`{ unlockedLevel, highestClearedLevel, totalCoinsEarned }`，通过 `engine.updateSaveOnLevelComplete()` / `engine.updateSaveOnGameOver()` 在状态切换时自动写入
- 关卡解锁机制：完成第 N 关后自动解锁第 N+1 关，最高通关记录持久化
- 兼容层设计：原有无尽模式保留，通过 `endless: true/false` 参数区分

**xushaoyang15 — 成就系统**：
- 8 个成就条件与本人 engine 的 `stats` / `saveData` 数据结构对接（如 `enemiesKilled`、`waveNum`、`shopPurchases`）
- Toast 通知系统：3 秒渐显渐隐动画，支持队列（多个成就连续解锁时依次显示）
- 成就列表界面：独立绘制方法 `drawList()`，ESC/SPACE 返回主菜单

### 2.4 测试与质量审查方式

- **手动 Playtest**：每个 Phase 完成后进行至少 3 轮完整游戏流程测试（从 MENU 到 GAMEOVER），验证状态切换、经济闭环、难度曲线。
- **边界测试**：故意触发边界条件（如金币为负、生命值为 0、波次溢出）验证鲁棒性。
- **回归测试**：每次修复后重新运行完整流程，确保不引入新问题（如 `enemies no longer spawn inside walls` 修复后验证所有生成点）。
- **CHANGELOG 维护**：本人每次提交记录变更内容，便于回溯与审查。
- **队友代码审查**：队友提交后本人拉取并验证功能正常（选关、存档、成就解锁流程完整运行）。

---

## 三、后续开发、未完成工作与接手注意事项

### 3.1 已完成功能（闭环）

- [x] **核心引擎与游戏循环**（本人）
- [x] **玩家系统**（本人）：移动、射击、受伤、死亡
- [x] **三种基础敌人 + 精英怪**（本人）
- [x] **道具系统**（本人）：5 种增益道具
- [x] **商店系统**（本人）：属性升级经济闭环
- [x] **波次管理**（本人）：难度曲线 + 波间商店
- [x] **音频系统**（本人）：BGM + SFX
- [x] **菜单与 HUD 渲染**（本人）
- [x] **选关系统**（队友）：5 关递进 + 无尽模式切换
- [x] **本地存档**（队友）：关卡解锁进度 + 最高分 + 总金币
- [x] **成就系统**（队友）：8 个成就 + Toast 通知 + 列表展示

### 3.2 未完成 / 可扩展项

| 优先级 | 功能 | 说明 |
|---|---|---|
| P1 | 移动端虚拟摇杆 | 当前仅支持键盘+触摸方向，需增加虚拟摇杆 UI |
| P2 | 更多敌人种类 | 已有基础框架，增加新敌人仅需继承 enemy.js 模板 |
| P2 | 关卡编辑器 | 当前 5 关硬编码在 main.js 的 `LEVELS` 数组中，可扩展为外部 JSON 加载 |
| P3 | 多人联机 | 需要 WebSocket 架构，当前为单机架构 |
| P3 | 成就云同步 | 当前仅为 localStorage，可扩展为后端账号系统同步 |

### 3.3 接手注意事项

1. **无框架依赖**：纯原生 JS，接手者需熟悉 Canvas 2D API 与 requestAnimationFrame。
2. **状态机为核心**：所有逻辑挂在 main.js 的状态分支中，新增状态需同步修改 `GameState` 枚举 + `update()` / `draw()` 分支 + `changeState()` 边界。队友新增的状态（LEVEL_SELECT/LEVEL_CLEAR/WIN）是良好参考。
3. **关卡模式参数注入**：`engine.reset(options)` 接受 `{endless, name, startWave, endWave, isFinal, levelId}`，与 wave-manager 的 `startWave()` 对接。修改关卡配置只需编辑 `LEVELS` 数组。
4. **存档数据结构**：`saveData` 由队友设计，包含 `unlockedLevel`、`highestClearedLevel`、`totalCoinsEarned`。成就系统另有独立的 `prairieKingLite_achievements` localStorage key。
5. **成就条件扩展**：新增成就只需在 `achievement.js` 的 `ACHIEVEMENTS` 数组中添加 `{id, name, desc, condition}`，`condition` 函数接收 `engine` 实例，可访问所有游戏状态。
6. **碰撞检测为 AABB**：简单矩形碰撞，若需精确碰撞需重写 `utils.js` 中的 `checkCollision`。
7. **资源路径硬编码**：图片/音频路径写在各模块顶部，修改目录结构时需同步更新。
8. **全局变量谨慎**：`main.js` 暴露少量全局变量用于调试，生产环境建议改为模块化导入。

---

## 四、项目学习成长报告

### 4.1 对项目自身的理解

本项目是一个**完整的单机射击游戏**，核心挑战不在于某一项技术的深度，而在于**多个子系统的耦合与状态一致性**。最大的体会是：**游戏不是功能的堆叠，而是闭环的咬合**。商店系统单独看很简单，但它必须嵌入波次结束→购买→下一波的时间线中，任何一个环节断裂都会导致体验崩塌。

从 Prairie King（星露谷物语内置小游戏）的参考分析到最终实现，我学会了**如何从参考作品中提取核心 loop 而非复制表面**。Prairie King 的精髓是「紧张-奖励-升级-更紧张」的循环，我保留了这一节奏，简化了非核心的 Roguelike 元素，使代码量可控在课程设计范围内。

**队友扩展系统的价值**：选关系统和成就系统的加入，将原本的单机无尽模式扩展为**有明确进度感的闯关体验**。我设计的 wave-manager 波次系统和 engine 的 `stats` 数据结构为队友的扩展提供了良好的接口基础，这验证了**模块化设计的前瞻性**——如果 Phase 3-4 时把波次和统计写死，后续加选关和成就就需要大规模重构。

### 4.2 从合作中学到的东西

虽然核心代码由本人独立完成，但在团队后期协作中学到了：

- **接口预留的重要性**：我在 Phase 6 预留的 `saveData` 和 `stats` 结构，恰好成为队友实现存档和成就系统的数据基础。如果当时没有抽象出 `totalCoinsEarned`、`enemiesKilled` 等统计量，队友需要修改我的核心代码才能接入。
- **PR 自查的价值**：即使是一个人开发，通过 PR 强制自己写清楚变更说明（CHANGELOG），能显著降低后期维护的认知负担。队友直接推送到 main 的方式虽然快，但缺少变更记录，review 时需要读 diff 才能理解意图。
- **模块化边界的重要性**：前期将 engine / player / enemy 等模块职责划分清楚，后期 Phase 7 的平衡调整无需重写整个系统，只需修改 enemy.js 和 wave-manager.js 的参数。队友的选关系统也只需要修改 main.js 和 engine.js 的入口层，无需触碰游戏世界内部逻辑。
- **队友代码的参考价值**：RTaoTao 的选关系统展示了如何用最小改动扩展状态机（新增 3 个状态而非重写原有状态），xushaoyang15 的成就系统展示了独立模块的设计模式（自包含的加载/检测/展示/持久化）。

### 4.3 独立开发的流程认知与能力匹配

**是否能独立完成类似项目？能。**

经过本项目的锻炼，我已具备以下能力链条：

1. **需求拆解**：能将游戏设计文档（ Prairie King 参考）拆解为可实现的模块清单（Phase 0-7）。
2. **增量开发**：每个 Phase 都是一个可交付版本（MVP 思维），不追求一次到位。
3. **调试能力**：纯手写无框架时，遇到问题需直接读源码而非查文档，培养了底层调试能力。
4. **性能意识**：Canvas 渲染需手动管理对象池与渲染批次，理解了 60fps 的硬约束。
5. **接口设计意识**：为后续扩展预留数据结构和钩子（`stats`、`saveData`、`reset(options)`），降低协作成本。

**待提升的能力**：
- 单元测试框架的引入（当前纯手动测试，后续应接入 Jest + Canvas mock）
- TypeScript 的类型安全（纯 JS 在大型项目中易出隐性 bug）
- 游戏设计能力（关卡难度曲线设计目前依赖线性递增，缺乏"心流"理论指导）

---

**报告人**：宿 (juice094)  
**日期**：2026-05-31  
**项目仓库**：[https://github.com/juice094/course-design-canvas-game](https://github.com/juice094/course-design-canvas-game)
