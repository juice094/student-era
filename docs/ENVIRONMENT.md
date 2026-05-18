# 实验环境配置汇总

> 本机实验环境配置速查表，涵盖 WSL2、大数据、机器学习、网络安全四大方向。

## WSL2 基础配置

| 项目 | 配置值 |
|------|--------|
| WSL 版本 | 2.7.3.0 |
| 网络模式 | mirrored |
| DNS 隧道 | enabled |
| 内存限制 | 16 GB |
| CPU 核心 | 20 |
| 交换空间 | 6 GB |

### 已安装发行版

| 发行版 | 用途 | 默认用户 | 主机名 |
|--------|------|----------|--------|
| Ubuntu-24.04 | 大数据 / 机器学习 | root | 继承 Windows |
| kali-linux | 网络安全 | zjx | kali-zjx |

## 大数据环境 (Ubuntu-24.04)

### Java
- **版本**: OpenJDK 21.0.10
- **路径**: `/usr/lib/jvm/java-21-openjdk-amd64`
- **兼容性注意**: Hadoop/YARN 需添加 `--add-opens` JVM 参数

### Hadoop
- **版本**: 3.4.1
- **路径**: `/opt/hadoop`
- **模式**: 伪分布式 (Pseudo-Distributed)
- **已验证**: HDFS / MapReduce / YARN 运行正常
- **启动命令**:
  ```bash
  start-dfs.sh
  start-yarn.sh
  ```

### 其他组件 (安装中)
| 组件 | 版本 | 路径 | 状态 | 备注 |
|------|------|------|------|------|
| Spark | 4.1.1 | /opt/spark | pending | 2026-01-09 |
| Flink | 2.2.1 | /opt/flink | pending | 2026-05-15 |
| Kafka | 4.2.0 | /opt/kafka | pending | KRaft mode, 2026-02-17 |
| ZooKeeper | 3.9.3 | /opt/zookeeper | pending | HBase 协调服务 |
| HBase | 2.6.2 | /opt/hbase | pending | |
| Hive | 4.2.0 | /opt/hive | pending | JDK 21 required, 2025-11-23 |

## 机器学习环境 (Ubuntu-24.04)

### Python
- **解释器**: `/opt/miniconda/bin/python`
- **版本**: Python 3.13.13
- **Conda**: base 环境

### 已安装包
| 包 | 版本 | 用途 |
|----|------|------|
| PyTorch | 2.12.0+cpu | 深度学习框架 |
| Tqdm | latest | 进度条 |
| OpenCV | 4.13.0 | 图像处理 |
| Matplotlib | 3.10.9 | 可视化 |
| Scikit-learn | 1.8.0 | 机器学习工具 |
| TensorBoard | 2.20.0 | 训练监控 |
| JupyterLab | 4.5.7 | 交互式开发 |

### 项目路径
```
~/dev/student-era/projects/ml-apple-detection/
```

### 快速开始
```bash
cd ~/dev/student-era/projects/ml-apple-detection/src
python train.py --epochs 50 --batch-size 8 --lr 0.001
```

## 网络安全环境 (kali-linux)

### 用户信息
- **用户名**: zjx
- **密码**: (由实验指导教师配置)
- **主机名**: kali-zjx
- **sudo**: 免密配置

### 已安装工具
| 工具 | 版本 | 用途 |
|------|------|------|
| nmap | 7.98 | 端口扫描 / 主机发现 |
| john | 1.9.0 | 密码哈希破解 |
| hping3 | 3.a2 | 网络包构造 / DoS 演示 |
| whois | - | 域名注册信息查询 |
| dnsutils | - | nslookup / host / dig |

### 实验脚本路径
```
/home/zjx/netsec-exp/scripts/
```

### 安全声明
> 所有攻击类实验仅限针对 `127.0.0.1` 或授权实验环境。严禁扫描、攻击任何公网地址或未经授权的系统。

## Claude Code 配置

### 已启用插件
- `code-review`
- `code-simplifier`
- `security-guidance`
- `claude-md-management`
- `pr-review-toolkit`

### MCP 服务器
- GitHub Copilot MCP (通过 `GITHUB_PERSONAL_ACCESS_TOKEN`)

### 设置文件
- 全局: `~/.claude/settings.json`
- 本地权限: `~/.claude/settings.local.json`
- MCP: `~/.claude/mcp.json`
