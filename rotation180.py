
import cv2
import matplotlib.pyplot as plt

# Read the input image
img = cv2.imread("image.jpg")

# Check whether image is loaded
if img is None:
    print("Error: Image not found!")
    exit()

# Rotate image 180 degrees clockwise
rotated = cv2.rotate(img, cv2.ROTATE_180)

# Convert BGR to RGB
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
rotated_rgb = cv2.cvtColor(rotated, cv2.COLOR_BGR2RGB)

# Display original image
plt.subplot(1, 2, 1)
plt.imshow(img_rgb)
plt.title("Original Image")
plt.axis("off")

# Display rotated image
plt.subplot(1, 2, 2)
plt.imshow(rotated_rgb)
plt.title("180 Degree Rotation")
plt.axis("off")

plt.tight_layout()
plt.show()
