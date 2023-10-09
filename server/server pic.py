import socket
import time

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((SERVER_HOST, SERVER_PORT))

server_socket.listen(5)
print(f"[*] Listening on {SERVER_HOST}:{SERVER_PORT}")

client_socket, client_address = server_socket.accept()
print(f"[*] Accepted connection from {client_address[0]}:{client_address[1]}")

timestamp = time.time()

with open(f"{timestamp}.png", "wb") as file:
    while True:
        data = client_socket.recv(1024)
        if not data:
            break

        file.write(data)

print("[+] Picture received and saved.")

client_socket.close()
server_socket.close()
