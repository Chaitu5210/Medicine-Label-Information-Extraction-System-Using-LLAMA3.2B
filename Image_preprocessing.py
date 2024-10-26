import cv2
import numpy as np
from matplotlib import pyplot as plt

def preprocessing(image_path):
    # Load the image
    original_image = cv2.imread(image_path)

    # Check if the image was loaded
    if original_image is None:
        print("Error: Image not found.")
        return
    else:
        # Convert to grayscale
        gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

        # Sharpening
        sharpen_kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
        sharpened_image = cv2.filter2D(gray_image, -1, sharpen_kernel)

        # Save the processed image
        processed_image_path = 'Saved_Images/processed_image_with_text.jpg'
        cv2.imwrite(processed_image_path, sharpened_image)
        print(f"Processed image saved at {processed_image_path}")

        # Display the images at each step
        fig, axs = plt.subplots(2, 3, figsize=(12, 8))
        axs[0, 0].imshow(cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB))
        axs[0, 0].set_title("Original Image")
        axs[0, 1].imshow(gray_image, cmap='gray')
        axs[0, 1].set_title("Grayscale Image")
        axs[0, 2].imshow(sharpened_image, cmap='gray')
        axs[0, 2].set_title("Sharpened Image")

        for ax in axs.flat:
            ax.axis('off')

        plt.tight_layout()
        plt.show()
    
    return "Saved_Images/processed_image_with_text.jpg"
