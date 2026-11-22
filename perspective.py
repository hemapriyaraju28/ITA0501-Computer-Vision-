
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the input image
img = cv2.imread("image.jpg")

# Check whether image is loaded
if img is None:
    print("Error: Image not found!")
    exit()

# Get image dimensions
rows, cols = img.shape[:2]

# Define four points in the original image
pts1 = np.float32([
    [50, 50],
    [cols - 50, 50],
    [50, rows - 50],
    [cols - 50, rows - 50]
])

# Define four destination points
pts2 = np.float32([
    [0, 0],
    [cols - 1, 0],
    [50, rows - 1],
    [cols - 100, rows - 1]
])

# Calculate perspective transformation matrix
M = cv2.getPerspectiveTransform(pts1, pts2)

# Apply perspective transformation
transformed = cv2.warpPerspective(img, M, (cols, rows))

# Convert BGR to RGB
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
transformed_rgb = cv2.cvtColor(transformed, cv2.COLOR_BGR2RGB)

# Display original image
plt.subplot(1, 2, 1)
plt.imshow(img_rgb)
plt.title("Original Image")
plt.axis("off")

# Display transformed image
plt.subplot(1, 2, 2)
plt.imshow(transformed_rgb)
plt.title("Perspective Transformed Image")
plt.axis("off")

plt.tight_layout()
plt.show()
