import random
import math

def is_prime(n, k=5):
    """Miller-Rabin 素性测试"""
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0:
        return False
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for __ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def generate_large_prime(bits=1024):
    """生成一个大素数"""
    while True:
        p = random.getrandbits(bits)
        if is_prime(p):
            return p

def extended_gcd(a, b):
    """扩展欧几里得算法"""
    if b == 0:
        return a, 1, 0
    else:
        g, x, y = extended_gcd(b, a % b)
        return g, y, x - (a // b) * y

def mod_inverse(a, m):
    """求模逆元"""
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise ValueError("模逆不存在")
    return x % m

def generate_rsa_keys(bit_length=1024):
    """生成RSA密钥对"""
    p = generate_large_prime(bit_length)
    q = generate_large_prime(bit_length)
    while p == q:
        q = generate_large_prime(bit_length)
    n = p * q
    phi_n = (p - 1) * (q - 1)
    e = 65537
    while math.gcd(e, phi_n) != 1:
        e += 2
    d = mod_inverse(e, phi_n)
    return (e, n), (d, n)

def rsa_encrypt(m, public_key):
    """RSA加密"""
    e, n = public_key
    if m >= n:
        raise ValueError("明文必须小于 n")
    return pow(m, e, n)

def rsa_decrypt(c, private_key):
    """RSA解密"""
    d, n = private_key
    return pow(c, d, n)

# 示例
if __name__ == "__main__":
    public_key, private_key = generate_rsa_keys(bit_length=16)
    print(f"公钥 (e, n): {public_key}")
    print(f"私钥 (d, n): {private_key}")

    plaintext = 12345
    ciphertext = rsa_encrypt(plaintext, public_key)
    print(f"明文: {plaintext} → 密文: {ciphertext}")

    decrypted = rsa_decrypt(ciphertext, private_key)
    print(f"密文: {ciphertext} → 解密后: {decrypted}")
