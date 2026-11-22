
import cv2

# Read input video
cap = cv2.VideoCapture("video.mp4")

if not cap.isOpened():
    print("Error: Cannot open video!")
    exit()

# Get video properties
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

if fps <= 0:
    fps = 25

# Create background subtractor
background = cv2.createBackgroundSubtractorMOG2(
    history=500,
    varThreshold=50,
    detectShadows=False
)

# Create output video
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter(
    "vehicle_output.mp4",
    fourcc,
    fps,
    (width, height)
)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Detect moving objects
    mask = background.apply(frame)

    # Remove noise
    kernel = cv2.getStructuringElement(
        cv2.MORPH_RECT, (5, 5)
    )
    mask = cv2.morphologyEx(
        mask, cv2.MORPH_OPEN, kernel
    )

    # Find object contours
    contours, _ = cv2.findContours(
        mask,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    # Draw rectangles around large moving objects
    for contour in contours:
        area = cv2.contourArea(contour)

        if area > 1000:
            x, y, w, h = cv2.boundingRect(contour)

            cv2.rectangle(
                frame,
                (x, y),
                (x + w, y + h),
                (0, 255, 0),
                2
            )

            cv2.putText(
                frame,
                "Moving Object",
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 0),
                2
            )

    # Display and save video
    cv2.imshow("Vehicle Detection", frame)
    out.write(frame)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
out.release()
cv2.destroyAllWindows()

print("Vehicle detection video created successfully!")
print("Output saved as vehicle_output.mp4")
