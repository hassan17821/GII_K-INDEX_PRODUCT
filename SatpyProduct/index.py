import os
import sys

# Import functions from modules
from fog import plot_fog

if len(sys.argv) == 5:
    # Extract command-line arguments
    date_arg, time_arg, input_path_arg, output_path_arg = sys.argv[1:]
    output_data = [
        {
            'output_path': f'{output_path_arg}/fog [{time_arg}].webp',
            'function': plot_fog
        },
        # {
        #     'output_path': f'{output_path_arg}/night_fog [{time_arg}].webp',
        #     'function': plot_nightfog
        # }
    ]

    print(input_path_arg)
    # Check if output paths exist
    if all(os.path.exists(item['output_path']) for item in output_data):
        print("All output paths already exist")
    else:
        for item in output_data:
            output_path = item['output_path']
            function = item['function']
            if not os.path.exists(output_path):
                print(f"Processing {function.__name__} {output_path}")
                function(input_path_arg, output_path, time_arg)

else:
    print("Some required arguments are missing.")
