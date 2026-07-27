import socket
from messaging import encrypt, decrypt

HOST = "127.0.0.1"
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

message = input("Enter message: ")

encrypted = encrypt(message)

client.send(encrypted)

reply = client.recv(4096)

print()

print("Server Reply:")

print(decrypt(reply))