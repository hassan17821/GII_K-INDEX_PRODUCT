import pdbufr
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from matplotlib.colors import ListedColormap

# Read BUFR data
df = pdbufr.read_bufr('drive/MyDrive/GII.bufr', columns=("latitude", "longitude", "kIndex", "koIndex", "precipitableWater"))

# Filter data based on latitude and longitude range
filterd_df = df[
    (df['latitude'] >= 20)
    & (df['latitude'] <= 40)
    & (df['longitude'] >= 43.753)
    & (df['longitude'] <= 102.363)
    & (df['kIndex'] >= -30)
    & (df['kIndex'] <= 36)
]

print(filterd_df)
# Create the base map
fig = plt.figure(figsize=(16, 10))
ax = plt.axes(projection=ccrs.PlateCarree())
ax.set_extent([50, 90, 20, 40])

# Add map features
ax.add_feature(cfeature.LAND, edgecolor='black', facecolor='lightgray')
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS, linestyle=':')
ax.add_feature(cfeature.OCEAN, facecolor='lightblue')

# Define discrete colormap
num_colors = 10
cmap = plt.get_cmap('viridis', num_colors)
discrete_cmap = ListedColormap(cmap(np.linspace(0, 1, num_colors)))

# Plot the KIndex with discrete colors
sc = ax.scatter(
    filterd_df['longitude'],
    filterd_df['latitude'],
    c=filterd_df['kIndex'],
    cmap=discrete_cmap,
    transform=ccrs.PlateCarree(),
    s=1
)

# Add a colorbar
cbar = plt.colorbar(sc, ticks=np.linspace(filterd_df['kIndex'].min(), filterd_df['kIndex'].max(), num_colors))
cbar.set_label('K-Index')

# Add a title
plt.title('K-Index Plot')

# Show the plot
plt.show()
