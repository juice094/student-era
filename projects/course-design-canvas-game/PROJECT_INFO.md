---
title: "course-design-canvas-game — 项目信息"
date: 2026-05-31
type: project-info
---

# course-design-canvas-game — 草原王者射击游戏

## 基本信息

| 属性 | 内容 |
|---|---|
| **课程** | 课程设计（2026 春） |
| **类型** | Project / Game |
| **技术栈** | 原生 JavaScript + HTML5 Canvas |
| **GitHub** | [juice094/course-design-canvas-game](https://github.com/juice094/course-design-canvas-game) |
| **本地路径** | `C:\Users\22414\dev\course-design-canvas-game` |

## 角色与贡献

**周景潇（juice094）— 核心开发者 / 基础系统唯一实现者**

| 阶段 | 内容 | 占比 |
|---|---|---|
| Phase 0-7 | 独立完成全部基础架构与核心玩法系统（13 个模块，~100KB） | ~79% |
| 维护期 | 敌人卡墙修复、商店 bug 修复、波次溢出修复、生成位置检查 | — |
| 队友扩展 | 审查并合并队友提交的选关系统（RTaoTao）和成就系统（xushaoyang15） | — |

## 核心模块

- `engine.js` — 游戏主循环、状态机、渲染管线
- `player.js` — 玩家实体、移动、射击、动画状态机
- `enemy.js` — 敌人 AI、3 种基础敌人 + Spikey 精英怪
- `shop.js` — 商店经济闭环
- `wave-manager.js` — 波次难度曲线
- `audio.js` — Web Audio API 音频系统
- `main.js` — 入口与状态机主控

## 队友扩展（在本人 Phase 7 基础上）

- **RTaoTao**：选关系统（5 关递进 + 无尽模式切换）、本地存档（关卡解锁进度）
- **xushaoyang15**：成就系统（8 项成就 + Toast 通知 + 持久化）

## 提交统计

- 本人：22/27 次（79%）
- 队友：4/27 次（21%）

## 一键启动

```powershell
cd C:\Users\22414\dev\course-design-canvas-game
npx serve --listen 5176 --single
```

或参见 `course-design-web-frontend/start-demo.ps1`（统一启动脚本）。
