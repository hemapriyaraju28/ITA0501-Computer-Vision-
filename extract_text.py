
import cv2
import pytesseract

# Set Tesseract path (Windows)
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

def extract_text(video_path):
    # Open the video
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Cannot open video!")
        return

    frame_count = 0
    extracted_text = set()

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        # Process every 30th frame
        if frame_count % 30 == 0:

            # Convert frame to grayscale
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Extract text using OCR
            text = pytesseract.image_to_string(gray)

            if text.strip():
                extracted_text.add(text.strip())

        frame_count += 1

    cap.release()

    # Display extracted text
    print("\nExtracted Text from Video:")

    if extracted_text:
        for text in extracted_text:
            print(text)
    else:
        print("No text found in the video.")

    # Save extracted text
    with open("extracted_text.txt", "w", encoding="utf-8") as file:
        for text in extracted_text:
            file.write(text + "\n")

    print("\nText extraction completed successfully!")

# Get video file name
video_path = input("Enter video file name: ")

extract_text(video_path)
