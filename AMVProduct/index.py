import os
import sys
import pdbufr

# Import functions from modules
from wind import plot_upperLevelWind, plot_lowerLevelWind

if len(sys.argv) == 5:
    # Extract command-line arguments
    date_arg, time_arg, input_path_arg, output_path_arg = sys.argv[1:]
    output_data = [
        {
            'output_path': f'{output_path_arg}/LRIT_GII_upperLevelWind [{time_arg}].webp',
            'function': plot_upperLevelWind
        },
        {
            'output_path': f'{output_path_arg}/LRIT_GII_lowerLevelWind [{time_arg}].webp',
            'function': plot_lowerLevelWind
        }
    ]

    print(input_path_arg)
    # Check if output paths exist
    if all(os.path.exists(item['output_path']) for item in output_data):
        print("All output paths already exist")
    else:
        df = pdbufr.read_bufr(input_path_arg, columns="data",flat=True)
        for item in output_data:
            output_path = item['output_path']
            function = item['function']
            if not os.path.exists(output_path):
                print(f"Processing {function.__name__} {output_path}")
                function(output_path, df)

else:
    print("Some required arguments are missing.")
