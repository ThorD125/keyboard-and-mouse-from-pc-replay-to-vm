import struct
import socket
import pyautogui
import time
import win32api

pyautogui.FAILSAFE = False

def main():
    host = '0.0.0.0'  # Listen on all available network interfaces
    port = 12345  # Port for communication
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)  # Listen for one connection at a time

    print(f"Server listening on {host}:{port}")

    app_window = pyautogui.getWindowsWithTitle("Warframe")[0]
    app_window.activate()

    client_socket, addr = server_socket.accept()
    print(f"Connection from {addr}")

    moves = 0
    skippers = 0

    try:
        while True:
            serverinput = client_socket.recv(4)
            if not serverinput:
                break
            
            message_length = struct.unpack('!I', serverinput)[0]
            data = client_socket.recv(message_length).decode('utf-8')

            coords = data.split(',')
            if len(coords) == 2:
                #  and moves == skippers:
                x, y = coords[0], coords[1]
                # pyautogui.moveTo(int(x), int(y),0)
                pyautogui.mouseDown()
                win32api.SetCursorPos((int(x), int(y)))
                pyautogui.mouseUp()
                moves = 0
                print(f"Received unexpected tdata: {x}, {y}")
            moves += 1

         

    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()
        server_socket.close()

if __name__ == "__main__":
    main()
