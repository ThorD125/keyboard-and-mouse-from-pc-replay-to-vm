import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
server_address = ('192.168.32.156', 12345)  # Replace with the server's address and port
client_socket.connect(server_address)

while True:
    # Get user input
    message = input("Enter a message to send to the server (or type 'exit' to quit): ")
    
    if message == 'exit':
        break  # Exit the loop if the user types 'exit'
    
    # Send the message to the server
    client_socket.send(message.encode('utf-8'))

# Close the socket
client_socket.close()
