import os
import sys

# Import functions from modules
from fog import plot_fog
from all_bands import plot_all_bands
from all_products import plot_products
from satpy.utils import debug_off,debug_on
debug_off()
# debug_on()
if len(sys.argv) == 5:
    # Extract command-line arguments
    date_arg, time_arg, input_path_arg, output_path_arg = sys.argv[1:]
    output_data = [
        # {
        #     'output_path': f'{output_path_arg}/fog [{time_arg}].webp',
        #     'function': plot_fog
        # },
        {
            'output_path': f'{output_path_arg}/**band_name** [{time_arg}].webp',
            'function': plot_all_bands
        },
        {
            'output_path': f'{output_path_arg}/**product_name** [{time_arg}].webp',
            'function': plot_products
        }
    ]

    print(input_path_arg)

    for item in output_data:
        output_path = item['output_path']
        function = item['function']
        if not os.path.exists(output_path):
            print(f"Processing {function.__name__} {output_path}")
            function(input_path_arg, output_path, date_arg, time_arg)

else:
    print("Some required arguments are missing.")
