# Student Era 架构审视与协作优化方案

> 生成时间: 2026-05-18
> 范围: 仓库结构、协作工作流、Agent 上下文管理

---

## 一、当前架构诊断

### 1.1 仓库性质定位

student-era 本质上是一个**"个人课程设计归档 + 实验环境配置"**的混合型仓库。它同时承载三种不同性质的内容：

| 类型 | 代表项目 | 特征 |
|------|----------|------|
| **构建型项目** | bigdata-visualization | 有 package.json、构建流程、依赖管理 |
| **可运行脚本** | computational-methods, ml-apple-detection | Python 源码 + 数据，可直接执行 |
| **文档/导航型** | gis-lab-navigator, information-retrieval | 纯 HTML/Markdown，无需构建 |
| **环境配置型** | docs/ENVIRONMENT.md | 记录 WSL2 环境状态 |

**核心矛盾**: 同一个仓库同时管理"需要版本控制的代码"和"不需要版本控制的实验数据/截图"，边界模糊。

### 1.2 技术债清单

| 优先级 | 问题 | 影响 |
|--------|------|------|
| **高** | `pnpm-workspace.yaml` 包含 `projects/*`，但 Python 项目无 package.json | pnpm 会在 Python 目录报错或跳过 |
| **高** | 实验数据（`data/`）分散在各子项目，通过 `.gitignore` 排除 | 数据备份依赖人工，无统一恢复路径 |
| **中** | 无 CI/CD，代码变更无自动验证 | 计算方法实验的 Python 脚本可能因环境变化失效 |
| **中** | 环境配置状态（WSL 组件版本）与文档不同步 | ENVIRONMENT.md 需要手动更新 |
| **低** | 文档格式不统一（有的用 Markdown，有的用 HTML 导航页） | 维护成本高，但短期内可接受 |

### 1.3 Agent 协作痛点

从本仓库的多次会话历史来看，以下问题反复出现：

1. **上下文恢复成本高**: 每次新会话需要重新读取 ENVIRONMENT.md、STATUS 报告、各项目 README
2. **环境状态不可验证**: 文档声称"Hadoop 运行正常"，但 Agent 无法自动验证
3. **跨项目依赖隐式**: 计算方法依赖 WSL Ubuntu-24.04，GIS 依赖 Windows GUI，但依赖关系未显式声明
4. **历史决策不可追溯**: 为什么选择清华 PyPI 镜像？为什么 Kafka 用 KRaft？这些决策原因散落在会话历史中

---

## 二、成熟管理方法参考

### 2.1 学术/课程仓库参考

| 模式 | 来源 | 适用场景 |
|------|------|----------|
| **GitHub Classroom** | GitHub Education | 课程作业分发与收集，自动评分 |
| **Cookiecutter Data Science** | DrivenData | 数据科学项目标准化目录结构 |
| **Research Compendium** | rOpenSci | 可复现研究：代码 + 数据 + 环境 + 论文 |
| **DevContainer** | Microsoft | VS Code 一键启动标准化开发环境 |

student-era 最接近 **Research Compendium** 模式，但缺少环境声明（如 Dockerfile 或 Conda environment.yml）。

### 2.2 Monorepo 管理参考

| 工具 | 适用规模 | 特点 |
|------|----------|------|
| **Turborepo** | 中小型 | 前端为主，支持远程缓存 |
| **Nx** | 中大型 | 支持多种语言，依赖图可视化 |
| **Bazel** | 大型 | 企业级，学习成本高 |
| **just** | 小型 | 命令运行器，Makefile 替代品 |

对 student-era 而言，**just** 或 **Taskfile** 比完整 monorepo 工具更合适。

### 2.3 个人知识管理（PKM）参考

| 系统 | 核心思想 | 借鉴点 |
|------|----------|--------|
| **Zettelkasten** | 原子化笔记 + 双向链接 | 每个实验作为独立"原子"，通过链接关联 |
| **PARA** | Projects / Areas / Resources / Archives | 区分"进行中"和"已归档" |
| **Dendron** | 层次化笔记 + Schema | 统一命名规范，降低检索成本 |

