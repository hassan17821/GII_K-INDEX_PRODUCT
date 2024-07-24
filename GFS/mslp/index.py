# Required Libraries
# !pip install netCDF4 matplotlib cartopy scipy
# !pip install ecmwf-data ecmwf-opendata magpye
import netCDF4 as nc
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from scipy.ndimage import gaussian_filter, minimum_filter, maximum_filter
from urllib.parse import urlparse
from gfs_data_fetch import fetch_latest_data
import schedule
import time
import subprocess
from datetime import datetime
import os

def plot_mslp_isobars():    
    try:
        # Fetch The data url
        base_url = "http://nomads.ncep.noaa.gov:80/dods/gfs_0p25_1hr"
        latest_data_url = fetch_latest_data(base_url)

        print(latest_data_url)
        dataset = nc.Dataset(latest_data_url)
        parsed_url = urlparse(latest_data_url)
        path_parts = parsed_url.path.split('/')
        last_two = '/'.join(path_parts[-2:])

        # Extract the necessary variables
        latitudes = dataset.variables['lat'][:]
        longitudes = dataset.variables['lon'][:]
        mslp_var = dataset.variables['prmslmsl']
        time_var = dataset.variables['time']

        # Define the extent
        extent = (7.22, 43.753, 37.454, 102.363)

        # Define the time range
        time_range = np.arange(0, 3)

        # Loop through each time step and create plots
        for time_index in time_range:
            # Extract the MSLP data for the current time step and convert Pa to hPa (millibars)
            mslp = mslp_var[time_index, :, :] / 100

            # Apply Gaussian smoothing
            sigma = 2  # Adjust the sigma value for more or less smoothing
            mslp_smoothed = gaussian_filter(mslp, sigma=sigma)

            # Create a figure and an axis with Cartopy projection
            fig, ax = plt.subplots(figsize=(12, 6), subplot_kw={'projection': ccrs.PlateCarree()})

            # Plot the smoothed MSLP data with 2-millibar intervals
            contour = ax.contour(longitudes, latitudes, mslp_smoothed, levels=np.arange(np.min(mslp_smoothed), np.max(mslp_smoothed), 2), colors='black', linewidths=0.5)

            # Set the extent
            ax.set_extent([extent[1], extent[3], extent[0], extent[2]], crs=ccrs.PlateCarree())

            # Add pressure values on isobars
            ax.clabel(contour, inline=True, fontsize=8, fmt='%1.0f')

            # Find local maxima and minima
            neighborhood_size = 20
            local_min = minimum_filter(mslp_smoothed, size=neighborhood_size) == mslp_smoothed
            local_max = maximum_filter(mslp_smoothed, size=neighborhood_size) == mslp_smoothed

            # Get the coordinates of local minima and maxima
            min_coords = np.where(local_min)
            max_coords = np.where(local_max)

            # Annotate the high and low pressure areas within the bounds
            for lat_idx, lon_idx in zip(min_coords[0], min_coords[1]):
                lat = latitudes[lat_idx]
                lon = longitudes[lon_idx]
                if extent[0] <= lat <= extent[2] and extent[1] <= lon <= extent[3]:
                    ax.text(lon, lat, 'L', color='red', fontsize=12, fontweight='bold', ha='center', va='center')

            for lat_idx, lon_idx in zip(max_coords[0], max_coords[1]):
                lat = latitudes[lat_idx]
                lon = longitudes[lon_idx]
                if extent[0] <= lat <= extent[2] and extent[1] <= lon <= extent[3]:
                    ax.text(lon, lat, 'H', color='blue', fontsize=12, fontweight='bold', ha='center', va='center')

            fileName = f'mslp_isobars_{time_index}.webp'
            if(time_index == 0):
                fileName = f'mslp_isobars_current.svg'

            # current date in YYYY-MM-DD format
            current_date = datetime.today().strftime("%Y-%m-%d")
            folder_path = f'D:/server1/Archive/GFS/{current_date}'

            # Create the folder if it doesn't exist
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            plt.savefig(f'{folder_path}/{fileName}', format='svg', bbox_inches='tight', pad_inches=0, transparent=True)

            # Close the figure to avoid memory issues
            plt.close(fig)

    finally:
        # Close the dataset
        dataset.close()

def main():
    # Run the function immediately
    plot_mslp_isobars()
    
    # Then schedule it to run every 5 minutes
    schedule.every(5).minutes.do(plot_mslp_isobars)
    
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()