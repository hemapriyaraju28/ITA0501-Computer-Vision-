
import cv2

# Read the image
img = cv2.imread("image.jpg")

# Apply Gaussian Blur
blur = cv2.GaussianBlur(img, (15, 15), 0)

# Display original image
cv2.imshow("Original Image", img)

# Display blurred image
cv2.imshow("Gaussian Blur Image", blur)

# Wait for a key press
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()
