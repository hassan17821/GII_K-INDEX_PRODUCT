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

def plot_kIndex(output_path, df):
    productKey = '#1#kIndex'
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
    productKey = '#1#parcelLiftedIndexTo500Hpa'
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


def plot_precipitable_water(df, outputPath, productKey, norm=None,cmap='Spectral_r'):
    latBound = [7.22, 37.454]
    lngBound = [43.753, 102.363]
    # Filter data based on latitude and longitude range
    filtered_df = df[
        (df['#1#latitude'] >= latBound[0])
        & (df['#1#latitude'] <= latBound[1])
        & (df['#1#longitude'] >= lngBound[0])
        & (df['#1#longitude'] <= lngBound[1])
    ]

    # Create the base map
    fig = plt.figure(figsize=(16, 16))
    ax = plt.axes(projection=ccrs.Mercator())
    ax.set_extent([lngBound[0], lngBound[1], latBound[0], latBound[1]], crs=ccrs.PlateCarree())
    # ax.add_feature(cfeature.LAND,  facecolor='white', alpha=0.1)
    # ax.add_feature(cfeature.OCEAN, facecolor='white', alpha=0.1)

    sc = ax.scatter(filtered_df['#1#longitude'], filtered_df['#1#latitude'], c=filtered_df[productKey], norm=norm, cmap=cmap, transform=ccrs.PlateCarree(), s=1)

    fig.savefig(outputPath, format='webp', dpi=300, bbox_inches='tight', pad_inches=0)

def plot_precipitableWater01(date, time, input_path, output_path, df):
    ranges = [0, 5, 10, 20, 50]
    norm = Normalize(vmin= min(ranges), vmax= max(ranges))
    plot_precipitable_water(df, output_path, '#1#precipitableWater', norm=norm, cmap='Spectral_r')    

def plot_precipitableWater02(date, time, input_path, outputPath, df):
    norm = None
    # norm = Normalize(vmin= 0, vmax= 50)
    plot_precipitable_water(df, outputPath, '#2#precipitableWater', norm=norm, cmap='Spectral_r')    

def plot_precipitableWater03(date, time, input_path, outputPath, df):
    norm = None
    # norm = Normalize(vmin= 0, vmax= 50)
    plot_precipitable_water(df, outputPath, '#3#precipitableWater', norm=norm, cmap='Spectral_r')    

def plot_precipitableWater04(date, time, input_path, outputPath, df):
    norm = None
    # norm = Normalize(vmin= 0, vmax= 50)
    plot_precipitable_water(df, outputPath, '#4#precipitableWater', norm=norm, cmap='Spectral_r')    

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

if len(sys.argv) == 5:
    # Extract command-line arguments
    date_arg, time_arg, input_path_arg, output_path_arg = sys.argv[1:]
    output_data = [
        {
            'output_path': f'{output_path_arg}/LRIT_GII_kIndex [{time_arg}].webp',
            'function_name': 'plot_kIndex'
        },
        {
            'output_path': f'{output_path_arg}/LRIT_GII_koIndex [{time_arg}].webp',
            'function_name': 'plot_koIndex'
        },
        {
            'output_path': f'{output_path_arg}/LRIT_GII_parcelLiftedIndexTo500Hpa [{time_arg}].webp',
            'function_name': 'plot_parcelLiftedIndexTo500Hpa'
        },
        {
            'output_path': f'{output_path_arg}/LRIT_GII_precipitableWater01 [{time_arg}].webp',
            'function_name': 'plot_precipitableWater01'
        }
    ]

    print(input_path_arg)
    # Check if output paths exist
    if all(os.path.exists(item['output_path']) for item in output_data):
        print("All output paths already exist")
    else:
        df = pdbufr.read_bufr(input_path_arg, columns=("latitude", "longitude", "kIndex","koIndex", "parcelLiftedIndexTo500Hpa", "precipitableWater"))
        for item in output_data:
            output_path = item['output_path']
            function_name = item['function_name']
            if not os.path.exists(output_path):
                print(f"Processing {function_name} {output_path}")
                globals()[function_name](date_arg, time_arg, input_path_arg, output_path, df)

else:
    print("Usage: python plot_kIndex.py <date> <time> <output_path>")

# Add map features
# ax.add_feature(cfeature.LAND, edgecolor='black', facecolor='lightgray')
# ax.add_feature(cfeature.BORDERS, linestyle=':')
# ax.add_feature(cfeature.OCEAN, facecolor='lightblue')