---

## 三、优化建议（分阶段）

### Phase 1: 立即执行（本周内）

#### 3.1.1 引入 CLAUDE.md

在仓库根目录创建 `.claude/CLAUDE.md`，作为 Agent 的"入职手册"。

```markdown
# Student Era — Agent 协作指南

## 仓库性质
个人课程设计归档。混合代码项目（Vue/Python/Shell）与文档型项目（实验指导/导航页）。

## 关键路径
- 环境配置总览: docs/ENVIRONMENT.md
- 项目状态快照: docs/STATUS-YYYY-MM-DD.md
- 计算方法实验: projects/computational-methods/src/exp{1,2,3,4}.py
- 大数据组件: WSL Ubuntu-24.04 /opt/*

## Agent 操作规范
1. 修改代码前，先读取对应项目的 README.md
2. 环境配置变更必须同步更新 ENVIRONMENT.md
3. 新增项目需在 README.md 的 Project Index 表格中登记
4. 敏感信息（密码、密钥）不得提交到 git

## 环境验证命令
```bash
# WSL Ubuntu-24.04
wsl -d Ubuntu-24.04 -u root jps
wsl -d Ubuntu-24.04 -u root /opt/miniconda/bin/python -c "import torch, numpy"

# WSL kali-linux
wsl -d kali-linux -u zjx nmap --version
```
```

**为什么重要**: 每次新会话的 Agent 需要 ~5-10 次文件读取才能理解项目全貌。CLAUDE.md 可将这个成本降到 1 次。

#### 3.1.2 统一命令入口（Taskfile）

```yaml
# Taskfile.yml
version: '3'

tasks:
  env:check:
    desc: 验证所有环境组件
    cmds:
      - wsl -d Ubuntu-24.04 -u root jps
      - wsl -d Ubuntu-24.04 -u root /opt/miniconda/bin/python -c "import torch, numpy, scipy, matplotlib"
      - wsl -d kali-linux -u zjx nmap --version

  bigdata:start:
    desc: 启动 Hadoop
    cmds:
      - wsl -d Ubuntu-24.04 -u root start-dfs.sh
      - wsl -d Ubuntu-24.04 -u root start-yarn.sh

  ml:train:
    desc: 运行 ML 短训练
    dir: projects/ml-apple-detection/src
    cmds:
      - /opt/miniconda/bin/python train.py --epochs 2

  cm:test:
    desc: 运行计算方法测试
    dir: projects/computational-methods/src
    cmds:
      - /opt/miniconda/bin/python -c "import matplotlib; matplotlib.use('Agg'); import exp1_root_finding; exp1_root_finding.main()"
      - /opt/miniconda/bin/python -c "import matplotlib; matplotlib.use('Agg'); import exp2_linear_systems; exp2_linear_systems.main()"
```

**为什么重要**: Agent 不需要记住复杂的 WSL 路径，只需 `task cm:test`。

#### 3.1.3 修复 pnpm-workspace

```yaml
# pnpm-workspace.yaml
packages:
  - 'packages/*'
  - 'projects/bigdata-visualization'
```

将 Python/纯文档项目从 workspace 中移除，避免 pnpm 报错。

### Phase 2: 短期优化（本月内）

#### 3.2.1 结构化环境状态存储

将 ENVIRONMENT.md 中的表格数据提取为 YAML，便于 Agent 解析：

```yaml
# .claude/environment-state.yml
generated_at: "2026-05-18"
wsl2:
  version: "2.7.3.0"
  networking_mode: mirrored
  memory: 16GB
  cpus: 20
  distros:
    - name: Ubuntu-24.04
      user: root
      purpose: [bigdata, ml]
    - name: kali-linux
      user: zjx
      hostname: kali-zjx
      purpose: [network-security]

components:
  java:
    version: "21.0.10"
    path: /usr/lib/jvm/java-21-openjdk-amd64
  hadoop:
    version: "3.4.1"
    path: /opt/hadoop
    mode: pseudo-distributed
    status: running  # 需手动维护或自动化检测
  spark: { version: "4.1.1", path: /opt/spark }
  kafka: { version: "4.2.0", path: /opt/kafka, mode: kraft }
  # ...

python_packages:
  torch: "2.12.0+cpu"
  numpy: "2.4.4"
  scipy: "1.17.1"
  matplotlib: "3.10.9"
  # 由 `pip freeze` 自动生成
```

