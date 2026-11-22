
import cv2

def add_text(image_path, text):
    # Read the input image
    img = cv2.imread(image_path)

    if img is None:
        print("Error: Image not found!")
        return

    # Add text to the image
    cv2.putText(
        img,
        text,
        (50, 100),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 0, 255),
        2
    )

    # Display and save the image
    cv2.imshow("Image with Text", img)
    cv2.imwrite("text_output.jpg", img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print("Text added successfully!")

# Get input from user
image_path = input("Enter image file name: ")
text = input("Enter the text: ")

add_text(image_path, text)
