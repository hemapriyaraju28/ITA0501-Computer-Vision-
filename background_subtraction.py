
import cv2
import numpy as np

def background_subtraction(image_path):
    # Read the input image
    img = cv2.imread(image_path)

    if img is None:
        print("Error: Image not found!")
        return

    # Convert image from BGR to HSV color space
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Define color levels for background
    lower = np.array([0, 0, 180])
    upper = np.array([180, 50, 255])

    # Create mask for background color
    mask = cv2.inRange(hsv, lower, upper)

    # Subtract the background
    result = cv2.bitwise_and(img, img, mask=cv2.bitwise_not(mask))

    # Display images
    cv2.imshow("Original Image", img)
    cv2.imshow("Background Mask", mask)
    cv2.imshow("Background Removed", result)

    # Save output
    cv2.imwrite("background_removed.jpg", result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print("Background subtraction completed successfully!")

# Get image name from user
image_path = input("Enter image file name: ")

background_subtraction(image_path)
