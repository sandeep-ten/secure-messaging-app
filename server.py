import socket
from messaging import decrypt, encrypt

HOST = "127.0.0.1"
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print(f"Server listening on {HOST}:{PORT}")

client, address = server.accept()

print(f"Connected by {address}")

while True:

    encrypted = client.recv(4096)

    if not encrypted:
        break

    print("\nEncrypted message:")
    print(encrypted)

    plaintext = decrypt(encrypted)

    print("\nDecrypted message:")
    print(plaintext)

    response = encrypt("Message received successfully.")

    client.send(response)

client.close()
server.close()