# caesar_cipher.py

def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            result += chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
        else:
            result += char
    return result

def main():
    while True:
        print("Caesar Cipher")
        print("1. Encrypt")
        print("2. Decrypt")
        choice = input("Choose an option: ")

        if choice == "1":
            text = input("Enter a message to encrypt: ")
            shift = int(input("Enter a shift value: "))
            encrypted_text = caesar_encrypt(text, shift)
            print("Encrypted text:", encrypted_text)
        elif choice == "2":
            text = input("Enter a message to decrypt: ")
            shift = int(input("Enter a shift value: "))
            decrypted_text = caesar_decrypt(text, shift)
            print("Decrypted text:", decrypted_text)
        else:
            print("Invalid option. Try again!")

if __name__ == "__main__":
    main()