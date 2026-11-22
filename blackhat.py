
import cv2
import numpy as np

# Read the input image
img = cv2.imread("image.jpg")

if img is None:
    print("Error: Image not found!")
    exit()

# Convert image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Create a structuring element
kernel = np.ones((5, 5), np.uint8)

# Apply Black Hat operation
blackhat = cv2.morphologyEx(
    gray, cv2.MORPH_BLACKHAT, kernel
)

# Display the images
cv2.imshow("Original Image", img)
cv2.imshow("Grayscale Image", gray)
cv2.imshow("Black Hat Operation", blackhat)

# Save the output
cv2.imwrite("blackhat_output.jpg", blackhat)

cv2.waitKey(0)
cv2.destroyAllWindows()
