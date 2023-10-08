import keyboard

while True:
    if keyboard.is_pressed("x"):
        print(f"x is pressed!")
    else:
        print(f"x is not pressed!")
