# Question 1 - Encryption/Decryption
def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

def encrypt(text, n, m):
    result = ""
    for char in text:
        if char.islower():
            if 'a' <= char <= 'm':
                shift = (ord(char) - ord('a') + n * m) % 13 + ord('a')
                result += chr(shift)
            elif 'n' <= char <= 'z':
                shift = (ord(char) - ord('n') - (n + m)) % 13 + ord('n')
                result += chr(shift)
            else:
                result += char
        elif char.isupper():
            if 'A' <= char <= 'M':
                shift = (ord(char) - ord('A') - n) % 13 + ord('A')
                result += chr(shift)
            elif 'N' <= char <= 'Z':
                shift = (ord(char) - ord('N') + m ** 2) % 13 + ord('N')
                result += chr(shift)
            else:
                result += char
        else:
            result += char
    return result

def decrypt(text, n, m):
    result = ""
    for char in text:
        if char.islower():
            if 'a' <= char <= 'm':
                shift = (ord(char) - ord('a') - n * m) % 13 + ord('a')
                result += chr(shift)
            elif 'n' <= char <= 'z':
                shift = (ord(char) - ord('n') + (n + m)) % 13 + ord('n')
                result += chr(shift)
            else:
                result += char
        elif char.isupper():
            if 'A' <= char <= 'M':
                shift = (ord(char) - ord('A') + n) % 13 + ord('A')
                result += chr(shift)
            elif 'N' <= char <= 'Z':
                shift = (ord(char) - ord('N') - m ** 2) % 13 + ord('N')
                result += chr(shift)
            else:
                result += char
        else:
            result += char
    return result

def check_correctness(original, decrypted):
    return original == decrypted

# 示例调用（n=2, m=3）
n = 2
m = 3
original_text = read_file("raw_text.txt")
encrypted_text = encrypt(original_text, n, m)
write_file("encrypted_text.txt", encrypted_text)
decrypted_text = decrypt(encrypted_text, n, m)
write_file("decrypted_text.txt", decrypted_text)

if check_correctness(original_text, decrypted_text):
    print("✅ 解密成功，内容匹配原文")
else:
    print("❌ 解密失败")
