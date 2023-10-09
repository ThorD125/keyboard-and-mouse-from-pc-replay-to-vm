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

    processing_packets = True  # Flag to control packet processing

    try:
        while True:
            serverinput = client_socket.recv(4)
            if not serverinput:
                break
            
            message_length = struct.unpack('!I', serverinput)[0]
            data = client_socket.recv(message_length).decode('utf-8')
            
            coords = data.split(',')
            if len(coords) == 2:
                x, y = coords[0], coords[1]
                print(f"Received: {x}, {y}")

                if processing_packets:
                    pyautogui.moveTo(int(x), int(y), 0)
            else:
                print(f"Received unexpected data: {data}")

            # Add logic to temporarily disable packet processing during mouse movements
            if pyautogui._pyautogui_x != previous_mouse_x or pyautogui._pyautogui_y != previous_mouse_y:
                print("Mouse is moving, pausing packet processing...")
                processing_packets = False
            else:
                processing_packets = True

            previous_mouse_x = pyautogui._pyautogui_x
            previous_mouse_y = pyautogui._pyautogui_y

    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()
        server_socket.close()

if __name__ == "__main__":
    main()
