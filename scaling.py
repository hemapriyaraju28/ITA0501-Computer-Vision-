
import cv2
import matplotlib.pyplot as plt

# Read the input image
img = cv2.imread("image.jpg")

# Check whether image is loaded
if img is None:
    print("Error: Image not found!")
    exit()

# Get original image dimensions
h, w = img.shape[:2]

# Resize to bigger size (increase by 2 times)
bigger = cv2.resize(img, (w * 2, h * 2),
                    interpolation=cv2.INTER_CUBIC)

# Resize to smaller size (reduce by half)
smaller = cv2.resize(img, (w // 2, h // 2),
                     interpolation=cv2.INTER_AREA)

# Convert images from BGR to RGB
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
bigger_rgb = cv2.cvtColor(bigger, cv2.COLOR_BGR2RGB)
smaller_rgb = cv2.cvtColor(smaller, cv2.COLOR_BGR2RGB)

# Display original image
plt.figure(figsize=(10, 5))

plt.subplot(1, 3, 1)
plt.imshow(img_rgb)
plt.title("Original Image")
plt.axis("off")

# Display bigger image
plt.subplot(1, 3, 2)
plt.imshow(bigger_rgb)
plt.title("Bigger Image")
plt.axis("off")

# Display smaller image
plt.subplot(1, 3, 3)
plt.imshow(smaller_rgb)
plt.title("Smaller Image")
plt.axis("off")

plt.tight_layout()
plt.show()
