#K-Index
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from matplotlib.colors import Normalize, ListedColormap, LinearSegmentedColormap

def plot_kIndex(output_path, df):
    productKey = '#1#kIndex'
    latBound = [7.22, 37.454]
    lngBound = [43.753, 102.363]
    minMaxVal = [-20 , 50]
    ranges = [-20, -10, 0, 10, 20, 30, 40, 50]

    # Filter data based on latitude and longitude range
    filtered_df = df[
        (df['#1#latitude'] >= latBound[0])
        & (df['#1#latitude'] <= latBound[1])
        & (df['#1#longitude'] >= lngBound[0])
        & (df['#1#longitude'] <= lngBound[1])
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
    sc = ax.scatter(filtered_df['#1#longitude'], filtered_df['#1#latitude'], c=filtered_df[productKey], cmap=combined_cmap, transform=ccrs.PlateCarree(), s=1, norm=norm)

    # Save the figure using the provided output path
    fig.patch.set_alpha(0)
    fig.savefig(output_path, transparent=True, format='webp', dpi=300, bbox_inches='tight', pad_inches=0)

export = plot_kIndex