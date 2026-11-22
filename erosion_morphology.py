
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the input image
img = cv2.imread("image.jpg")

# Check whether image is loaded
if img is None:
    print("Error: Image not found!")
    exit()

# Convert image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply binary thresholding
ret, binary = cv2.threshold(
    gray, 127, 255, cv2.THRESH_BINARY
)

# Create a structuring element (kernel)
kernel = np.ones((5, 5), np.uint8)

# Apply erosion operation
erosion = cv2.erode(
    binary, kernel, iterations=1
)

# Display original image
plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Original Image")
plt.axis("off")

# Display binary image
plt.subplot(1, 3, 2)
plt.imshow(binary, cmap="gray")
plt.title("Binary Image")
plt.axis("off")

# Display eroded image
plt.subplot(1, 3, 3)
plt.imshow(erosion, cmap="gray")
plt.title("Eroded Image")
plt.axis("off")

plt.tight_layout()
plt.show()

# Save the output
cv2.imwrite("erosion_output.jpg", erosion)

print("Erosion operation completed successfully!")
