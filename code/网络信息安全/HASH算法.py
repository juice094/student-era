import hashlib

def get_digest(data, algorithm="sha256"):
    """计算字符串的消息摘要"""
    hasher = hashlib.new(algorithm)
    hasher.update(data.encode())
    return hasher.hexdigest()  # 返回16进制字符串

# 示例
text = "区块链ABC123"
print(f"SHA-256: {get_digest(text)}")
print(f"MD5:     {get_digest(text, 'md5')}")  # 仅演示，勿用MD5！
