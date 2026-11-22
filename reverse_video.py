
import cv2

def reverse_video(input_file, output_file):

    # Open the input video
    cap = cv2.VideoCapture(input_file)

    if not cap.isOpened():
        print("Error: Cannot open video!")
        return

    # Get video properties
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Read all video frames
    frames = []

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        frames.append(frame)

    cap.release()

    # Create output video
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(
        output_file, fourcc, fps, (width, height)
    )

    # Write frames in reverse order
    for frame in reversed(frames):
        out.write(frame)

    out.release()

    print("Reverse video created successfully!")

# Call the function
reverse_video("video.mp4", "reverse_video.mp4")
