
import cv2

# Read the image
img = cv2.imread("image.jpg")

# Check image
if img is None:
    print("Error: Image not found!")
    exit()

# Split image into color channels
b, g, r = cv2.split(img)

# Calculate histograms
hist_b = cv2.calcHist([b], [0], None, [256], [0, 256])
hist_g = cv2.calcHist([g], [0], None, [256], [0, 256])
hist_r = cv2.calcHist([r], [0], None, [256], [0, 256])

# Create histogram image
hist_img = cv2.merge([b, g, r])

# Draw histograms
canvas = cv2.imread("image.jpg")
canvas = cv2.resize(canvas, (512, 400))
canvas[:] = 255

for i in range(256):
    x = int(i * 2)

    yb = int(hist_b[i][0] / hist_b.max() * 300)
    yg = int(hist_g[i][0] / hist_g.max() * 300)
    yr = int(hist_r[i][0] / hist_r.max() * 300)

    cv2.line(canvas, (x, 350), (x, 350-yb), (255, 0, 0), 1)
    cv2.line(canvas, (x, 350), (x, 350-yg), (0, 255, 0), 1)
    cv2.line(canvas, (x, 350), (x, 350-yr), (0, 0, 255), 1)

# Display histogram
cv2.imshow("Original Image", img)
cv2.imshow("Color Histogram", canvas)

cv2.waitKey(0)
cv2.destroyAllWindows()
