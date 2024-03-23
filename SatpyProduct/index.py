# https://nbviewer.org/github/pytroll/pytroll-examples/blob/main/satpy/hrit_msg_tutorial.ipynb
from satpy.scene import Scene
from satpy.resample import get_area_def
from satpy import find_files_and_readers
from datetime import datetime
import glob
import warnings

# Date format in YYYYMMDDhhmm
data_dir = "//EUMETCAST-INGES/Data/XRIT/Compressed"

# List all files in the directory
files = os.listdir(data_dir)
fnames = [os.path.join(data_dir, f) for f in files]

# fnames = glob.glob('/path/to/data/H*202009060000*__')
scn = Scene(reader='seviri_l1b_hrit', filenames=fnames)
scn.available_composite_ids()

composite = 'airmass'
scn.load([composite])
scn.show(composite)