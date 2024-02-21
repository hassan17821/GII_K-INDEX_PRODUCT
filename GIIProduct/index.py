import os
import sys
import pdbufr

# Import functions from modules
from kIndex import plot_kIndex
from koIndex import plot_koIndex
from parcelLiftedIndexTo500Hpa import plot_parcelLiftedIndexTo500Hpa
from precipitableWater import plot_totalPrecipitableWater, plot_precipitableWater10To500mbar, plot_precipitableWater500To850mbar, plot_precipitableWater850To1000mbar
from maximumBuoyancy import plot_maximumBuoyancy

if len(sys.argv) == 5:
    # Extract command-line arguments
    date_arg, time_arg, input_path_arg, output_path_arg = sys.argv[1:]
    output_data = [
        {
            'output_path': f'{output_path_arg}/LRIT_GII_kIndex [{time_arg}].webp',
            'function': plot_kIndex
        },
        {
            'output_path': f'{output_path_arg}/LRIT_GII_koIndex [{time_arg}].webp',
            'function': plot_koIndex
        },
        {
            'output_path': f'{output_path_arg}/LRIT_GII_parcelLiftedIndexTo500Hpa [{time_arg}].webp',
            'function': plot_parcelLiftedIndexTo500Hpa
        },
        {
            'output_path': f'{output_path_arg}/LRIT_GII_totalPrecipitableWater [{time_arg}].webp',
            'function': plot_totalPrecipitableWater
        },
        {
            'output_path': f'{output_path_arg}/LRIT_GII_precipitableWater10To500mbar [{time_arg}].webp',
            'function': plot_precipitableWater10To500mbar
        },
        {
            'output_path': f'{output_path_arg}/LRIT_GII_precipitableWater500To850mbar [{time_arg}].webp',
            'function': plot_precipitableWater500To850mbar
        },
        {
            'output_path': f'{output_path_arg}/LRIT_GII_precipitableWater850To1000mbar [{time_arg}].webp',
            'function': plot_precipitableWater850To1000mbar
        },
        {
            'output_path': f'{output_path_arg}/LRIT_GII_maximumBuoyancy [{time_arg}].webp',
            'function': plot_maximumBuoyancy
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
