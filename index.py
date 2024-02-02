import pdbufr
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from matplotlib.colors import LinearSegmentedColormap

# Read BUFR data
# df = pdbufr.read_bufr('drive/MyDrive/GII.bufr', columns=("latitude", "longitude", "kIndex", "koIndex", "precipitableWater"))

# Filter data based on latitude and longitude range
filtered_df = df[
    (df['latitude'] >= 20)
    & (df['latitude'] <= 40)
    & (df['longitude'] >= 50)
    & (df['longitude'] <= 90)
    & (df['kIndex'] >= -30)
    & (df['kIndex'] <= 36)
]

# Create the base map
fig = plt.figure(figsize=(16, 10))
ax = plt.axes(projection=ccrs.PlateCarree())
ax.set_extent([50, 90, 20, 40])

# Add map features
ax.add_feature(cfeature.LAND, edgecolor='black', facecolor='lightgray')
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS, linestyle=':')
ax.add_feature(cfeature.OCEAN, facecolor='lightblue')

# Define a custom colormap
colors = [(0.8, 0, 0),(1, 0.5, 0.16),(1, 0, 0.7),(1, 1, 0.27), (0.29, 0.66, 0.16),(0.16, 0.37, 0.9)]  # Blue to Green to Yellow to Orange to Red

n_bins = 10  # Number of color bins
cmap_name = 'custom_contrast'
custom_cmap = LinearSegmentedColormap.from_list(cmap_name, colors, N=n_bins)

# Plot the KIndex with custom colormap
sc = ax.scatter(
    filtered_df['longitude'],
    filtered_df['latitude'],
    c=filtered_df['kIndex'],
    cmap=custom_cmap,
    transform=ccrs.PlateCarree(),
    s=1
)

# Add a colorbar
cbar = plt.colorbar(sc, ticks=np.linspace(filtered_df['kIndex'].min(), filtered_df['kIndex'].max(), n_bins))
cbar.set_label('K-Index')

# Add a title
plt.title('K-Index Plot')

# Show the plot
plt.show()
