
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

# Define three points from the original image
pts1 = np.float32([
    [50, 50],
    [200, 50],
    [50, 200]
])

# Define three destination points
pts2 = np.float32([
    [10, 100],
    [200, 50],
    [100, 250]
])

# Calculate affine transformation matrix
M = cv2.getAffineTransform(pts1, pts2)

# Apply affine transformation
transformed = cv2.warpAffine(img, M, (cols, rows))

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
plt.title("Affine Transformed Image")
plt.axis("off")

plt.tight_layout()
plt.show()
