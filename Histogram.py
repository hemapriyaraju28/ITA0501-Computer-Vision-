
import cv2
import matplotlib.pyplot as plt

# Read the input image
img = cv2.imread("image.jpg")

# Check whether image is loaded
if img is None:
    print("Error: Image not found!")
    exit()

# Convert BGR to RGB
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Function to analyze histogram
def analyze_histogram(image):

    colors = ('b', 'g', 'r')
    labels = ('Blue', 'Green', 'Red')

    plt.figure(figsize=(8, 5))

    for i, color in enumerate(colors):
        histogram = cv2.calcHist([image], [i], None,
                                 [256], [0, 256])

        plt.plot(histogram, color=color,
                 label=labels[i])

    plt.title("Color Histogram Analysis")
    plt.xlabel("Pixel Intensity Levels")
    plt.ylabel("Number of Pixels")
    plt.xlim([0, 256])
    plt.legend()
    plt.grid()
    plt.show()


# Display original image
plt.imshow(img_rgb)
plt.title("Original Image")
plt.axis("off")
plt.show()

# Call histogram function
analyze_histogram(img)
