import socket

HOST = "127.0.0.1"
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print(f"Server listening on {HOST}:{PORT}")

client, address = server.accept()

print(f"Connected by {address}")

while True:
    data = client.recv(1024)

    if not data:
        break

    print("Received:", data.decode())

    client.send(data)

client.close()
server.close()