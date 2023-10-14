import cv2
import numpy as np
import pyautogui

# Load the two images you want to compare
image1 = cv2.imread('recieved/first.png')
image2 = cv2.imread('recieved/right.png')

# Convert the images to grayscale for easier comparison
gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

# Calculate the absolute difference between the two images
diff = cv2.absdiff(gray1, gray2)

# Define a threshold to identify significant differences (you may need to adjust this)
threshold = 30

# Create a binary mask where differences above the threshold are set to 255 (white)
_, thresholded = cv2.threshold(diff, threshold, 255, cv2.THRESH_BINARY)

# Find contours in the thresholded image to identify areas of movement
contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Initialize an empty list to store the mouse movement
mouse_movement = []

# Iterate through the detected contours (representing movement)
for contour in contours:
    # Calculate the centroid of the contour (potential mouse movement)
    M = cv2.moments(contour)
    if M["m00"] != 0:
        cx = int(M["m10"] / M["m00"])
        cy = int(M["m01"] / M["m00"])
        mouse_movement.append((cx, cy))

# Print the detected mouse movement
# print("Mouse Movement:")
# for movement in mouse_movement:
#     print(movement)

for point in mouse_movement:
    pyautogui.moveTo(point[0], point[1], duration=0.2)
