import socket
import pyautogui
import struct

def main():
    # host = '127.0.0.1'
    host = '192.168.32.156'
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    previous_mouse_pos = None

    try:
        while True:
            x, y = pyautogui.position()
            data = f"{x},{y}"

            if data != previous_mouse_pos:
                print(f"Sending: {data}")

    
                message = struct.pack('!I', len(data)) + data.encode('utf-8')
                client_socket.sendall(message)

                previous_mouse_pos = data
    except KeyboardInterrupt:
        pass
    finally:
        print("Closing connection...")
        client_socket.close()

if __name__ == "__main__":
    main()
