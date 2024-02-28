import os
import sys
import pdbufr

# Import functions from modules
from wind import plot_upperLevelWind, plot_lowerLevelWind
from airTemperature import plot_airTemperature


def checkIfAllOutputPathsExist(curr_time,total_time_args ):

    totalOutputPaths = []
    timeForNext3 = find_next_three_elements(curr_time, total_time_args);
    
    for item in output_data:
        label = item['label']
        for time in timeForNext3:
            totalOutputPaths.append(f'{output_path_arg}/{label} [{time}].webp')

    allPathExist = all(map(os.path.exists, totalOutputPaths))
    return allPathExist

def generate_time_args():
    time_args = []
    for hour in range(24):
        for minute in range(0, 60, 15):
            time_args.append("{:02d}-{:02d}".format(hour, minute))
    return time_args

def find_next_three_elements(time_arg, time_args):
    index = time_args.index(time_arg)
    result = []    
    # Add the current time argument and the next three elements
    for i in range(index, index + 4):
        result.append(time_args[i % len(time_args)])
    
    return result

if len(sys.argv) == 5:
    # Extract command-line arguments
    date_arg, curr_time, input_path_arg, output_path_arg = sys.argv[1:]
    total_time_args = generate_time_args()
    timeForNext3 = find_next_three_elements(curr_time, total_time_args);
    output_data = [
        {   'id':1,
            'label': 'LRIT_AMV_upperLevelWind',
            'function': plot_upperLevelWind
        },
        {   'id':2,
            'label': 'LRIT_AMV_lowerLevelWind',
            'function': plot_lowerLevelWind
        },
        {   'id':3,
            'label': 'LRIT_AMV_airTemperature',
            'function': plot_airTemperature
        }
    ]

    print(input_path_arg)
    # Check if output paths exist
    allPathExist = checkIfAllOutputPathsExist(curr_time, total_time_args)
    if allPathExist:
        print("All output paths already exist")
    else:
        df = pdbufr.read_bufr(input_path_arg, columns="data",flat=True)
        for item in output_data:
            function = item['function']
            id = item['id']
            label = item['label']
            outputPaths = []
            
            for time in timeForNext3:
                outputPath = f'{output_path_arg}/{label} [{time}].webp'
                if not os.path.exists(outputPath):
                    print(f"Processing {function.__name__} {outputPath}")
                    function(outputPath, df)
else:
    print("Some required arguments are missing.")
