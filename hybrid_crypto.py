from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

from cryptography.fernet import Fernet

from cryptography.hazmat.primitives import serialization


# -------------------------
# Load RSA Keys
# -------------------------

def load_public_key():

    with open("keys/public_key.pem", "rb") as f:

        return serialization.load_pem_public_key(f.read())


def load_private_key():

    with open("keys/private_key.pem", "rb") as f:

        return serialization.load_pem_private_key(

            f.read(),

            password=None

        )


# -------------------------
# Generate AES Session Key
# -------------------------

def generate_session_key():

    return Fernet.generate_key()


# -------------------------
# Encrypt AES Key using RSA
# -------------------------

def encrypt_session_key(session_key):

    public_key = load_public_key()

    encrypted_key = public_key.encrypt(

        session_key,

        padding.OAEP(

            mgf=padding.MGF1(

                algorithm=hashes.SHA256()

            ),

            algorithm=hashes.SHA256(),

            label=None

        )

    )

    return encrypted_key


# -------------------------
# Decrypt AES Key
# -------------------------

def decrypt_session_key(encrypted_key):

    private_key = load_private_key()

    session_key = private_key.decrypt(

        encrypted_key,

        padding.OAEP(

            mgf=padding.MGF1(

                algorithm=hashes.SHA256()

            ),

            algorithm=hashes.SHA256(),

            label=None

        )

    )

    return session_key
def decrypt_session_key(encrypted_key):

    private_key = load_private_key()

    session_key = private_key.decrypt(
        ...
    )

    return session_key


# -------------------------
# Encrypt Message using AES Session Key
# -------------------------

def encrypt_message(session_key, message):

    cipher = Fernet(session_key)

    return cipher.encrypt(message.encode())


# -------------------------
# Decrypt Message
# -------------------------

def decrypt_message(session_key, encrypted_message):

    cipher = Fernet(session_key)

    return cipher.decrypt(encrypted_message).decode()



if __name__ == "__main__":

    print("Generating AES Session Key...")

    session_key = generate_session_key()

    print("Original Session Key:")
    print(session_key)

    encrypted_key = encrypt_session_key(session_key)

    print("\nEncrypted Session Key:")
    print(encrypted_key)

    decrypted_key = decrypt_session_key(encrypted_key)

    print("\nDecrypted Session Key:")
    print(decrypted_key)

    if session_key == decrypted_key:
        print("\nSUCCESS: Keys match!")
    else:
        print("\nERROR: Keys do not match!")