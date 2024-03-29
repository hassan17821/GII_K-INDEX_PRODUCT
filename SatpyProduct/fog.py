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


def is_daytime(time_arg):
    # Assuming time_arg is in the format HH-MM
    hour, minute = map(int, time_arg.split('-'))
    time = datetime.now().replace(hour=hour, minute=minute)

    # Define daytime hours (you can adjust these as needed)
    day_start = datetime.now().replace(hour=6, minute=0, second=0)
    day_end = datetime.now().replace(hour=18, minute=0, second=0)

    return day_start <= time <= day_end

def plot_dayfog(data_dir,output_path):

    composites = ['fog']
    latBound = [7.22, 37.454]
    lngBound = [43.753, 102.363]

    files = os.listdir(data_dir)
    fnames = [os.path.join(data_dir, f) for f in files]

    print("FileNames Length :: ",len(fnames))
    if(len(fnames) < 140):
        print("Not enough files to process")
        return
    
    scn = Scene(reader='seviri_l1b_hrit', filenames=fnames)
    scn.load(composites)

    my_area = create_area_def('my_area', {'proj': 'merc', 'lon_0': 45.5},
                width=1500, height=850,
                area_extent=[lngBound[0], latBound[0], lngBound[1], latBound[1]],
                reduce_data=False,
                units='degrees')

    scn_resampled = scn.resample(my_area)
    print('Saving Day Fog')
    scn_resampled.save_dataset('fog', output_path)

def plot_nightfog(data_dir,output_path):

    composites = ['night_fog']
    latBound = [7.22, 37.454]
    lngBound = [43.753, 102.363]

    files = os.listdir(data_dir)
    fnames = [os.path.join(data_dir, f) for f in files]

    print("FileNames Length :: ",len(fnames))
    if(len(fnames) < 140):
        print("Not enough files to process")
        return
    
    scn = Scene(reader='seviri_l1b_hrit', filenames=fnames)
    scn.load(composites)

    my_area = create_area_def('my_area', {'proj': 'merc', 'lon_0': 45.5},
                width=1500, height=850,
                area_extent=[lngBound[0], latBound[0], lngBound[1], latBound[1]],
                reduce_data=False,
                units='degrees')

    scn_resampled = scn.resample(my_area)
    print('Saving Night Fog')
    scn_resampled.save_dataset('night_fog', output_path)

def plot_fog(data_dir,output_path,time_arg):
    if is_daytime(time_arg):
        plot_dayfog(data_dir,output_path)
    else:
        plot_nightfog(data_dir,output_path)

export = plot_fog