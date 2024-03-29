import os
import matplotlib.pyplot as plt
from satpy.scene import Scene
from satpy.resample import get_area_def
from pyresample.geometry import AreaDefinition
from pyresample import create_area_def
from satpy.writers import to_image
import pyspectral.near_infrared_reflectance
from glob import glob
from satpy.writers import to_image
from satpy.utils import debug_on
from satpy.enhancements import create_colormap
from satpy.enhancements import palettize
from datetime import datetime


def plot_band(data_dir,output_path, composite):

    latBound = [7.22, 37.454]
    lngBound = [43.753, 102.363]

    files = os.listdir(data_dir)
    fnames = [os.path.join(data_dir, f) for f in files]

    print("FileNames Length :: ",len(fnames))
    if(len(fnames) < 140):
        print("Not enough files to process")
        return
    
    scn = Scene(reader='seviri_l1b_hrit', filenames=fnames)
    scn.load([composite])

    my_area = create_area_def('my_area', {'proj': 'merc', 'lon_0': 45.5},
                width=1500, height=850,
                area_extent=[lngBound[0], latBound[0], lngBound[1], latBound[1]],
                reduce_data=False,
                units='degrees')

    scn_resampled = scn.resample(my_area)
    print('Saving '+ composite)
    scn_resampled.save_dataset(composite , output_path)


def plot_all_bands(data_dir, output_path, date_arg, time_arg):
    bands=[
    'HRV',
    'IR_016',
    'IR_039',
    'IR_087',
    'IR_097',
    'IR_108',
    'IR_120',
    'IR_134',
    'VIS006',
    'VIS008',
    'WV_062',
    'WV_073',
    ]
    for band in bands:
        _output_path = output_path.replace('**band_name**', band);
        plot_band(data_dir, _output_path, band)


export = plot_all_bands