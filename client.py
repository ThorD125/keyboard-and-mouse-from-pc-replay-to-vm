from client_library import *
import keyboard

client_socket = connect_to_server("192.168.32.156", 12345)
# client_socket = connect_to_server("127.0.0.1", 12345)

previous_state = False

while True:
    current_state = keyboard.is_pressed("x")
    if current_state != previous_state:
        if current_state:
            message = "press:w"
            client_socket.send(message.encode('utf-8'))
        else:
            message = "release:w"
            client_socket.send(message.encode('utf-8'))
    previous_state = current_state

client_socket.close()
