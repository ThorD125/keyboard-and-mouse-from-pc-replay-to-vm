import socket

# Define server address and port
SERVER_HOST = '127.0.0.1'  # Replace with the server's IP address or hostname
SERVER_PORT = 12345

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((SERVER_HOST, SERVER_PORT))

# Send the picture data to the server
with open("clientscreenshot.png", "rb") as file:
    data = file.read(1024)
    while data:
        client_socket.send(data)
        data = file.read(1024)

print("[+] Picture sent to the server.")

# Close the socket
client_socket.close()
