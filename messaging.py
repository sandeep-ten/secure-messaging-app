from cryptography.fernet import Fernet


def generate_key():
    return Fernet.generate_key()


def encrypt_message(key, message):
    cipher = Fernet(key)
    encrypted = cipher.encrypt(message.encode())
    return encrypted


def decrypt_message(key, encrypted_message):
    cipher = Fernet(key)
    decrypted = cipher.decrypt(encrypted_message)
    return decrypted.decode()


if __name__ == "__main__":
    key = generate_key()

    message = input("Enter message: ")

    encrypted = encrypt_message(key, message)

    print("\nEncrypted:")
    print(encrypted)

    decrypted = decrypt_message(key, encrypted)

    print("\nDecrypted:")
    print(decrypted)