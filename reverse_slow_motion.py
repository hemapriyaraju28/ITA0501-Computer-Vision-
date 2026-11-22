
import cv2

def reverse_slow_motion(video_path):
    # Open the video file
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Cannot open video!")
        return

    fps = cap.get(cv2.CAP_PROP_FPS)

    if fps <= 0:
        fps = 30

    # Read and store all video frames
    frames = []

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        frames.append(frame)

    cap.release()

    if len(frames) == 0:
        print("Error: No frames found!")
        return

    # Create video writer for slow-motion output
    height, width = frames[0].shape[:2]

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')

    out = cv2.VideoWriter(
        "reverse_slow_video.mp4",
        fourcc,
        fps / 2,
        (width, height)
    )

    # Play frames in reverse order
    for frame in reversed(frames):
        cv2.imshow("Reverse Slow Motion", frame)

        # Save reversed frames
        out.write(frame)

        # Wait longer to play in slow motion
        if cv2.waitKey(int(2000 / fps)) & 0xFF == ord('q'):
            break

    out.release()
    cv2.destroyAllWindows()

    print("Reverse slow-motion video created successfully!")

# Get video file name
video_path = input("Enter video file name: ")

reverse_slow_motion(video_path)
