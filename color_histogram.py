import cv2
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Load the image (you can replace 'image_path' with your actual image file)
image_path = "D:\TABLET\Tablet-Insight-Engine\ch.jpg"
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Step 2: Calculate the histogram
histogram = cv2.calcHist([image], [0], None, [256], [0, 256])

# Step 3: Plot the histogram
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")
plt.plot(histogram)
plt.xlim([0, 256])  # Setting the limits for the x-axis
plt.show()

# Optional: Display the image as well
cv2.imshow('Grayscale Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()


'''Interpretation:
X-Axis (Pixel Intensity):

The X-axis represents the pixel intensity values ranging from 0 (black) to 255 (white).
In the histogram, most of the intensity values are concentrated in the range between approximately 130 to 220. This indicates that the image contains mostly mid to high gray levels.
Y-Axis (Frequency):

The Y-axis shows the frequency of each pixel intensity level in the image. Peaks in the histogram indicate that a large number of pixels share the same intensity value.
Histogram Peaks:

There are prominent peaks around the 150 to 220 range. This suggests that the image contains a significant amount of pixels with these mid-to-high gray intensities.
The highest peak is around the 180 to 200 range, which likely corresponds to the brightest areas in the image.
Dark and Light Regions:

There is a relatively low frequency of very dark pixels (left side of the histogram, near 0), indicating that the image has few or no completely black regions.
There is also a low frequency of very light pixels (right side of the histogram, near 255), suggesting that there are few or no completely white regions in the image.'''
