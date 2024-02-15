import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from matplotlib.colors import Normalize, ListedColormap, LinearSegmentedColormap

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

    sc = ax.scatter(filtered_df['#1#longitude'], filtered_df['#1#latitude'], c=filtered_df[productKey], norm=norm, cmap=cmap, transform=ccrs.PlateCarree(), s=1)

    fig.savefig(outputPath, format='webp', dpi=300, bbox_inches='tight', pad_inches=0)

def plot_totalPrecipitableWater( output_path, df):
    ranges = [0, 5, 10, 20, 50]
    norm = Normalize(vmin= min(ranges), vmax= max(ranges))
    plot_precipitable_water(df, output_path, '#1#precipitableWater', norm=norm, cmap='Spectral_r')    

def plot_precipitableWater10To500mbar( outputPath, df):
    norm = None
    # norm = Normalize(vmin= 0, vmax= 50)
    plot_precipitable_water(df, outputPath, '#2#precipitableWater', norm=norm, cmap='Spectral_r')    

def plot_precipitableWater500To850mbar( outputPath, df):
    norm = None
    # norm = Normalize(vmin= 0, vmax= 50)
    plot_precipitable_water(df, outputPath, '#3#precipitableWater', norm=norm, cmap='Spectral_r')    

def plot_precipitableWater850To1000mbar( outputPath, df):
    norm = None
    # norm = Normalize(vmin= 0, vmax= 50)
    plot_precipitable_water(df, outputPath, '#4#precipitableWater', norm=norm, cmap='Spectral_r')    

export = plot_totalPrecipitableWater, plot_precipitableWater10To500mbar, plot_precipitableWater500To850mbar, plot_precipitableWater850To1000mbar