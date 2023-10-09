import socket
import pyautogui
from PIL import ImageGrab
import io

# Define server address and port
SERVER_HOST = '127.0.0.1'  # Replace with the server's IP address or hostname
SERVER_PORT = 12345

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((SERVER_HOST, SERVER_PORT))

app_window = pyautogui.getWindowsWithTitle('Notepad')[0]

left, top, right, bottom = app_window.left, app_window.top, app_window.right, app_window.bottom
screenshot = ImageGrab.grab(bbox=(left, top, right, bottom))
new_width = screenshot.width // 2
new_height = screenshot.height // 2
resized_screenshot = screenshot.resize((new_width, new_height))

# Create an in-memory binary stream
image_stream = io.BytesIO()
resized_screenshot.save(image_stream, format='PNG')
image_data = image_stream.getvalue()

# Send the image data to the server
client_socket.send(image_data)

print("[+] Picture sent to the server.")

# Close the socket
client_socket.close()
