import hashlib

# 计算BLAKE2b（默认64字节输出）
data = "Hello, BLAKE2!".encode()
blake2b_hash = hashlib.blake2b(data).hexdigest()  # 128字符（512位）
print(f"BLAKE2b: {blake2b_hash}")

# 计算BLAKE2s（默认32字节输出）
blake2s_hash = hashlib.blake2s(data).hexdigest()  # 64字符（256位）
print(f"BLAKE2s: {blake2s_hash}")
