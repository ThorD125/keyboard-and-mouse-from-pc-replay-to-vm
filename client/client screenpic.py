import socket
import pyautogui
from PIL import ImageGrab
import io
import time

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((SERVER_HOST, SERVER_PORT))

app_window = pyautogui.getWindowsWithTitle('Warframe')[0]

app_window.activate()
time.sleep(0.1)

left, top, right, bottom = app_window.left, app_window.top, app_window.right, app_window.bottom
screenshot = ImageGrab.grab(bbox=(left, top, right, bottom))
new_width = screenshot.width // 2
new_height = screenshot.height // 2
resized_screenshot = screenshot.resize((new_width, new_height))

image_stream = io.BytesIO()
resized_screenshot.save(image_stream, format='PNG')
image_data = image_stream.getvalue()

client_socket.send(image_data)

print("[+] Picture sent to the server.")

client_socket.close()
