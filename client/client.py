import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('192.168.32.156', 12345)
client_socket.connect(server_address)

while True:
    message = input("Enter a message to send to the server (or type 'exit' to quit): ")
    
    if message == 'exit':
        break

    client_socket.send(message.encode('utf-8'))

client_socket.close()
