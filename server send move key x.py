import pygetwindow as gw
import pyautogui
import time
import keyboard

def press(button):
    keyboard.press(button)
    time.sleep(0.3)

def release(button):
    keyboard.release(button)
    time.sleep(0.3)

# Find the window by its title
window = gw.getWindowsWithTitle("Warframe")[0]

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
# time.sleep(1)

press('w')

i = 1
while i < 10:
    press('w')
    i += 1
release('w')

print("done")
