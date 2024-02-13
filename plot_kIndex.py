#K-Index
import os
import sys
import pdbufr
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from matplotlib.colors import Normalize, ListedColormap, LinearSegmentedColormap
import threading

def plot_kIndex(date, time, input_path, output_path, df):
    productKey = 'kIndex'
    productLabel = 'k-Index'
    latBound = [7.22, 37.454]
    lngBound = [43.753, 102.363]
    minMaxVal = [-20 , 50]
    ranges = [-20, -10, 0, 10, 20, 30, 40, 50]

    # Filter data based on latitude and longitude range
    filtered_df = df[
        (df['latitude'] >= latBound[0])
        & (df['latitude'] <= latBound[1])
        & (df['longitude'] >= lngBound[0])
        & (df['longitude'] <= lngBound[1])
        & (df[productKey] >= minMaxVal[0])
        & (df[productKey] <= minMaxVal[1])
    ]

    # Create the base map
    fig = plt.figure(figsize=(16, 16))
    ax = plt.axes(projection=ccrs.Mercator())
    ax.set_extent([lngBound[0], lngBound[1], latBound[0], latBound[1]], crs=ccrs.PlateCarree())

    brown_cmap = LinearSegmentedColormap.from_list('brown', ['#D2B48C', '#8B4513'], N=20)
    purple_cmap = LinearSegmentedColormap.from_list('blue', ['#A0A0E6', '#524788'], N=5)
    yellow_cmap = LinearSegmentedColormap.from_list('green', ['#A09D12', '#F0EB9F'], N=5)
    red_cmap = LinearSegmentedColormap.from_list('red', ['#6C0000', '#FC8282'], N=5)

    # Combine the custom colormaps into one
    combined_cmap = ListedColormap(np.concatenate([
        brown_cmap(np.linspace(0, 1, 20)),
        purple_cmap(np.linspace(0, 1, 5)),
        yellow_cmap(np.linspace(0, 1, 5)),
        red_cmap(np.linspace(0, 1, 5)),
    ]))

    # Define color ranges and corresponding normalization values
    norm = Normalize(vmin=minMaxVal[0], vmax=minMaxVal[1])

    # Plot the KIndex with the combined custom colormap
    sc = ax.scatter(filtered_df['longitude'], filtered_df['latitude'], c=filtered_df[productKey], cmap=combined_cmap, transform=ccrs.PlateCarree(), s=1, norm=norm)

    # Save the figure using the provided output path
    fig.savefig(output_path, format='webp', dpi=300, bbox_inches='tight', pad_inches=0)


def plot_parcelLiftedIndexTo500Hpa(date, time, input_path, output_path, df):
    productKey = 'parcelLiftedIndexTo500Hpa'
    latBound = [7.22, 37.454]
    lngBound = [43.753, 102.363]
    ranges = [-16 , -8 , -4 , 0 , 10 , 20]
    minMaxVal = [-16 , 20]

    # Filter data based on latitude and longitude range
    filtered_df = df[
        (df['latitude'] >= latBound[0])
        & (df['latitude'] <= latBound[1])
        & (df['longitude'] >= lngBound[0])
        & (df['longitude'] <= lngBound[1])
        & (df[productKey] >= minMaxVal[0])
        & (df[productKey] <= minMaxVal[1])
    ]

    fig = plt.figure(figsize=(16, 16))
    ax = plt.axes(projection=ccrs.Mercator())
    ax.set_extent([lngBound[0], lngBound[1], latBound[0], latBound[1]], crs=ccrs.PlateCarree())

    brown_cmap = LinearSegmentedColormap.from_list('brown', ['#D2B48C', '#8B4513'], N=20)
    purple_cmap = LinearSegmentedColormap.from_list('blue', ['#A0A0E6', '#524788'], N=4)
    yellow_cmap = LinearSegmentedColormap.from_list('green', ['#F0EB9F', '#A09D12'], N=4)
    red_cmap = LinearSegmentedColormap.from_list('red', ['#6C0000', '#FC8282'], N=8)

    # Combine the custom colormaps into one
    combined_cmap = ListedColormap(np.concatenate([
        red_cmap(np.linspace(0, 1, 8)),
        yellow_cmap(np.linspace(0, 1, 4)),
        purple_cmap(np.linspace(0, 1, 4)),
        brown_cmap(np.linspace(0, 1, 20)),
    ]))

    # Define color ranges and corresponding normalization values
    norm = Normalize(vmin=minMaxVal[0], vmax=minMaxVal[1])

    # Plot the KIndex with the combined custom colormap
    sc = ax.scatter(filtered_df['longitude'], filtered_df['latitude'], c=filtered_df[productKey], cmap=combined_cmap, transform=ccrs.PlateCarree(), s=1, norm=norm)

    # Save the figure
    fig.savefig(output_path, format='webp', dpi=300, bbox_inches='tight', pad_inches=0)


