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
from utils import plot_msg,is_time_present
from constants import products

def plot_product(data_dir,output_path, product_ids,fnames,time_arg):
    for product in product_ids:
        productKey = product['product_key']
        productTitle = product['product_title']
        productType = product['product_type']
        validTimeArgs = product['valid_time_args']
        isTimeValid = is_time_present(time_arg, validTimeArgs)
        _output_path = output_path.replace('**placeholder_name**', productTitle);            
        if os.path.isfile(_output_path):
            print(f'File already exists: {_output_path}')
        else:
            if not isTimeValid:
                print(f'Invalid Time {time_arg} for {productKey}: {_output_path}')
                continue
            plot_msg(data_dir, _output_path, productKey,fnames)

def plot_products(data_dir, output_path, date_arg, time_arg, fnames):
    # if is_daytime(time_arg):
    #     plot_product(data_dir,output_path,day_products)
    # else:
    #     plot_product(data_dir,output_path,night_products)
    # plot_product(data_dir, output_path, day_products,fnames)
    # plot_product(data_dir,output_path, night_products,fnames)
    plot_product(data_dir,output_path,products,fnames,time_arg)

export = plot_products