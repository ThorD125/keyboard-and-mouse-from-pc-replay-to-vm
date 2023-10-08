import socket

# Define host and port for the server
HOST = '127.0.0.1'  # Use your server's IP address or 'localhost' for testing
PORT = 12345

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address and port
server_socket.bind((HOST, PORT))

# Listen for incoming connections
server_socket.listen()

print(f"Server is listening on {HOST}:{PORT}")

# Accept a client connection
client_socket, client_address = server_socket.accept()
print(f"Connected to {client_address}")

try:
    while True:
        # Receive data from the client
        data = client_socket.recv(1024).decode()

        # Check if the received data is 'pressed'
        if data == 'pressed':
            print("Button pressed on the client!")
            # You can perform any action you want here

except KeyboardInterrupt:
    print("Server stopped")

finally:
    # Close the server socket
    server_socket.close()
