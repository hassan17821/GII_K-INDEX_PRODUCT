import cv2
import numpy as np
from google.colab.patches import cv2_imshow
from google.colab import drive

# Mount Google Drive (if needed)
# drive.mount('/content/drive')

# Image file paths
image_path = '/content/drive/MyDrive/329.jpg'
output_path = '329.webp'
target_color = (212, 230, 230)
target_color1 = (255, 255, 255)

# Define the target ocean color (BGR) with 40% tolerance range
tolerance = 0.15  # Adjust this value for desired tolerance (0 to 1)
target_color_lower = np.array([target_color[0] * (1 - tolerance), target_color[1] * (1 - tolerance), target_color[2] * (1 - tolerance)])
target_color_upper = np.array([target_color[0] * (1 + tolerance), target_color[1] * (1 + tolerance), target_color[2] * (1 + tolerance)])

tolerance1 = 0.05
target_color1_lower = np.array([target_color1[0] * (1 - tolerance1), target_color1[1] * (1 - tolerance1), target_color1[2] * (1 - tolerance1)])
target_color1_upper = np.array([target_color1[0] * (1 + tolerance1), target_color1[1] * (1 + tolerance1), target_color1[2] * (1 + tolerance1)])

# Load the image
image = cv2.imread(image_path)

# Check if the image is loaded successfully
if image is not None:

  # Convert the image to BGR (in case it's loaded in a different format)
  image = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)

  # Create a mask to select the ocean color with tolerance
  mask1 = cv2.inRange(image, target_color_lower, target_color_upper)
  mask2 = cv2.inRange(image, target_color1_lower, target_color1_upper)

  print('Original ')
  cv2_imshow(image)
  print('Mask1 ')
  cv2_imshow(mask1)
  print('Mask2 ')
  cv2_imshow(mask2)

  # Combine masks (union)
  combined_mask = cv2.bitwise_or(mask1, mask2)

  print('combined_mask ')
  cv2_imshow(combined_mask)
  # Invert the mask
  combined_mask = cv2.bitwise_not(combined_mask)

  # Invert the mask for transparent replacement
  mask = cv2.bitwise_not(mask)

  # Make the masked region transparent
  transparent_image = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)
  transparent_image[:, :, 3] = combined_mask

  # Save the transparent image
  cv2.imwrite(output_path, transparent_image)
  print('Final ')
  # Display the transparent image (if in a compatible environment)
  cv2_imshow(transparent_image)