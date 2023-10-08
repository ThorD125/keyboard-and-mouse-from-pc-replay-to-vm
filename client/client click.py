import socket
import tkinter as tk

# Define host and port to connect to the server
HOST = '127.0.0.1'  # Use the server's IP address or 'localhost' for testing
PORT = 12345

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Function to send 'pressed' signal to the server
def send_pressed_signal():
    client_socket.send('pressed'.encode())

# Function to send 'released' signal to the server
def send_released_signal():
    client_socket.send('released'.encode())

# Create the main GUI window
root = tk.Tk()
root.title("Client")

# Create a button in the GUI
button = tk.Button(root, text="Press Me")
button.pack()

# Bind functions to button press and release events
button.bind("<ButtonPress-1>", lambda event: send_pressed_signal())
button.bind("<ButtonRelease-1>", lambda event: send_released_signal())

# Function to close the client socket and exit the application
def close_client():
    client_socket.close()
    root.destroy()

# Create a Quit button to close the client
quit_button = tk.Button(root, text="Quit", command=close_client)
quit_button.pack()

# Connect to the server
client_socket.connect((HOST, PORT))

# Start the GUI main loop
root.mainloop()
