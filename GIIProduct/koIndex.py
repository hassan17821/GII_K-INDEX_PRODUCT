#K-Index
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from matplotlib.colors import Normalize, ListedColormap, LinearSegmentedColormap

def plot_koIndex(output_path, df):
    productKey = '#1#koIndex'
    latBound = [7.22, 37.454]
    lngBound = [43.753, 102.363]
    ranges = [-16 , -8 , -4 , 0 , 10 , 20]
    minMaxVal = [-30 , 50]

    # Filter data based on latitude and longitude range
    filtered_df = df[
        (df['#1#latitude'] >= latBound[0])
        & (df['#1#latitude'] <= latBound[1])
        & (df['#1#longitude'] >= lngBound[0])
        & (df['#1#longitude'] <= lngBound[1])
        & (df[productKey] >= minMaxVal[0])
        & (df[productKey] <= minMaxVal[1])
    ]

    fig = plt.figure(figsize=(16, 16))
    ax = plt.axes(projection=ccrs.Mercator())
    ax.set_extent([lngBound[0], lngBound[1], latBound[0], latBound[1]], crs=ccrs.PlateCarree())

    # Define color ranges and corresponding normalization values
    norm = Normalize(vmin=minMaxVal[0], vmax=minMaxVal[1])

    # Plot the KIndex with the combined custom colormap
    sc = ax.scatter(filtered_df['#1#longitude'], filtered_df['#1#latitude'], c=filtered_df[productKey], cmap='Spectral', transform=ccrs.PlateCarree(), s=1, norm=norm)

    # Save the figure
    fig.savefig(output_path, format='webp', dpi=300, bbox_inches='tight', pad_inches=0)

export = plot_koIndex