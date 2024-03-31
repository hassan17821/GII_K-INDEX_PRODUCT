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
from utils import plot_msg,is_daytime
from constants import day_products, night_products, all_bands

def plot_day_products(data_dir, output_path):
    for product_id in day_products:
        _output_path = output_path.replace('**placeholder_name**', product_id);
        if not os.path.exists(_output_path):
            plot_msg(data_dir, _output_path, product_id)


def plot_night_products(data_dir, output_path):
    for product_id in night_products:
        _output_path = output_path.replace('**placeholder_name**', product_id);
        if not os.path.exists(_output_path):
            plot_msg(data_dir, _output_path, product_id)

def plot_all_bands(data_dir, output_path):
    for band in all_bands:
        _output_path = output_path.replace('**placeholder_name**', band);
        if not os.path.exists(_output_path):
            plot_msg(data_dir, _output_path, band)


def plot_products(data_dir, output_path, date_arg, time_arg):
    # if is_daytime(time_arg):
    #     plot_day_products(data_dir,output_path)
    # else:
    #     plot_night_products(data_dir,output_path)
    plot_all_bands(data_dir, output_path)
    plot_day_products(data_dir,output_path)
    plot_night_products(data_dir,output_path)

export = plot_products