def plot_PrecipitableWater(date, time, input_path, output_path, df):
    productKey = 'precipitableWater'
    latBound = [7.22, 37.454]
    lngBound = [43.753, 102.363]

    # Filter data based on latitude and longitude range
    filtered_df = df[
    (df['latitude'] >= latBound[0])
    & (df['latitude'] <= latBound[1])
    & (df['longitude'] >= lngBound[0])
    & (df['longitude'] <= lngBound[1])
    ]

    # Create the base map
    fig = plt.figure(figsize=(16, 16))
    ax = plt.axes(projection=ccrs.Mercator())
    ax.set_extent([lngBound[0], lngBound[1], latBound[0], latBound[1]], crs=ccrs.PlateCarree())

    # Save the figure
    sc = ax.scatter(filtered_df['longitude'], filtered_df['latitude'], c=filtered_df[productKey], cmap='Spectral', transform=ccrs.PlateCarree(), s=1)

    fig.savefig(output_path, format='webp', dpi=300, bbox_inches='tight', pad_inches=0)
    

def plot_koIndex(date, time, input_path, output_path, df):
    productKey = 'koIndex'
    productLabel = 'kO Index'
    latBound = [7.22, 37.454]
    lngBound = [43.753, 102.363]
    ranges = [-16 , -8 , -4 , 0 , 10 , 20]
    minMaxVal = [-30 , 50]

    # Filter data based on latitude and longitude range
    filtered_df = df[
        (df['latitude'] >= latBound[0])
        & (df['latitude'] <= latBound[1])
        & (df['longitude'] >= lngBound[0])
        & (df['longitude'] <= lngBound[1])
        & (df[productKey] >= minMaxVal[0])
        & (df[productKey] <= minMaxVal[1])
    ]

    fig = plt.figure(figsize=(16, 16))
    ax = plt.axes(projection=ccrs.Mercator())
    ax.set_extent([lngBound[0], lngBound[1], latBound[0], latBound[1]], crs=ccrs.PlateCarree())

    # Define color ranges and corresponding normalization values
    norm = Normalize(vmin=minMaxVal[0], vmax=minMaxVal[1])

    # Plot the KIndex with the combined custom colormap
    sc = ax.scatter(filtered_df['longitude'], filtered_df['latitude'], c=filtered_df[productKey], cmap='Spectral', transform=ccrs.PlateCarree(), s=1, norm=norm)

    # Save the figure
    fig.savefig(output_path, format='webp', dpi=300, bbox_inches='tight', pad_inches=0)


def process_function(date_arg, time_arg, input_path_arg, output_path, function_name, df):
    if not os.path.exists(output_path):
        print(f"Processing {function_name} {output_path}")
        globals()[function_name](date_arg, time_arg, input_path_arg, output_path, df)


if len(sys.argv) == 5:
    # Extract command-line arguments
    date_arg, time_arg, input_path_arg, output_path_arg = sys.argv[1:]
    output_paths = [
        f'{output_path_arg}/LRIT_GII_KINDEX [{time_arg}].webp',
        f'{output_path_arg}/LRIT_GII_KOINDEX [{time_arg}].webp',
        f'{output_path_arg}/LRIT_GII_PRECIPITABLE_WATER [{time_arg}].webp',
        f'{output_path_arg}/LRIT_GII_parcelLiftedIndexTo500Hpa [{time_arg}].webp'
    ]
    function_names = [
        "plot_kIndex",
        "plot_koIndex",
        "plot_PrecipitableWater",
        "plot_parcelLiftedIndexTo500Hpa"
    ]

    print(input_path_arg)
    # Check if output paths exist
    if all(os.path.exists(path) for path in output_paths):
        print("All output paths already exist")
    else:
        df = pdbufr.read_bufr(input_path_arg, columns=("latitude", "longitude", "kIndex","koIndex", "parcelLiftedIndexTo500Hpa", "precipitableWater"))
        threads = []
        for output_path, function_name in zip(output_paths, function_names):
            thread = threading.Thread(target=process_function, args=(date_arg, time_arg, input_path_arg, output_path, function_name, df))
            thread.start()
            threads.append(thread)
        
        for thread in threads:
            thread.join()

else:
    print("Usage: python plot_kIndex.py <date> <time> <output_path>")


# Add map features
# ax.add_feature(cfeature.LAND, edgecolor='black', facecolor='lightgray')
# ax.add_feature(cfeature.BORDERS, linestyle=':')
# ax.add_feature(cfeature.OCEAN, facecolor='lightblue')
