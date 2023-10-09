import socket

# Define server address and port
SERVER_HOST = '127.0.0.1'  # Listen on all available interfaces
SERVER_PORT = 12345

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the server socket to the address and port
server_socket.bind((SERVER_HOST, SERVER_PORT))

# Listen for incoming connections
server_socket.listen(5)
print(f"[*] Listening on {SERVER_HOST}:{SERVER_PORT}")

# Accept a connection from a client
client_socket, client_address = server_socket.accept()
print(f"[*] Accepted connection from {client_address[0]}:{client_address[1]}")

# Receive the picture data from the client and save it to a file

import time

while True:
    data = client_socket.recv(1024)
    if not data:
        break

    timestamp = time.time()
    with open("{timestamp}.png", "wb") as file:
        file.write(data)

print("[+] Picture received and saved.")

# Close the sockets
client_socket.close()
server_socket.close()
