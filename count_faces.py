
import cv2

def count_faces(image_path):
    # Read the input image
    img = cv2.imread(image_path)

    if img is None:
        print("Error: Image not found!")
        return

    # Load Haar Cascade face detector
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades +
        "haarcascade_frontalface_default.xml"
    )

    # Convert image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    # Count faces
    count = len(faces)

    # Draw rectangles around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h),
                      (0, 255, 0), 2)

    # Display face count
    print("Number of faces detected:", count)

    cv2.imshow("Face Detection", img)
    cv2.imwrite("face_count_output.jpg", img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Get image name from user
image_path = input("Enter image file name: ")

count_faces(image_path)
