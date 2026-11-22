
import cv2
import matplotlib.pyplot as plt

# Read the original image
img = cv2.imread("image.jpg")

# Check whether image is loaded
if img is None:
    print("Error: Image not found!")
    exit()

# Create a copy of the original image
watermarked = img.copy()

# Define watermark text
text = "WATERMARK"

# Set watermark properties
font = cv2.FONT_HERSHEY_SIMPLEX
position = (30, img.shape[0] - 30)
font_scale = 1
color = (0, 0, 255)
thickness = 2

# Insert watermark into image
cv2.putText(watermarked, text, position, font,
            font_scale, color, thickness,
            cv2.LINE_AA)

# Save watermarked image
cv2.imwrite("watermarked_image.jpg", watermarked)

# Convert BGR to RGB
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
watermarked_rgb = cv2.cvtColor(watermarked, cv2.COLOR_BGR2RGB)

# Display original image
plt.subplot(1, 2, 1)
plt.imshow(img_rgb)
plt.title("Original Image")
plt.axis("off")

# Display watermarked image
plt.subplot(1, 2, 2)
plt.imshow(watermarked_rgb)
plt.title("Watermarked Image")
plt.axis("off")

plt.tight_layout()
plt.show()

print("Watermark inserted successfully!")
