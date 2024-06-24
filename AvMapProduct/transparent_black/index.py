import cv2
import numpy as np
import os
from os.path import join, exists
from datetime import datetime
import fnmatch
import time

current_date = datetime.now().strftime('%Y-%m-%d')

# Input and output directory paths
input_base_path = os.path.join(r'D:\server1\Archive', current_date)
output_base_path = os.path.join(r'D:\server1\Archive', current_date, 'transparent')

# Define target colors as an array of objects with tolerance
target_colors = [
    {'color': (0, 0, 0), 'tolerance': 0.15},
]

# File patterns to match
file_patterns = [
    'Picture_2_Rain_fall_estimate_using_IR_imagery_WG*.webp',
    'Picture_5_IR_108+IR_120+IR_120 reprojected palette_WG*.webp',
    'HRV_IO_region_WG*.webp'
]

def process_image(input_path, output_path):
    global processed_files  # Use the global set variable
    # Remove .jpg from output_path and add .webp
    output_path = output_path.replace(".jpg", ".webp")

    # Check if the .webp file already exists
    if exists(output_path):
        print(f"Skipping already existing file: {output_path}")
        return

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
        cv2.imwrite(output_path, transparent_image)
        print(f"Processed and saved image: {output_path}")
    else:
        print(f"Error: Unable to load image from {input_path}")

def process_directory(input_dir, output_dir):
    for root, _, files in os.walk(input_dir):
        for file in files:
            # Check if the file matches any pattern in the file_patterns list
            if any(fnmatch.fnmatch(file, pattern) for pattern in file_patterns):
                input_path = join(root, file)
                output_path = join(output_dir, os.path.relpath(root, input_dir), file)
                process_image(input_path, output_path)

# Process the input directory
while True:
    process_directory(input_base_path, output_base_path)    
    # print('________ Sleeping for 120sec _____________')
    time.sleep(120)  # Wait for 120 seconds before running the process again