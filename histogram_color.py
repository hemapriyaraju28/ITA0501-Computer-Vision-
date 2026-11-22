
import cv2
import matplotlib.pyplot as plt

# Function to analyze image histogram
def analyze_histogram(image_path):
    # Read the image
    img = cv2.imread(image_path)

    if img is None:
        print("Error: Image not found!")
        return

    # Convert BGR to RGB
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Define colors
    colors = ('r', 'g', 'b')

    # Calculate and display histogram
    for i, color in enumerate(colors):
        hist = cv2.calcHist([img], [i], None, [256], [0, 256])
        plt.plot(hist, color=color)
    
    plt.title("Color Histogram")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Number of Pixels")
    plt.xlim([0, 256])
    plt.show()

# Call the function
analyze_histogram("image.jpg")
