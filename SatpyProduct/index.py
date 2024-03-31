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
    output_path = f'{output_path_arg}/**placeholder_name** [{time_arg}].webp'
    plot_products(input_path_arg, output_path, date_arg, time_arg)

else:
    print("Some required arguments are missing.")
