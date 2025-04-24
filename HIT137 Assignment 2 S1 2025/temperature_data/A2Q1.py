def encrypt_text(text, n, m):
    encrypted = ""
    for char in text:
        if 'a' <= char <= 'm':
            shift = (ord(char) - ord('a') + n * m) % 13 + ord('a')
            encrypted += chr(shift)
        elif 'n' <= char <= 'z':
            shift = (ord(char) - ord('n') - (n + m)) % 13 + ord('n')
            encrypted += chr(shift)
        elif 'A' <= char <= 'M':
            shift = (ord(char) - ord('A') - n) % 13 + ord('A')
            encrypted += chr(shift)
        elif 'N' <= char <= 'Z':
            shift = (ord(char) - ord('N') + m ** 2) % 13 + ord('N')
            encrypted += chr(shift)
        else:
            encrypted += char 
    return encrypted


def decrypt_text(text, n, m):
    decrypted = ""
    for char in text:
        if 'a' <= char <= 'm':
            shift = (ord(char) - ord('a') - n * m) % 13 + ord('a')
            decrypted += chr(shift)
        elif 'n' <= char <= 'z':
            shift = (ord(char) - ord('n') + (n + m)) % 13 + ord('n')
            decrypted += chr(shift)
        elif 'A' <= char <= 'M':
            shift = (ord(char) - ord('A') + n) % 13 + ord('A')
            decrypted += chr(shift)
        elif 'N' <= char <= 'Z':
            shift = (ord(char) - ord('N') - m ** 2) % 13 + ord('N')
            decrypted += chr(shift)
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


        if check_correctness(original_text.strip(), decrypted.strip()):
            print("Success: Decrypted text matches the original.")
        else:
            print("Error: Decrypted text does not match.")
    except FileNotFoundError:
        print("raw_text.txt not found. Make sure the file is in the same folder.")
    except ValueError:
        print("Please enter valid integers for n and m.")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()



    


    
