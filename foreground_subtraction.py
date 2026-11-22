
import cv2
import numpy as np

def foreground_subtraction(image_path):
    # Read the input image
    img = cv2.imread(image_path)

    if img is None:
        print("Error: Image not found!")
        return

    # Convert image from BGR to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Define foreground color levels
    lower = np.array([0, 50, 50])
    upper = np.array([180, 255, 255])

    # Create mask for foreground
    mask = cv2.inRange(hsv, lower, upper)

    # Subtract the foreground
    result = cv2.bitwise_and(
        img, img, mask=cv2.bitwise_not(mask)
    )

    # Display images
    cv2.imshow("Original Image", img)
    cv2.imshow("Foreground Mask", mask)
    cv2.imshow("Foreground Subtracted", result)

    # Save output
    cv2.imwrite("foreground_subtracted.jpg", result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print("Foreground subtraction completed successfully!")

# Get image name from user
image_path = input("Enter image file name: ")

foreground_subtraction(image_path)
