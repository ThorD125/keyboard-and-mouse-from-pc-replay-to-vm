import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
host = '192.168.32.156'  # Loopback address for localhost
port = 12345  # You can use any available port

server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen(5)

print(f"Server listening on {host}:{port}")

# Accept a connection from a client
client_socket, client_address = server_socket.accept()
print(f"Accepted connection from {client_address}")

while True:
    # Receive data from the client
    data = client_socket.recv(1024).decode('utf-8')
    
    if not data:
        break  # Connection closed by client
    
    # Print the received data
    print(f"Received: {data}")
    

# Close the sockets
client_socket.close()
server_socket.close()
