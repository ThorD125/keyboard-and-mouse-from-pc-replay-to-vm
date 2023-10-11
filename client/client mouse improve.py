import mouse
import socket
import struct

globals()['prev_mouse_pos'] = None

host = '192.168.32.156'
port = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

counter = 0
skip = 15

def send_mouse(x):
    try:
        data = f"{x.x},{x.y}"

        if data != globals()['prev_mouse_pos'] and globals()['counter'] == globals()['skip']:
            globals()['prev_mouse_pos'] = data
            
            print(data)

            message = struct.pack('!I', len(data)) + data.encode('utf-8')
            client_socket.sendall(message)
            globals()['counter'] = 0
        globals()['counter'] += 1
    except Exception as e:
        print(f"an error occured: {e}")
        raise e


mouse.hook(send_mouse)
mouse.wait(button=mouse.RIGHT, target_types=(mouse.DOWN,))
mouse.unhook(send_mouse)
client_socket.close()


# print(recorded)
