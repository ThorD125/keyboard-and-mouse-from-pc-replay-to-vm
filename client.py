from client_library import *
import keyboard

client_socket = connect_to_server("192.168.32.156", 12345)
# client_socket = connect_to_server("127.0.0.1", 12345)

# previous_state_w = False

# while True:
#     current_state_w = keyboard.is_pressed("w")
#     if current_state_w != previous_state_w:
#         if current_state_w:
#             message = "press:w"
#             client_socket.send(message.encode('utf-8'))
#         else:
#             message = "release:w"
#             client_socket.send(message.encode('utf-8'))
#     previous_state_w = current_state_w

keys_to_monitor = ["w", "a", "s", "d"]
previous_states = {key: False for key in keys_to_monitor}

while True:
    for key in keys_to_monitor:
        current_state = keyboard.is_pressed(key)
        if current_state != previous_states[key]:
            if current_state:
                message = f"press:{key}"
                client_socket.send(message.encode('utf-8'))
            else:
                message = f"release:{key}"
                client_socket.send(message.encode('utf-8'))
        previous_states[key] = current_state



client_socket.close()
