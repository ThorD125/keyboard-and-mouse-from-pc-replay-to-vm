from client_library import connect_to_server


client_socket = connect_to_server("192.168.32.156", 12345)
previous_state = False


while True:
    current_state = keyboard.is_pressed("x")  # Get the current state of the "x" key
    
    if current_state != previous_state:  # Compare current state to previous state
        if current_state:
            message = "press:t"
            client_socket.send(message.encode('utf-8'))
        else:
            message = "release:t"
            client_socket.send(message.encode('utf-8'))
    
    previous_state = current_state  # Update the previous state



client_socket.close()
