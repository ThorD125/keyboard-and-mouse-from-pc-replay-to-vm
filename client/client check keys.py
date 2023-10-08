import keyboard




# while True:
#     if keyboard.is_pressed("x"):
#         print(f"x is pressed!")
#     else:
#         print(f"x is not pressed!")
previous_state = False  # Initialize the previous state of the "x" key

while True:
    current_state = keyboard.is_pressed("x")  # Get the current state of the "x" key
    
    if current_state != previous_state:  # Compare current state to previous state
        if current_state:
            print("x is pressed!")
        else:
            print("x is not pressed!")
    
    previous_state = current_state  # Update the previous state
