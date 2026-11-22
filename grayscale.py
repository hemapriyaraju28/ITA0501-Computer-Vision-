
import cv2

# Read the image
img = cv2.imread("image.jpg")

# Convert image into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Display original image
cv2.imshow("Original Image", img)

# Display grayscale image
cv2.imshow("Gray-scale Image", gray)

# Wait for a key press
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()