**Agent 收益**: 不再需要正则表达式解析 Markdown 表格，直接 `yaml.safe_load()`。

#### 3.2.2 实验数据管理策略

当前问题: `data/` 被 `.gitignore` 排除，但实验报告需要引用这些数据。

方案对比:

| 方案 | 优点 | 缺点 | 推荐度 |
|------|------|------|--------|
| Git LFS | 版本控制大文件 | 需要 GitHub LFS 配额 | 中 |
| 外部存储 + 清单 | 不占用仓库空间 | 需要额外备份步骤 | **高** |
| 压缩归档 + 清单 | 简单，可放 release | 更新不便 | 中 |

**推荐方案**: 外部存储 + 清单文件

```
projects/ml-apple-detection/
├── data/              # .gitignore 排除
├── data-manifest.yml  # git 跟踪
└── README.md
```

```yaml
# data-manifest.yml
description: "Apple quality detection dataset (8 classes, ~170 images)"
total_size: "102MB"
source: "course-assigned"  # 或 URL
backup_location: "D:/backups/student-era/ml-data-2026-05-18.tar"
files:
  - path: data/raw/
    count: 170
    format: jpg
  - path: data/test/
    count: 20
    format: jpg
```

#### 3.2.3 引入 DevContainer 配置（可选）

如果未来需要在其他机器上复现环境：

```json
// .devcontainer/devcontainer.json
{
  "name": "Student Era BigData+ML",
  "image": "mcr.microsoft.com/devcontainers/base:ubuntu",
  "features": {
    "ghcr.io/devcontainers/features/java:1": { "version": "21" },
    "ghcr.io/devcontainers/features/python:1": { "version": "3.13" }
  },
  "postCreateCommand": "bash scripts/setup-wsl-env.sh",
  "customizations": {
    "vscode": {
      "extensions": ["ms-python.python", "Vue.volar"]
    }
  }
}
```

**注意**: DevContainer 是 Docker 容器，无法完全替代 WSL2（特别是 Kali Linux 网络安全实验）。但对于计算方法、大数据组件等纯软件环境，可作为补充。

### Phase 3: 长期优化（结课后）

#### 3.3.1 自动化环境验证

将 STATUS 报告中的手动验证转化为脚本：

```bash
#!/bin/bash
# scripts/verify-environment.sh

FAILED=0

check_service() {
    local name=$1
    local cmd=$2
    if eval "$cmd" >/dev/null 2>&1; then
        echo "  [PASS] $name"
    else
        echo "  [FAIL] $name"
        FAILED=1
    fi
}

echo "=== Hadoop Services ==="
check_service "NameNode" "wsl -d Ubuntu-24.04 -u root jps | grep NameNode"
check_service "DataNode" "wsl -d Ubuntu-24.04 -u root jps | grep DataNode"
check_service "ResourceManager" "wsl -d Ubuntu-24.04 -u root jps | grep ResourceManager"

echo "=== Python Packages ==="
check_service "PyTorch" "wsl -d Ubuntu-24.04 -u root /opt/miniconda/bin/python -c 'import torch'"
check_service "NumPy" "wsl -d Ubuntu-24.04 -u root /opt/miniconda/bin/python -c 'import numpy'"

echo "=== Kali Tools ==="
check_service "nmap" "wsl -d kali-linux -u zjx nmap --version"
check_service "john" "wsl -d kali-linux -u zjx john --version"

exit $FAILED
```

#### 3.3.2 实验结果归档系统

课程结束后，实验结果（截图、报告 PDF）需要与代码一起归档：

```
docs/archive/
├── 2026-spring/
│   ├── bigdata-visualization/
│   │   ├── report.pdf
│   │   └── screenshots/
│   ├── ml-apple-detection/
│   │   ├── report.pdf
│   │   ├── tensorboard-screenshots/
│   │   └── confusion-matrix.png
│   └── ...
```

