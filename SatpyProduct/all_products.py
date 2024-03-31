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

def plot_product(data_dir, output_path, product_ids,fnames):
    for product_id in product_ids:
        _output_path = output_path.replace('**placeholder_name**', product_id);
        if os.path.isfile(_output_path):
            print(f'File already exists: {_output_path}')
        else:
            plot_msg(data_dir, _output_path, product_id,fnames)

def plot_products(data_dir, output_path, date_arg, time_arg, fnames):
    # if is_daytime(time_arg):
    #     plot_product(data_dir,output_path,day_products)
    # else:
    #     plot_product(data_dir,output_path,night_products)
    plot_product(data_dir, output_path, day_products,fnames)
    plot_product(data_dir,output_path, night_products,fnames)
    plot_product(data_dir,output_path, all_bands,fnames)

export = plot_products