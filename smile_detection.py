
import cv2

# Read image
img = cv2.imread("image.jpg")

if img is None:
    print("Error: image.jpg not found!")
    exit()

# Load face detector
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    "haarcascade_frontalface_default.xml"
)

# Load smile detector
smile_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    "haarcascade_smile.xml"
)

if face_cascade.empty() or smile_cascade.empty():
    print("Error: Haar Cascade file not loaded!")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(
    gray, 1.1, 5
)

print("Faces detected:", len(faces))

# Detect smiles
count = 0

for (x, y, w, h) in faces:

    face_gray = gray[y:y+h, x:x+w]
    face_color = img[y:y+h, x:x+w]

    # Search in the lower half of the face
    lower_gray = face_gray[h//2:h, :]

    smiles = smile_cascade.detectMultiScale(
        lower_gray,
        scaleFactor=1.3,
        minNeighbors=15,
        minSize=(25, 15)
    )

    for (sx, sy, sw, sh) in smiles:
        cv2.rectangle(
            face_color,
            (sx, sy+h//2),
            (sx+sw, sy+sh+h//2),
            (0, 255, 0), 2
        )

        cv2.putText(
            img, "Smile",
            (x+sx, y+sy+h//2-5),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7, (0, 255, 0), 2
        )

        count += 1

print("Smiles detected:", count)

# Display and save output
cv2.imshow("Smile Detection", img)
cv2.imwrite("smile_output.jpg", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
