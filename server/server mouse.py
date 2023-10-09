import struct
import socket
import pyautogui
import time

def main():
    host = '0.0.0.0'  # Listen on all available network interfaces
    port = 12345  # Port for communication
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)  # Listen for one connection at a time

    print(f"Server listening on {host}:{port}")

    app_window = pyautogui.getWindowsWithTitle("Paint")[0]
    app_window.activate()

    client_socket, addr = server_socket.accept()
    print(f"Connection from {addr}")


    previous_mouse_x = None
    previous_mouse_y = None

    try:
        while True:
            serverinput = client_socket.recv(4)
            if not serverinput:
                break
            
            # print(data)
            # # Unpack the message length
            message_length = struct.unpack('!I', serverinput)[0]

            # Receive the actual message data
            data = client_socket.recv(message_length).decode('utf-8')
            
            coords = data.split(',')
            if len(coords) == 2:
                x, y = coords[0], coords[1]
                print(f"Received: {x}, {y}")    
                pyautogui.moveTo(int(x), int(y), 0)
                # pyautogui.mouseDown()
                # time.sleep(0.01)
                # pyautogui.mouseUp()

            else:
                print(f"Received unexpected data: {data}")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        # pyautogui.mouseUp()
        client_socket.close()
        server_socket.close()

if __name__ == "__main__":
    main()
