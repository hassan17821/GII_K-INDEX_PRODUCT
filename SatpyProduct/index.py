import os
import sys

# Add the parent directory to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
# Import functions from modules
from SatpyProduct.all_hrit_products import plot_products
from satpy.utils import debug_off,debug_on
debug_off()
import warnings
warnings.filterwarnings('ignore')

# debug_on()
if len(sys.argv) == 5:
    # Extract command-line arguments
    date_arg, time_arg, input_path_arg, output_path_arg = sys.argv[1:]
    print("DATE      :: ", date_arg)
    print("TIME      :: ", time_arg)
    print("READ_DIR  :: ", input_path_arg)
    print("WRITE_DIR :: ", output_path_arg)

    files = os.listdir(input_path_arg)
    fnames = [os.path.join(input_path_arg, f) for f in files]
    fnames = [f for f in fnames if not f.endswith('.tmp')]
    # print("FileNames :: ", fnames)
    # exclude all .temp files in the directory

    print("FileNames Length :: ", len(fnames))
    # if len(fnames) < 140:
    #     raise ValueError("Insufficient number of files in the directory. Expected at least 140 files.")
    # else:
    output_path = f'{output_path_arg}/**placeholder_name**__{time_arg}.webp'
    plot_products(input_path_arg, output_path, date_arg, time_arg, fnames)

else:
    print("Some required arguments are missing.")
