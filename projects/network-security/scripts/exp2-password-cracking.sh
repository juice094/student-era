#!/bin/bash
# ============================================================================
# 实验二：密码破解（John the Ripper）
# 课程：网络信息安全
# 姓名缩写：zjx
# 警告：仅用于教学实验，不得用于非法用途
# ============================================================================

set -euo pipefail

EXPDIR="/home/zjx/netsec-exp"
mkdir -p "\${EXPDIR}"

echo "========================================"
echo "  实验二：密码破解 (John the Ripper)"
echo "  操作人：zjx"
echo "========================================"

# 创建弱密码哈希用于演示
echo ""
echo "【步骤 1】生成测试密码哈希"
echo "----------------------------------------"
PASSWD_FILE="\${EXPDIR}/test_passwd.txt"
echo "admin:\$(openssl passwd -1 '123456')" > "\${PASSWD_FILE}"
echo "user1:\$(openssl passwd -1 'password')" >> "\${PASSWD_FILE}"
echo "zjx:\$(openssl passwd -1 'zjx123')" >> "\${PASSWD_FILE}"
echo "\$ cat \${PASSWD_FILE}"
cat "\${PASSWD_FILE}"

echo ""
echo "【步骤 2】使用 John 破解哈希"
echo "----------------------------------------"
echo "\$ john \${PASSWD_FILE}"
john "\${PASSWD_FILE}"

echo ""
echo "【步骤 3】查看破解结果"
echo "----------------------------------------"
echo "\$ john --show \${PASSWD_FILE}"
john --show "\${PASSWD_FILE}"

echo ""
echo "【步骤 4】使用自定义字典（如有）"
echo "----------------------------------------"
echo "\$ john --wordlist=/usr/share/wordlists/rockyou.txt \${PASSWD_FILE}"
echo "[提示] rockyou.txt 体积较大，此处仅展示命令格式"

echo ""
echo "========================================"
echo "  实验二完成"
echo "========================================"
