
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

# Apply Sobel filter in X direction
sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)

# Apply Sobel filter in Y direction
sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

# Convert results to unsigned 8-bit images
sobel_x = cv2.convertScaleAbs(sobel_x)
sobel_y = cv2.convertScaleAbs(sobel_y)

# Combine X and Y gradients
sobel = cv2.addWeighted(sobel_x, 0.5, sobel_y, 0.5, 0)

# Display original and filtered images
plt.figure(figsize=(10, 6))

plt.subplot(2, 2, 1)
plt.imshow(gray, cmap="gray")
plt.title("Original Grayscale Image")
plt.axis("off")

plt.subplot(2, 2, 2)
plt.imshow(sobel_x, cmap="gray")
plt.title("Sobel X")
plt.axis("off")

plt.subplot(2, 2, 3)
plt.imshow(sobel_y, cmap="gray")
plt.title("Sobel Y")
plt.axis("off")

plt.subplot(2, 2, 4)
plt.imshow(sobel, cmap="gray")
plt.title("Sobel Filtered Image")
plt.axis("off")

plt.tight_layout()
plt.show()
