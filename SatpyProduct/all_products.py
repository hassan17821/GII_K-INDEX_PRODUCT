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

def is_daytime(time_arg):
    # Assuming time_arg is in the format HH-MM
    hour, minute = map(int, time_arg.split('-'))
    time = datetime.now().replace(hour=hour, minute=minute)

    # Define daytime hours (you can adjust these as needed)
    day_start = datetime.now().replace(hour=6, minute=0, second=0)
    day_end = datetime.now().replace(hour=18, minute=0, second=0)

    return day_start <= time <= day_end

def plot_day_products(data_dir, output_path):
    product_ids=[
    'airmass',
    'ash',
    'cloud_phase_distinction',
    'cloud_phase_distinction_raw',
    'cloudtop',
    'cloudtop_daytime',
    'colorized_ir_clouds',
    'convection',
    'day_microphysics',
    'day_microphysics_winter',
    'dust',
    'fog',
    'green_snow',
    'hrv_clouds',
    'hrv_fog',
    'hrv_severe_storms',
    'hrv_severe_storms_masked',
    'ir108_3d',
    'ir_cloud_day',
    'ir_overview',
    'ir_sandwich',
    'natural_color',
    'natural_color_nocorr',
    'natural_color_raw',
    'natural_color_raw_with_night_ir',
    'natural_color_with_night_ir',
    'natural_color_with_night_ir_hires',
    'natural_enh',
    'natural_enh_with_night_ir',
    'natural_enh_with_night_ir_hires',
    'natural_with_night_fog',
    # 'night_fog',
    # 'night_ir_alpha',
    # 'night_ir_with_background',
    # 'night_ir_with_background_hires',
    # 'night_microphysics',
    'overview',
    'overview_raw',
    'realistic_colors',
    'rocket_plume_day',
    'rocket_plume_night',
    'snow',
    'vis_sharpened_ir'
    ]

    for product_id in product_ids:
        _output_path = output_path.replace('**product_name**', product_id);
        if not os.path.exists(_output_path):
            plot_msg(data_dir, _output_path, product_id)


def plot_night_products(data_dir, output_path):
    
    night_products = [
    'night_fog',
    'night_ir_alpha',
    'night_ir_with_background',
    'night_ir_with_background_hires',
    'night_microphysics',
    ]

    for product_id in night_products:
        _output_path = output_path.replace('**product_name**', product_id);
        if not os.path.exists(_output_path):
            plot_msg(data_dir, _output_path, product_id)


def plot_products(data_dir, output_path, date_arg, time_arg):
    # if is_daytime(time_arg):
    #     plot_day_products(data_dir,output_path)
    # else:
    #     plot_night_products(data_dir,output_path)
    plot_day_products(data_dir,output_path)
    plot_night_products(data_dir,output_path)

export = plot_products