使用 Git LFS 或外部存储管理二进制文件。

---

## 四、Agent 长期协作优化

### 4.1 核心问题: Agent 的"失忆"

当前每次新会话的 Agent 面临以下信息损失:

1. **历史决策不可见**: 为什么选择华为云镜像？为什么放弃 Aliyun？原因在旧会话中
2. **环境状态不确定**: Agent 无法确认 Hadoop 当前是否正在运行
3. **个人偏好未知**: 用户喜欢简洁回复、不接受emoji、偏好 CAP-v2 格式

### 4.2 解决方案: 三层记忆架构

```
Layer 1: 项目级持久化 (.claude/)
  ├── CLAUDE.md           # 项目总览 + Agent 操作规范
  ├── environment-state.yml  # 结构化环境状态
  └── decisions/          # 关键决策记录 (ADR 风格)
      ├── 001-kafka-kraft-over-zookeeper.md
      ├── 002-huawei-cloud-mirror.md
      └── 003-pypi-tsinghua-mirror.md

Layer 2: 会话级上下文 (.claude/sessions/)
  ├── 2026-05-17-bigdata-upgrade.md   # 本次会话摘要
  └── 2026-05-18-gis-computational.md

Layer 3: 用户级记忆 (~/.claude/memory/)
  ├── user-profile.md     # 角色、偏好、知识背景
  └── feedback/           # 用户纠正或确认的偏好
      ├── terse-responses.md
      └── prefer-bundled-prs.md
```

### 4.3 具体实施: 决策记录 (ADR)

```markdown
# ADR-001: Kafka 4.2.0 使用 KRaft 模式替代 ZooKeeper

## 状态
Accepted (2026-05-17)

## 背景
课程教材可能使用 Kafka 2.x + ZooKeeper 模式，但实际安装时发现 Kafka 4.x 已完全移除 ZK 支持。

## 决策
采用 KRaft 模式（单节点 broker+controller）。

## 后果
- 正面: 无需维护 ZooKeeper 集群，配置更简单
- 负面: 与教材描述不一致，实验报告需特别说明版本差异

## 替代方案
- 方案 B: 安装 Kafka 3.x 保留 ZK 兼容性（被拒绝：版本太老）
```

### 4.4 Agent 自校验清单

在 `.claude/CLAUDE.md` 中添加：

```markdown
## Agent 自检清单（每次任务开始前）

- [ ] 已读取 docs/ENVIRONMENT.md 确认环境版本
- [ ] 已读取 docs/STATUS-*.md 确认最近会话状态
- [ ] 若修改代码，已检查对应项目的 README.md
- [ ] 若修改配置，已确认不会破坏其他项目
- [ ] 提交前已检查 .gitignore 是否排除了敏感文件/大文件
```

---

## 五、推荐优先级

| 优先级 | 事项 | 预计时间 | 收益 |
|--------|------|----------|------|
| **P0** | 创建 `.claude/CLAUDE.md` | 10 min | **极高** — 降低每次会话的上下文重建成本 |
| **P0** | 修复 `pnpm-workspace.yaml` | 2 min | 高 — 消除 pnpm 报错 |
| **P1** | 创建 `Taskfile.yml` | 20 min | 高 — 统一命令入口 |
| **P1** | 结构化 `environment-state.yml` | 30 min | 高 — Agent 可解析 |
| **P2** | 实验数据清单 `data-manifest.yml` | 20 min | 中 — 数据可追溯 |
| **P2** | 决策记录 `decisions/` | 30 min | 中 — 历史决策可见 |
| **P3** | 环境验证脚本 | 30 min | 中 — 自动化验证 |
| **P3** | DevContainer 配置 | 1h | 低 — 环境可复现 |

---

## 六、立即执行项

如同意，我将在 5 分钟内完成 P0 + P1 项：

1. 创建 `.claude/CLAUDE.md`
2. 修复 `pnpm-workspace.yaml`
3. 创建 `Taskfile.yml`
4. 创建 `environment-state.yml`
5. 提交到 GitHub
