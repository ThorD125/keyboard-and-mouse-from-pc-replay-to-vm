from client_library import connect_to_server


client_socket = connect_to_server("192.168.32.156", 12345)

while True:
    message = input("Enter a message to send to the server (or type 'exit' to quit): ")
    
    if message == 'exit':
        break

    client_socket.send(message.encode('utf-8'))

client_socket.close()

