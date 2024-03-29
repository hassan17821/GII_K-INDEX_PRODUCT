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
debug_on()


def plot_dayfog(data_dir,output_path, df):

    composites = ['fog']
    latBound = [7.22, 37.454]
    lngBound = [43.753, 102.363]

    # List all files in the directory
    # data_dir = "Z:/Data/XRIT/Archive/MSG2_IODC/2024-01-08/09-00"
    # data_dir = "M:/Archive/MSG2_IODC/2024-03-27/09-00"
    # data_dir = "M:/Archive/MSG2_IODC/2024-03-28/11-00"
    # data_dir = "Z:/Data/XRIT/Archive/MSG2_IODC/2024-03-29/05-30"

    files = os.listdir(data_dir)
    fnames = [os.path.join(data_dir, f) for f in files]
    print("fileNames Length :: ",len(fnames))
    # From Glob Data
    # data_dir = "Z:/Data/XRIT/Raw/*202403280700*";
    # fnames = glob(data_dir)
    if(len(fnames) < 140):
        print("Not enough files to process")
        return
    
    print(fnames)
    scn = Scene(reader='seviri_l1b_hrit', filenames=fnames)
    print(scn.available_dataset_names())
    print(scn.available_composite_names())  

    scn.load(composites)

    my_area = create_area_def('my_area', {'proj': 'merc', 'lon_0': 45.5},
                width=1500, height=850,
                area_extent=[lngBound[0], latBound[0], lngBound[1], latBound[1]],
                reduce_data=False,
                units='degrees')

    scn_resampled = scn.resample(my_area)
    xarr_dataset = scn_resampled.to_xarray_dataset(composites[0])
    # print(scn_resampled.to_xarray_dataset(composites[0]))

    # scn_resampled.save_dataset('airmass', 'airmass.png')
    scn_resampled.save_datasets(writer='simple_image', keep_palette=True)
    scn_resampled.save_datasets(writer='geotiff')
    # img = scn.images()
    scn_resampled.show(composites[0])

    # palettize(composites[0])
    # cmap = create_colormap({'filename':
    # './ir_colortable1.npy'})

    # print(cmap.values)
    # print(cmap.colors)
    # print(cmap.values)
    # print(cmap.colors)

    # img = to_image(composites[0])
    # img.show()

    # Create colorbar for the loaded dataset

export = plot_kIndex