import socket
import pygetwindow as gw
import pyautogui
import time
import keyboard



def create_server_socket(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    return server_socket

def press(button):
    keyboard.press(button)
    time.sleep(0.3)

def release(button):
    keyboard.release(button)
    time.sleep(0.3)


