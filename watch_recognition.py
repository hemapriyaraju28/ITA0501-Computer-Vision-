
import cv2
import numpy as np

# Read images
img = cv2.imread("image.jpg")
ref = cv2.imread("watch_reference.jpg")

if img is None or ref is None:
    print("Error: Check image.jpg and watch_reference.jpg")
    exit()

# Remove white background from reference image
gray_ref = cv2.cvtColor(ref, cv2.COLOR_BGR2GRAY)
mask = gray_ref < 240

points = cv2.findNonZero(mask.astype(np.uint8))

if points is None:
    print("Watch not found in reference image!")
    exit()

x, y, w, h = cv2.boundingRect(points)
template = ref[y:y+h, x:x+w]

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
temp = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

# Resize template if necessary
scale = min(1.0, gray.shape[1] / w, gray.shape[0] / h)
new_w = max(1, int(w * scale))
new_h = max(1, int(h * scale))
temp = cv2.resize(temp, (new_w, new_h))

# Match the watch
result = cv2.matchTemplate(
    gray, temp, cv2.TM_CCOEFF_NORMED
)

_, score, _, location = cv2.minMaxLoc(result)

if score >= 0.60:
    x, y = location
    cv2.rectangle(
        img, (x, y), (x+new_w, y+new_h),
        (0, 255, 0), 3
    )
    cv2.putText(
        img, "Watch Detected", (x, max(25, y-10)),
        cv2.FONT_HERSHEY_SIMPLEX, 0.8,
        (0, 255, 0), 2
    )
    print("Watch detected!")
else:
    print("Watch not detected!")

print("Matching score:", score)

cv2.imshow("Watch Recognition", img)
cv2.imwrite("watch_output.jpg", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
