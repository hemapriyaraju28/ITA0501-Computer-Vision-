
import cv2
import numpy as np

def create_circle(width, height):
    # Create a white image
    img = np.ones((height, width, 3), dtype=np.uint8) * 255

    # Define circle center and radius
    center = (width // 2, height // 2)
    radius = min(width, height) // 4

    # Draw a red circle
    cv2.circle(img, center, radius, (0, 0, 255), 3)

    # Display and save the image
    cv2.imshow("Circle Image", img)
    cv2.imwrite("circle_output.jpg", img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print("Circle image created successfully!")

# Get image size from user
width = int(input("Enter image width: "))
height = int(input("Enter image height: "))

create_circle(width, height)
