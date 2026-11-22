
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

# Apply dilation
dilated = cv2.dilate(img, kernel, iterations=1)

# Convert BGR to RGB
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
dilated_rgb = cv2.cvtColor(dilated, cv2.COLOR_BGR2RGB)

# Display original image
plt.subplot(1, 2, 1)
plt.imshow(img_rgb)
plt.title("Original Image")
plt.axis("off")

# Display dilated image
plt.subplot(1, 2, 2)
plt.imshow(dilated_rgb)
plt.title("Dilated Image")
plt.axis("off")

plt.show()
