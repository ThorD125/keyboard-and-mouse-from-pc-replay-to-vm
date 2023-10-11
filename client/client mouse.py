import socket
import pyautogui
import struct
import time


def main():
    # host = '127.0.0.1'
    host = '192.168.32.156'
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    previous_mouse_pos = None
    previous_mouse_x = None
    previous_mouse_y = None


    try:
        while True:
            x, y = pyautogui.position()
            data = f"{x},{y}"

            if data != previous_mouse_pos:
                # message = struct.pack('!I', len(data)) + data.encode('utf-8')
                # client_socket.sendall(message)

                if previous_mouse_x != None and previous_mouse_y != None:
                    if previous_mouse_pos != data:
                        previous_mouse_x = x
                        previous_mouse_y = y


                        timeddata = f"{data}"

                        print(f"Sending: {timeddata}")
                        message = struct.pack('!I', len(timeddata)) + timeddata.encode('utf-8')
                        

                        client_socket.sendall(message)
                elif previous_mouse_x == None and previous_mouse_y == None:
                    previous_mouse_x = x
                    previous_mouse_y = y
                # print(f"Received: {x}, {y}")    
                # pyautogui.moveTo(int(x), int(y))
                previous_mouse_pos = data
                
    except KeyboardInterrupt:
        pass
    finally:
        print("Closing connection...")
        client_socket.close()

if __name__ == "__main__":
    main()









