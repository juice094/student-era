# 网络信息安全实验

## 环境信息

| 项目 | 值 |
|------|-----|
| 姓名缩写 | zjx |
| Kali 主机名 | kali-zjx |
| Kali 用户名 | zjx |
| Kali 密码 | zjx123456 |

## 实验目录

```
network-security/
├── scripts/
│   ├── exp1-info-collection.sh      # 实验一：网络公开信息收集
│   ├── exp2-password-cracking.sh    # 实验二：密码破解
│   ├── exp3-dos-attack.sh           # 实验三：DoS 攻击演示
│   └── exp4-system-hardening.sh     # 实验四：系统安全加固
├── exp1-info-collection/            # 实验一报告/截图
├── exp2-password-cracking/          # 实验二报告/截图
├── exp3-dos-attack/                 # 实验三报告/截图
├── exp4-system-hardening/           # 实验四报告/截图
└── docs/                            # 补充文档
```

## 已安装工具

- nmap 7.98
- john 1.9.0 (John the Ripper)
- hping3
- whois
- dnsutils (nslookup, host, dig)
- net-tools / iproute2

## 使用方法

在 Kali Linux WSL2 中执行：

```bash
# 进入实验目录
cd /mnt/c/Users/22414/dev/student-era/projects/network-security/scripts

# 实验一：信息收集
bash exp1-info-collection.sh

# 实验二：密码破解
bash exp2-password-cracking.sh

# 实验三：DoS 攻击演示
bash exp3-dos-attack.sh

# 实验四：系统加固
bash exp4-system-hardening.sh
```

## 安全声明

> **⚠️ 所有攻击类实验仅限针对 127.0.0.1 或授权实验环境！**
> **严禁使用上述工具扫描、攻击任何公网地址或未经授权的系统！**
> **违反者将承担相应法律责任。**

## 实验报告截图要求

每个实验脚本已添加清晰的分隔线和步骤标题，输出适合直接截图贴入实验报告。
