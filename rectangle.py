
import cv2
import numpy as np

def create_rectangle(width, height):

    # Create a white image
    img = np.ones((height, width, 3), dtype=np.uint8) * 255

    # Draw a rectangle
    cv2.rectangle(
        img,
        (width // 4, height // 4),
        (3 * width // 4, 3 * height // 4),
        (0, 0, 255),
        3
    )

    # Display the image
    cv2.imshow("Rectangle Image", img)

    # Save the image
    cv2.imwrite("rectangle_output.jpg", img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print("Rectangle image created successfully!")

# Get image size from user
width = int(input("Enter image width: "))
height = int(input("Enter image height: "))

# Call the function
create_rectangle(width, height)
