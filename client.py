from client_library import *
import keyboard

client_socket = connect_to_server("192.168.32.156", 12345)
# client_socket = connect_to_server("127.0.0.1", 12345)

previous_state_w = False

while True:
    current_state_w = keyboard.is_pressed("w")
    if current_state_w != previous_state_w:
        if current_state_w:
            message = "press:w"
            client_socket.send(message.encode('utf-8'))
        else:
            message = "release:w"
            client_socket.send(message.encode('utf-8'))
    previous_state_w = current_state_w

client_socket.close()
