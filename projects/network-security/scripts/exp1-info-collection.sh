#!/bin/bash
# ============================================================================
# 实验一：网络公开信息收集
# 课程：网络信息安全
# 姓名缩写：zjx
# ============================================================================

set -euo pipefail

echo "========================================"
echo "  实验一：网络公开信息收集"
echo "  操作人：zjx"
echo "========================================"

TARGET_DOMAIN="example.com"
TARGET_IP="127.0.0.1"

echo ""
echo "【步骤 1】whois 查询域名注册信息"
echo "----------------------------------------"
echo "\$ whois \${TARGET_DOMAIN}"
whois "\${TARGET_DOMAIN}" 2>&1 | head -30 || echo "[提示] whois 查询需联网，此处仅演示命令格式"

echo ""
echo "【步骤 2】nslookup 域名解析"
echo "----------------------------------------"
echo "\$ nslookup \${TARGET_DOMAIN}"
nslookup "\${TARGET_DOMAIN}" 2>&1 || echo "[提示] 无法解析，演示命令格式"

echo ""
echo "【步骤 3】host 命令查询 DNS 记录"
echo "----------------------------------------"
echo "\$ host \${TARGET_DOMAIN}"
host "\${TARGET_DOMAIN}" 2>&1 || echo "[提示] 无法解析，演示命令格式"

echo ""
echo "【步骤 4】dig 详细 DNS 查询"
echo "----------------------------------------"
echo "\$ dig \${TARGET_DOMAIN} +short"
dig "\${TARGET_DOMAIN}" +short 2>&1 || echo "[提示] 无法解析，演示命令格式"

echo ""
echo "【步骤 5】nmap 主机发现（仅扫描本机，安全合规）"
echo "----------------------------------------"
echo "\$ nmap -sn \${TARGET_IP}"
sudo nmap -sn "\${TARGET_IP}"

echo ""
echo "【步骤 6】nmap 端口扫描（仅扫描本机，安全合规）"
echo "----------------------------------------"
echo "\$ nmap -sS -O \${TARGET_IP}"
sudo nmap -sS -O "\${TARGET_IP}" || nmap -sT "\${TARGET_IP}"

echo ""
echo "【步骤 7】nmap 服务版本探测"
echo "----------------------------------------"
echo "\$ nmap -sV \${TARGET_IP}"
nmap -sV "\${TARGET_IP}"

echo ""
echo "========================================"
echo "  实验一完成"
echo "========================================"
