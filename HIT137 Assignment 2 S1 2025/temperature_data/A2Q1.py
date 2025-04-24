def encrypt_text(text, n, m):
    encrypted = ""
    for char in text:
        if char.islower():
            if 'a' <= char <= 'm':
                shift = n*m
                new_char = chr((ord(char) - ord('a') + shift) % 26 +ord('a'))
            elif 'n' <= char <= 'z':
                shift = n + m
                new_char = chr((ord(char) - ord('a')- shift) % 26 + ord('a'))
            encrypted += new_char
        elif char.isupper():
            if "A" <= char <= 'M':
                shift  = n
                new_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
                
            elif 'N' <= char <= 'Z':
                shift = m ** 2
                new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            encrypted += new_char
        else:
            encrypted += char
    return encrypted

def decrypt_text(text, n, m):
    decrypted = ""
    for char in text:
        if char.islower():
            if 'a' <= char <= 'm':
                shift = n*m
                new_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            elif 'n' <= char <='z':
                shift = n + m
                new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            decrypted += new_char

        elif char.isupper():
            if 'A' <= char <= 'M':
                shift = n
                new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
                
            elif 'N' <= char <= 'Z':
                shift = m ** 2
                new_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            decrypted += new_char
        else:
            decrypted += char
    return decrypted

def check_correctness(original, decrypted):
    return original == decrypted

def main():
    try:
        n = int(input("Enter n: "))
        m = int(input("Enter m: "))

        with open("raw_text.txt", "r") as infile:
            original_text = infile.read()
        encrypted = encrypt_text(original_text, n, m)

        with open("encrypted_text.txt", "w") as outfile:
            outfile.write(encrypted)
    
        decrypted = decrypt_text(encrypted, n, m)
        print("原文：", repr(original_text))
        print("加密后：", repr(encrypted))
        print("解密后：", repr(decrypted))
        if check_correctness(original_text, decrypted):
            print("Success: Decrypted text matches the original.")
        else:
            print("Error: Decrypted text does not match.")
    except FileNotFoundError:
        print("Can't find  raw_text.txt file, please make sure file is under the same folder with A2Q1.py")
    except ValueError:
        print("Please enter valid integer")
    except Exception as e:
        print(f"Error reading program: {e}")
        
if __name__ == "__main__":
    main()



    