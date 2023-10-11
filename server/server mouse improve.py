
import socket
import pyautogui


host = '0.0.0.0'
port = 12345


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(1)


app_window = pyautogui.getWindowsWithTitle("Warframe")[0]
app_window.activate()


client_socket, addr = server_socket.accept()


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
            # win32api.SetCursorPos((int(x), int(y)))
            _os_mouse.move_to(event.x, event.y)
            #     _os_mouse.release(event.button)
            # else:
            #     _os_mouse.press(event.button)
            moves = 0
            print(f"Received unexpected tdata: {x}, {y}")
        moves += 1


except Exception as e:
    print(f"Error: {e}")
finally:
    client_socket.close()
    server_socket.close()







