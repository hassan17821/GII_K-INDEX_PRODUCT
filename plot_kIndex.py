#K-Index
import sys
import pdbufr
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from matplotlib.colors import Normalize, ListedColormap, LinearSegmentedColormap

def plot_kIndex(date, time, input_path, output_path):

    print(date, time, input_path_arg, output_path)

    productKey = 'kIndex'
    productLabel = 'k-Index'
    imagePath = output_path
    latBound = [7.22, 37.454]
    lngBound = [43.753, 102.363]
    minMaxVal = [-20 , 50]
    ranges = [-20, -10, 0, 10, 20, 30, 40, 50]

    df = pdbufr.read_bufr(input_path, columns=("latitude", "longitude", "kIndex", "parcelLiftedIndexTo500Hpa", "precipitableWater"))

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
    ax = plt.axes(projection=ccrs.PlateCarree())
    ax.set_extent([lngBound[0], lngBound[1], latBound[0], latBound[1]])

    # Add map features
    ax.add_feature(cfeature.LAND, edgecolor='black', facecolor='lightgray')
    ax.add_feature(cfeature.BORDERS, linestyle=':')
    ax.add_feature(cfeature.OCEAN, facecolor='lightblue')

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
    sc = ax.scatter(filtered_df['longitude'], filtered_df['latitude'], c=filtered_df[productKey],
                    cmap=combined_cmap, transform=ccrs.PlateCarree(), s=1, norm=norm)

    # Save the figure using the provided output path
    fig.savefig(imagePath, format='webp', dpi=300, bbox_inches='tight', pad_inches=0)

    # Check if command-line arguments are provided
if len(sys.argv) == 5:
    # Extract command-line arguments
    date_arg, time_arg, input_path_arg, output_path_arg = sys.argv[1:]

    # Call the function with the provided arguments
    plot_kIndex(date_arg, time_arg, input_path_arg, output_path_arg)
else:
    print("Usage: python plot_kIndex.py <date> <time> <output_path>")
