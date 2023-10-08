from server_library import *
import pygetwindow
import pyautogui
import time
import keyboard

server_socket = create_server_socket('192.168.32.156', 12345)
# server_socket = create_server_socket('127.0.0.1', 12345)

window = pygetwindow.getWindowsWithTitle("Warframe")[0]
window.activate()
screen_width, screen_height = pyautogui.size()
center_x = screen_width // 2
center_y = screen_height // 2


client_socket, client_address = server_socket.accept()
pyautogui.click(center_x, center_y)


while True:
    data = client_socket.recv(1024).decode('utf-8')
    
    if not data: 
        break

    if data == "press:w":
        press("w")
    elif data == "release:w":
        release("w")
    
    print(f"Received: {data}")

client_socket.close()
server_socket.close()

