# Plot Air Temprature
import pdbufr
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.cm import ScalarMappable
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from matplotlib.colors import Normalize, ListedColormap

# example usage:
# plot_airTemperature('airTemperature.webp',df)


def plot_airTemperature(outputPath, df):
    cmap='cividis_r'
    productKey = '#1#airTemperature'
    productLabel='Air Temperature'
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
    norm = Normalize(vmin=200, vmax=300)

    sc = ax.scatter(filtered_df['#1#longitude'], filtered_df['#1#latitude'],lw=1, c=filtered_df[productKey], norm=norm, cmap=cmap, transform=ccrs.PlateCarree(), s=1)
    # cbar = plt.colorbar(sc, orientation='vertical')
    # cbar.set_label(productLabel)
    # cbar.ax.set_position([cbar.ax.get_position().x0, cbar.ax.get_position().y0, cbar.ax.get_position().width, 0.55])
    # cbar.ax.tick_params(labelsize=12)

    fig.patch.set_alpha(0)
    fig.savefig(outputPath, transparent=True, format='webp', dpi=300, bbox_inches='tight', pad_inches=0)
    # fig.show()

export = plot_airTemperature

