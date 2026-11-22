
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

# Apply Top Hat operation
tophat = cv2.morphologyEx(
    gray, cv2.MORPH_TOPHAT, kernel
)

# Display the images
cv2.imshow("Original Image", img)
cv2.imshow("Grayscale Image", gray)
cv2.imshow("Top Hat Operation", tophat)

# Save the output
cv2.imwrite("tophat_output.jpg", tophat)

cv2.waitKey(0)
cv2.destroyAllWindows()
