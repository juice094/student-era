#!/bin/bash
# ============================================================================
# 实验四：系统安全加固
# 课程：网络信息安全
# 姓名缩写：zjx
# ============================================================================

set -uo pipefail

echo "========================================"
echo "  实验四：系统安全加固"
echo "  操作人：zjx"
echo "  主机：\$(hostname)"
echo "========================================"

echo ""
echo "【步骤 1】查看当前登录用户"
echo "----------------------------------------"
echo "\$ who"
who

echo ""
echo "【步骤 2】查看系统开放端口"
echo "----------------------------------------"
echo "\$ netstat -tlnp || ss -tlnp"
ss -tlnp 2>&1 || netstat -tlnp 2>&1 || echo "[提示] 无网络工具可用"

echo ""
echo "【步骤 3】查看当前防火墙状态"
echo "----------------------------------------"
echo "\$ sudo iptables -L -n -v"
sudo iptables -L -n -v 2>&1 || echo "[提示] iptables 未配置"

echo ""
echo "【步骤 4】查看最近登录记录"
echo "----------------------------------------"
echo "\$ last -10"
last -10 2>&1 || echo "[提示] wtmp 日志为空"

echo ""
echo "【步骤 5】查看系统进程（异常检测）"
echo "----------------------------------------"
echo "\$ ps aux --sort=-%cpu | head -15"
ps aux --sort=-%cpu | head -15

echo ""
echo "【步骤 6】检查 SUID 文件（潜在提权风险）"
echo "----------------------------------------"
echo "\$ find / -perm -4000 -type f 2>/dev/null | head -20"
find /usr -perm -4000 -type f 2>/dev/null | head -20

echo ""
echo "【步骤 7】查看系统服务"
echo "----------------------------------------"
echo "\$ systemctl list-units --type=service --state=running | head -20"
systemctl list-units --type=service --state=running 2>&1 | head -20 || echo "[提示] systemctl 不可用"

echo ""
echo "【步骤 8】检查密码策略"
echo "----------------------------------------"
echo "\$ cat /etc/login.defs | grep -E 'PASS_MAX_DAYS|PASS_MIN_DAYS|PASS_MIN_LEN'"
grep -E 'PASS_MAX_DAYS|PASS_MIN_DAYS|PASS_MIN_LEN' /etc/login.defs 2>&1 || echo "[提示] 配置文件路径不同"

echo ""
echo "========================================"
echo "  实验四完成"
echo "  建议：根据检查结果制定加固方案"
echo "========================================"
