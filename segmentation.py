
import cv2

# Read the input image
img = cv2.imread("image.jpg")

if img is None:
    print("Error: Image not found!")
    exit()

# Convert image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Set threshold value
threshold_value = 127

# Apply threshold segmentation
ret, segmented = cv2.threshold(
    gray,
    threshold_value,
    255,
    cv2.THRESH_BINARY
)

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Grayscale Image", gray)
cv2.imshow("Segmented Image", segmented)

# Save output
cv2.imwrite("segmented_output.jpg", segmented)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("Image segmentation completed successfully!")
