
import cv2
import numpy as np

# Read the input image
img = cv2.imread("image.jpg")

if img is None:
    print("Error: Image not found!")
    exit()

# Convert image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Convert grayscale image to binary
_, binary = cv2.threshold(
    gray, 127, 255, cv2.THRESH_BINARY
)

# Create a structuring element
kernel = np.ones((5, 5), np.uint8)

# Apply Opening operation
opening = cv2.morphologyEx(
    binary, cv2.MORPH_OPEN, kernel
)

# Display the images
cv2.imshow("Original Image", img)
cv2.imshow("Binary Image", binary)
cv2.imshow("Opening Operation", opening)

# Save the output
cv2.imwrite("opening_output.jpg", opening)

cv2.waitKey(0)
cv2.destroyAllWindows()
