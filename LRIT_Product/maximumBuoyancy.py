import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from matplotlib.colors import Normalize, ListedColormap, LinearSegmentedColormap

def plot_maximumBuoyancy(outputPath,df):
    latBound = [7.22, 37.454]
    lngBound = [43.753, 102.363]
    productKey = '#1#maximumBuoyancy'
    cmap = 'Spectral_r'

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
    norm = Normalize(vmin=-25, vmax=50)

    sc = ax.scatter(filtered_df['#1#longitude'], filtered_df['#1#latitude'], c=filtered_df[productKey], cmap=cmap, transform=ccrs.PlateCarree(), s=1, norm=norm)

    fig.patch.set_alpha(0)
    fig.savefig(outputPath, transparent=True, format='webp', dpi=300, bbox_inches='tight', pad_inches=0)

export = plot_maximumBuoyancy