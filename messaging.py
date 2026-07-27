from cryptography.fernet import Fernet

KEY_FILE = "keys/secret.key"


def generate_key():
    key = Fernet.generate_key()

    with open(KEY_FILE, "wb") as f:
        f.write(key)


def load_key():
    with open(KEY_FILE, "rb") as f:
        return f.read()


def encrypt(message):
    key = load_key()
    cipher = Fernet(key)

    return cipher.encrypt(message.encode())


def decrypt(ciphertext):
    key = load_key()
    cipher = Fernet(key)

    return cipher.decrypt(ciphertext).decode()


if __name__ == "__main__":

    generate_key()

    print("Secret key generated successfully.")