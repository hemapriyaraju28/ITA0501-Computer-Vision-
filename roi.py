
import cv2
import matplotlib.pyplot as plt

# Read the source image
img = cv2.imread("image.jpg")

# Check whether image is loaded
if img is None:
    print("Error: Image not found!")
    exit()

# Get image dimensions
h, w = img.shape[:2]

# Select Region of Interest (ROI)
x1 = w // 4
y1 = h // 4
x2 = 3 * w // 4
y2 = 3 * h // 4

# Crop the selected region
roi = img[y1:y2, x1:x2]

# Copy the cropped region
copied_roi = roi.copy()

# Create a copy of original image
pasted_img = img.copy()

# Paste ROI at a new position
pasted_img[0:copied_roi.shape[0],
           0:copied_roi.shape[1]] = copied_roi

# Convert BGR to RGB
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
roi_rgb = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)
pasted_rgb = cv2.cvtColor(pasted_img, cv2.COLOR_BGR2RGB)

# Display original image
plt.subplot(1, 3, 1)
plt.imshow(img_rgb)
plt.title("Original Image")
plt.axis("off")

# Display cropped image
plt.subplot(1, 3, 2)
plt.imshow(roi_rgb)
plt.title("Cropped ROI")
plt.axis("off")

# Display pasted image
plt.subplot(1, 3, 3)
plt.imshow(pasted_rgb)
plt.title("Pasted Image")
plt.axis("off")

plt.tight_layout()
plt.show()

# Save the output images
cv2.imwrite("cropped_roi.jpg", roi)
cv2.imwrite("pasted_image.jpg", pasted_img)

print("Cropping, copying and pasting completed successfully!")
