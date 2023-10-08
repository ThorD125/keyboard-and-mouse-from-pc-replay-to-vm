from server_library import create_server_socket

# server_socket = create_server_socket('192.168.32.156', 12345)
server_socket = create_server_socket('127.0.0.1', 12345)

client_socket, client_address = server_socket.accept()


state = False

while True:
    data = client_socket.recv(1024).decode('utf-8')
    
    if not data:
        break

    
    
    print(f"Received: {data}")




client_socket.close()
server_socket.close()
