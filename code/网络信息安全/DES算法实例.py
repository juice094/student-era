import binascii

def str_to_bits(text):
    """将字符串转换为二进制位列表"""
    return [int(bit) for byte in text.encode() for bit in f"{byte:08b}"]

def bits_to_str(bits):
    """将二进制位列表转回字符串"""
    bytes_list = []
    for i in range(0, len(bits), 8):
        byte = bits[i:i+8]
        bytes_list.append(int(''.join(map(str, byte)), 2))
    return bytes(bytes_list).decode(errors='ignore')

def xor(bits1, bits2):
    """按位异或"""
    return [b1 ^ b2 for b1, b2 in zip(bits1, bits2)]

def left_shift(bits, n):
    """循环左移"""
    return bits[n:] + bits[:n]

def fake_s_box(bits):
    """简化的S盒（实际DES有8个S盒，这里仅做示例）"""
    return bits[:4]  # 直接截取前4位（实际应为6位输入→4位输出）

def generate_key(key_bits):
    """生成简化版子密钥（实际DES有16轮）"""
    return left_shift(key_bits, 2)  # 简单左移2位代替真实密钥生成

def feistel(right, subkey):
    """简化版Feistel函数"""
    expanded = right * 2  # 简单扩展（实际DES用E表扩展32→48位）
    xored = xor(expanded, subkey)
    s_output = fake_s_box(xored)  # 假S盒处理
    return s_output * 8  # 简单填充（实际DES用P置换）

def mini_des(block, key, encrypt=True):
    """简化版DES加密/解密"""
    L, R = block[:8], block[8:]  # 分成左右8位（实际DES为32位）
    subkey = generate_key(key)
    
    for _ in range(2):  # 仅2轮（实际DES为16轮）
        new_R = xor(L, feistel(R, subkey))
        L, R = R, new_R
    
    return L + R  # 最终不交换（实际DES会交换）

# 示例使用
if __name__ == "__main__":
    plaintext = "AB"  # 2字节（16位）输入
    key = "K"         # 1字节（8位）密钥
    
    # 转二进制
    plain_bits = str_to_bits(plaintext)[:16]  # 截取16位
    key_bits = str_to_bits(key)[:8]           # 截取8位
    
    # 加密
    cipher_bits = mini_des(plain_bits, key_bits, encrypt=True)
    print(f"明文: {plaintext} → 二进制: {plain_bits}")
    print(f"密文: {bits_to_str(cipher_bits)} → 二进制: {cipher_bits}")
    
    # 解密
    decrypted_bits = mini_des(cipher_bits, key_bits, encrypt=False)
    print(f"解密: {bits_to_str(decrypted_bits)} → 二进制: {decrypted_bits}")
