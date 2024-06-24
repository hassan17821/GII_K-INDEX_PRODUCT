import cv2
import numpy as np
from google.colab.patches import cv2_imshow
from google.colab import drive

# Mount Google Drive (if needed)
# drive.mount('/content/drive')

# Image file paths
image_path = '/content/drive/MyDrive/329.jpg'
output_path = '329.webp'

# Load the image
image = cv2.imread(image_path)

# Check if the image was loaded successfully
if image is not None:

  # Convert the image to 8-bit grayscale
  image_8bit = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

  # Threshold the image to create a binary mask
  _, mask = cv2.threshold(image_8bit, 240, 255, cv2.THRESH_BINARY)

  # Invert the mask
  mask = cv2.bitwise_not(mask)

  # Make the masked region transparent
  transparent_image = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)  # Add alpha channel
  transparent_image[:, :, 3] = mask  # Set alpha channel values based on mask

  # Save the transparent image
  cv2.imwrite(output_path, transparent_image)

  # Display the transparent image (if in a compatible environment)
  cv2_imshow(transparent_image)

