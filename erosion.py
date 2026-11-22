
import cv2
import matplotlib.pyplot as plt

# Read the input image
img = cv2.imread("image.jpg")

# Check whether image is loaded
if img is None:
    print("Error: Image not found!")
    exit()

# Create a kernel
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

# Apply erosion
eroded = cv2.erode(img, kernel, iterations=1)

# Convert BGR to RGB
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
eroded_rgb = cv2.cvtColor(eroded, cv2.COLOR_BGR2RGB)

# Display original image
plt.subplot(1, 2, 1)
plt.imshow(img_rgb)
plt.title("Original Image")
plt.axis("off")

# Display eroded image
plt.subplot(1, 2, 2)
plt.imshow(eroded_rgb)
plt.title("Eroded Image")
plt.axis("off")

plt.show()
