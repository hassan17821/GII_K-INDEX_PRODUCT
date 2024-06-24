import cv2
import numpy as np
import os
from os.path import join, exists

# Input and output paths
input_base_path = r"D:/AVMAP__1"
output_base_path = r"D:/AVMAP__2/2402"

# Define target colors as an array of objects with tolerance
target_colors = [
    {'color': (212, 230, 230), 'tolerance': 0.10},
    {'color': (255, 255, 255), 'tolerance': 0.05},
]

def process_image(input_path, output_path):
    # Load the image
    image = cv2.imread(input_path)

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
        combined_mask = masks[0]
        for mask in masks[1:]:
            combined_mask = cv2.bitwise_or(combined_mask, mask)

        # Invert the mask
        combined_mask = cv2.bitwise_not(combined_mask)

        # Make the masked region transparent
        transparent_image = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)
        transparent_image[:, :, 3] = combined_mask

        # Create the output directory if it doesn't exist
        output_dir = os.path.dirname(output_path)
        os.makedirs(output_dir, exist_ok=True)

        # Save the transparent image
        # remove .jpg from output_path and add .webp
        output_path = output_path.replace(".jpg", ".webp")
        cv2.imwrite(output_path, transparent_image)
        print(f"Processed and saved image: {output_path}")
    else:
        print(f"Error: Unable to load image from {input_path}")

def process_directory(input_dir, output_dir):
    for root, _, files in os.walk(input_dir):
        for file in files:
            if file.endswith(".jpg"):
                input_path = join(root, file)
                output_path = join(output_dir, os.path.relpath(root, input_dir), file)
                # print(f"Processing image: {input_path} -> {output_path}")
                process_image(input_path, output_path)

# Process the input directory
process_directory(input_base_path, output_base_path)