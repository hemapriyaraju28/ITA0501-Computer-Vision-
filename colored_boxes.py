
import cv2
import numpy as np

def create_image(width, height):

    # Create a white image
    img = np.ones((height, width, 3), dtype=np.uint8) * 255

    # Calculate box size (1/10th of image)
    box_w = width // 10
    box_h = height // 10

    # Draw Black box at top-left corner
    img[0:box_h, 0:box_w] = (0, 0, 0)

    # Draw Blue box at top-right corner
    img[0:box_h, width-box_w:width] = (255, 0, 0)

    # Draw Green box at bottom-left corner
    img[height-box_h:height, 0:box_w] = (0, 255, 0)

    # Draw Red box at bottom-right corner
    img[height-box_h:height, width-box_w:width] = (0, 0, 255)

    # Display image
    cv2.imshow("Four Colored Boxes", img)

    # Save image
    cv2.imwrite("colored_boxes.jpg", img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print("Image created successfully!")

# Get image size from user
width = int(input("Enter image width: "))
height = int(input("Enter image height: "))

# Call function
create_image(width, height)
