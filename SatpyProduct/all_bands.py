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
from utils import plot_msg

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
        if not os.path.exists(_output_path):
            plot_msg(data_dir, _output_path, band)


export = plot_all_bands