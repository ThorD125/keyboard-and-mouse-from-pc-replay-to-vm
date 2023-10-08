import pyautogui
from PIL import ImageGrab

# Replace 'Your App Window Title' with the title of the application window you want to capture
app_window = pyautogui.getWindowsWithTitle('Warframe')[0]

# Get the coordinates of the application window
left, top, right, bottom = app_window.left, app_window.top, app_window.right, app_window.bottom

# Capture the screenshot
screenshot = ImageGrab.grab(bbox=(left, top, right, bottom))

new_width = screenshot.width // 2
new_height = screenshot.height // 2
resized_screenshot = screenshot.resize((new_width, new_height))

# Replace 'screenshot.png' with the desired file name and format
# screenshot.save('screenshot.png')
resized_screenshot.save('screenshot.png')
