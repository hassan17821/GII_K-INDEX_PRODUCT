import os
import sys

# Import functions from modules
from all_products import plot_products
from satpy.utils import debug_off,debug_on
debug_off()
import warnings
warnings.filterwarnings('ignore')

# debug_on()
if len(sys.argv) == 5:
    # Extract command-line arguments
    date_arg, time_arg, input_path_arg, output_path_arg = sys.argv[1:]
    print("date :: ", date_arg)
    print("time :: ", time_arg)
    print("input_path :: ", input_path_arg)
    print("output_path :: ", output_path_arg)

    files = os.listdir(input_path_arg)
    fnames = [os.path.join(input_path_arg, f) for f in files]
    print("FileNames Length :: ", len(fnames))
    if len(fnames) < 140:
        raise ValueError("Insufficient number of files in the directory. Expected at least 140 files.")
    else:
        output_path = f'{output_path_arg}/**placeholder_name** [{time_arg}].webp'
        plot_products(input_path_arg, output_path, date_arg, time_arg, fnames)

else:
    print("Some required arguments are missing.")
