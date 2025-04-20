"""
Name:Shaobin Chen
Date started: 17/04
GitHub URL:https://github.com/MarukiIroha/HIT137-Assignment-2-Group-9/
"""
INPUT_FILENAME = "raw_text.txt"

def main():
    try:
        n = int(input("Enter n (shift value): "))
        m = int(input("Enter m (shift value): "))
    except ValueError:
        print("Please enter valid integers for n and m.")
        return

    try:
        with open(INPUT_FILENAME, "r") as in_file:
            original_text = in_file.read()
            in_file.close()
    except FileNotFoundError:
        print("Error: raw_text.txt not found.")
        return
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    encrypted_text = encrypt_text(original_text, n, m)

    try:
        with open("encrypted_text.txt", "w") as out_file:
            out_file.write(encrypted_text)
            out_file.close()
    except Exception as e:
        print(f"Error writing to file: {e}")
        return

    decrypted_text = decrypt_text(encrypted_text, n, m)

    is_correct = check_decryption(original_text, decrypted_text)
    print(f"Decryption correct: {is_correct}")

    print("\nOriginal text:", original_text)
    print("Encrypted text:", encrypted_text)
    print("Decrypted text:", decrypted_text)


def encrypt_text(text, n, m):
    encrypted = ""
    for char in text:
        if char.islower():
            if 'a' <= char <= 'm':
                # Shift forward by n * m for lowercase a-m
                shift = (ord(char) - ord('a') + n * m) % 13 + ord('a')
                encrypted += chr(shift)
            elif 'n' <= char <= 'z':
                # Shift backward by n + m for lowercase n-z
                shift = (ord(char) - ord('n') - (n + m)) % 13 + ord('n')
                encrypted += chr(shift)
            else:
                encrypted += char
        elif char.isupper():
            if 'A' <= char <= 'M':
                # Shift backward by n for uppercase A-M
                shift = (ord(char) - ord('A') - n) % 13 + ord('A')
                encrypted += chr(shift)
            elif 'N' <= char <= 'Z':
                # Shift forward by m^2 for uppercase N-Z
                shift = (ord(char) - ord('N') + m ** 2) % 13 + ord('N')
                encrypted += chr(shift)
            else:
                encrypted += char
        else:
            encrypted += char
    return encrypted

def decrypt_text(encrypted_text, n, m):
    decrypted = ""
    for char in encrypted_text:
        if char.islower():
            if 'a' <= char <= 'm':
                # Reverse shift backward by n * m for lowercase a-m
                shift = (ord(char) - ord('a') - n * m) % 13 + ord('a')
                decrypted += chr(shift)
            elif 'n' <= char <= 'z':
                # Reverse shift forward by n + m for lowercase n-z
                shift = (ord(char) - ord('n') + (n + m)) % 13 + ord('n')
                decrypted += chr(shift)
            else:
                decrypted += char
        elif char.isupper():
            if 'A' <= char <= 'M':
                # Reverse shift forward by n for uppercase A-M
                shift = (ord(char) - ord('A') + n) % 13 + ord('A')
                decrypted += chr(shift)
            elif 'N' <= char <= 'Z':
                # Reverse shift backward by m^2 for uppercase N-Z
                shift = (ord(char) - ord('N') - m ** 2) % 13 + ord('N')
                decrypted += chr(shift)
            else:
                decrypted += char
        else:
            decrypted += char
    return decrypted

def check_decryption(original_text, decrypted_text):
    return original_text == decrypted_text

main()