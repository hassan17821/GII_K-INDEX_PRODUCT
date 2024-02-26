# For multiple Color transparent
import cv2
import numpy as np
from google.colab.patches import cv2_imshow
from google.colab import drive

# Mount Google Drive (if needed)
# drive.mount('/content/drive')

# Image file paths
image_path = '/content/drive/MyDrive/329.jpg'
output_path = '329.webp'

# Define target colors as an array of objects with tolerance
target_colors = [
    {'color': (212, 230, 230), 'tolerance': 0.15},
    {'color': (255, 255, 255), 'tolerance': 0.05},
    # ... You can add more colors here
]

# Load the image
image = cv2.imread(image_path)

# Check if the image is loaded successfully
if image is not None:

  # Convert the image to BGR (in case it's loaded in a different format)
  image = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)

  # Create masks for each target color
  masks = []
  for color_obj in target_colors:
    target_color = color_obj['color']
    tolerance = color_obj['tolerance']
    target_color_lower = np.array([target_color[0] * (1 - tolerance), target_color[1] * (1 - tolerance), target_color[2] * (1 - tolerance)])
    target_color_upper = np.array([target_color[0] * (1 + tolerance), target_color[1] * (1 + tolerance), target_color[2] * (1 + tolerance)])
    mask = cv2.inRange(image, target_color_lower, target_color_upper)
    masks.append(mask)

  # Combine masks (union)
  combined_mask = masks[0]  # Start with the first mask
  for mask in masks[1:]:    # Combine remaining masks with bitwise OR
    combined_mask = cv2.bitwise_or(combined_mask, mask)

  print('Original ')
  cv2_imshow(image)
  print('Combined Mask ')
  cv2_imshow(combined_mask)

  # Invert the mask
  combined_mask = cv2.bitwise_not(combined_mask)

  # Make the masked region transparent
  transparent_image = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)
  transparent_image[:, :, 3] = combined_mask

  # Save the transparent image
  cv2.imwrite(output_path, transparent_image)
  print('Final ')
  # Display the transparent image (if in a compatible environment)
  cv2_imshow(transparent_image)
