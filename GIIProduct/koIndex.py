#K-Index
import pdbufr
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from matplotlib.colors import Normalize, ListedColormap, LinearSegmentedColormap

def plot_koIndex(output_path, df):

    # Read BUFR data
    # (Assuming 'df' is already defined)
    productKey = '#1#koIndex'
    productLabel = 'KO Index'

    # Set latitude and longitude bounds
    latBound = [7.22, 37.454]
    lngBound = [43.753, 102.363]
    ranges = [-16 , 2 , 6 , 20]
    # 14, 4, 14
    minMaxVal = [-16 , 20]
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

    # Add map features
    # ax.add_feature(cfeature.LAND, edgecolor='black', facecolor='lightgray')
    # ax.add_feature(cfeature.BORDERS, linestyle=':')
    # ax.add_feature(cfeature.OCEAN, facecolor='lightblue')

    brown_cmap = LinearSegmentedColormap.from_list('brown', ['#D2B48C', '#8B4513'], N=7)
    purple_cmap = LinearSegmentedColormap.from_list('blue', ['#A0A0E6', '#524788'], N=4)
    # yellow_cmap = LinearSegmentedColormap.from_list('green', ['#F0EB9F', '#A09D12'], N=4)
    red_cmap = LinearSegmentedColormap.from_list('red', ['#6C0000', '#FC8282'], N=9)

    # Combine the custom colormaps into one
    combined_cmap = ListedColormap(np.concatenate([
        red_cmap(np.linspace(0, 1, 18)),
        purple_cmap(np.linspace(0, 1, 4)),
        brown_cmap(np.linspace(0, 1, 14)),
    ]))

    # Define color ranges and corresponding normalization values
    norm = Normalize(vmin=minMaxVal[0], vmax=minMaxVal[1])

    # Plot the KIndex with the combined custom colormap
    sc = ax.scatter(filtered_df['#1#longitude'], filtered_df['#1#latitude'], c=filtered_df[productKey],
                    cmap=combined_cmap, transform=ccrs.PlateCarree(), s=1, norm=norm)

    # Save the figure
    # fig.savefig('drive/MyDrive/GII_09-45__2024-02-02.webp', format='webp', dpi=300, bbox_inches='tight',pad_inches=0)

    ## Add a colorbar with fixed ticks and labels
    # cbar = plt.colorbar(sc, ticks=ranges, orientation='vertical')
    # cbar.set_label(productLabel)
    # cbar.ax.set_position([cbar.ax.get_position().x0, cbar.ax.get_position().y0, cbar.ax.get_position().width, 0.55])
    # cbar.ax.tick_params(labelsize=12)

    ## Add a title
    # plt.title(productLabel + ' Plot')

    # plt.show()
    # Save the figure
    fig.savefig(output_path, format='webp', dpi=300, bbox_inches='tight', pad_inches=0)

export = plot_koIndex