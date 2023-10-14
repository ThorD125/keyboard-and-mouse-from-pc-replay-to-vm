import pyautogui
from PIL import ImageGrab
import socket


def take_screenshot(nameapp, namepic):
    app_window = pyautogui.getWindowsWithTitle(nameapp)[0]
    left, top, right, bottom = app_window.left, app_window.top, app_window.right, app_window.bottom
    screenshot = ImageGrab.grab(bbox=(left, top, right, bottom))
    new_width = screenshot.width // 2
    new_height = screenshot.height // 2
    resized_screenshot = screenshot.resize((new_width, new_height))
    resized_screenshot.save(namepic)


def connect_to_server(ip, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (ip, port)
    client_socket.connect(server_address)
    return client_socket
















