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
from satpy.enhancements import create_colormap
from satpy.enhancements import palettize
from datetime import datetime
import numpy as np
from satpy.dataset import combine_metadata

import os
from pyresample import create_area_def
from satpy import Scene

def plot_msg(data_dir, output_path, composite, fnames):
    try:
        latBound = [7.22, 37.454]
        lngBound = [43.753, 102.363]

        scn = Scene(reader='seviri_l1b_hrit', filenames=fnames)
        scn.load([composite])

        my_area = create_area_def('my_area', {'proj': 'merc', 'lon_0': 45.5},
                                  width=1500, height=850,
                                  area_extent=[lngBound[0], latBound[0], lngBound[1], latBound[1]],
                                  reduce_data=False,
                                  units='degrees')

        scn_resampled = scn.resample(my_area)
        print("Saving File : " + output_path)
        scn_resampled.save_dataset(composite, output_path)
    except ValueError as ve:
        print("Value Error : ", output_path)
        print(ve)
    except Exception as e:
        print("Some Error  : ",output_path)
        print(e)



def plot_ndvi(output_path,  fnames):
    try:
        bands = [
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

        latBound = [7.22, 37.454]
        lngBound = [43.753, 102.363]

        scn = Scene(reader='seviri_l1b_hrit', filenames=fnames)

        scn.load(bands)

        my_area = create_area_def('my_area', {'proj': 'merc', 'lon_0': 45.5},
                    width=1500, height=850,
                    area_extent=[lngBound[0], latBound[0], lngBound[1], latBound[1]],
                    reduce_data=False,
                    units='degrees')

        scn_resampled = scn.resample(my_area)
        ndvi = (scn_resampled["IR_039"] - scn_resampled["IR_016"]) / (scn_resampled["IR_039"] + scn_resampled["IR_016"])
        # ndvi = (scn_resampled["IR_087"] - scn_resampled["VIS006"]) / (scn_resampled["IR_087"] + scn_resampled["VIS006"])

        ndvi.attrs = combine_metadata(scn_resampled[0.8], scn_resampled[0.6])
        ndvi.attrs.pop("standard_name")
        # ndvi_masked = np.where(ndvi < 0.94, ndvi, np.nan) 
        # Display NDVI
        fig = plt.figure(figsize=(10, 8))
        plt.axis('off')
        plt.imshow(ndvi, cmap='RdYlGn')
        # plt.colorbar(label='NDVI')
        # plt.title('Normalized Difference Vegetation Index (NDVI)')
        # plt.show()
            # Save the figure using the provided output path
        fig.patch.set_alpha(0)
        print("Saving File : " + output_path)
        fig.savefig(output_path, transparent=True, format='webp', dpi=300, bbox_inches='tight', pad_inches=0)
    except ValueError as ve:
        print("Value Error : ", output_path)
        print(ve)
    except Exception as e:
        print("Some Error  : ",output_path)
        print(e)

# Example usage:
# plot_msg("data_dir_path", "output_path", "composite_name")
def is_daytime(time_arg):
    # Assuming time_arg is in the format HH-MM
    hour, minute = map(int, time_arg.split('-'))
    time = datetime.now().replace(hour=hour, minute=minute)

    # Define daytime hours (you can adjust these as needed)
    day_start = datetime.now().replace(hour=6, minute=0, second=0)
    day_end = datetime.now().replace(hour=18, minute=0, second=0)

    return day_start <= time <= day_end

def is_time_present(time_to_check, time_ranges):
    for time_range in time_ranges:
        if time_to_check == time_range:
            return True
    return False

def generate_time_range(min_time='00:00', max_time='23:45', interval_minutes=15):
    min_hour, min_minute = map(int, min_time.split(':'))
    max_hour, max_minute = map(int, max_time.split(':'))
    
    time_args = []
    current_hour = min_hour
    current_minute = min_minute

    while current_hour < max_hour or (current_hour == max_hour and current_minute <= max_minute):
        time_args.append(pad_zero(current_hour) + "-" + pad_zero(current_minute))
        current_minute += interval_minutes

        if current_minute >= 60:
            current_hour += 1
            current_minute = 0

    return time_args

def generate24HourTimeRange(): 
    return generate_time_range('00:00', '23:45', 15)

def generateDayTimeRange ():
    return generate_time_range('00:00', '23:45', 15)
    # return generate_time_range('04:00', '18:00', 15)

def generateNightTimeRange():
    return generate_time_range('00:00', '23:45', 15)
    # return generate_time_range('00:00', '03:45', 15) +generate_time_range('18:15', '23:45', 15);

def pad_zero(num):
    return str(num).zfill(2)

export = plot_msg,is_daytime,is_time_present, generate24HourTimeRange,generateDayTimeRange,generateNightTimeRange,plot_ndvi