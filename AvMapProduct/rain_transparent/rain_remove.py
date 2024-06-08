import cv2
import numpy as np

# Mount Google Drive (if needed)
# drive.mount('/content/drive')

# Image file paths
image_path = './rain.webp'
output_path = '329.webp'
target_color = (0, 0, 0)

# Define the target ocean color (BGR) with 40% tolerance range
tolerance = 0.15  # Adjust this value for desired tolerance (0 to 1)
target_color_lower = np.array([target_color[0] * (1 - tolerance), target_color[1] * (1 - tolerance), target_color[2] * (1 - tolerance)])
target_color_upper = np.array([target_color[0] * (1 + tolerance), target_color[1] * (1 + tolerance), target_color[2] * (1 + tolerance)])

# Load the image
image = cv2.imread(image_path)

# Check if the image is loaded successfully
if image is not None:

  # Convert the image to BGR (in case it's loaded in a different format)
  image = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)

  # Create a mask to select the ocean color with tolerance
  mask = cv2.inRange(image, target_color_lower, target_color_upper)

  # Invert the mask for transparent replacement
  mask = cv2.bitwise_not(mask)

  # Make the masked region transparent
  transparent_image = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)
  transparent_image[:, :, 3] = mask

  # Save the transparent image
  cv2.imwrite(output_path, transparent_image)

  # Display the transparent image (if in a compatible environment)
  cv.imshow(transparent_image)
