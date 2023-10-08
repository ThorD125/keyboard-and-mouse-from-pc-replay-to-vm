import pygetwindow as gw
import pyautogui
import time
import keyboard
import socket



def press(button):
    keyboard.press_and_release(button)
    time.sleep(0.3)

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
host = '192.168.32.156'  # Loopback address for localhost
port = 12345  # You can use any available port

server_socket.bind((host, port))

# Find the window by its title
window = gw.getWindowsWithTitle("Warframe")[0]
# window = gw.getWindowsWithTitle("Notepad")[0]

# Activate the window
window.activate()
# Get the screen size
screen_width, screen_height = pyautogui.size()

# Calculate the center coordinates
center_x = screen_width // 2
center_y = screen_height // 2

# Click at the center of the screen
time.sleep(1)

pyautogui.click(center_x, center_y)
time.sleep(1)
# press('t')

# Listen for incoming connections
server_socket.listen(5)

print(f"Server listening on {host}:{port}")

# Accept a connection from a client
client_socket, client_address = server_socket.accept()
print(f"Accepted connection from {client_address}")




while True:
    # Receive data from the client
    
    data = client_socket.recv(1024).decode('utf-8')
    
    if not data:
        break  # Connection closed by client
    
    # Print the received data
    # print(f"Received: {data}")
    if len(data) ==1:
        press(data)
    else:
        for x in data:
            press(x)
    



print("done")
# Close the sockets
client_socket.close()
server_socket.close()
