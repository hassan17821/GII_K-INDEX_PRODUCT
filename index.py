# Given the code , issues with this code is
# 1- 'kIndex' has negative values but color bar showing only positive ones
# 2- Given the information about product color contrast of values not good

#  "The GII product consists of a set of indices which describe atmospheric air mass instability in cloud free areas. These indices are highly empirical in nature and might even be only relevant in certain geographic regions or under certain circumstances" 

import pdbufr
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import altair as alt

# Read BUFR data
df = pdbufr.read_bufr('drive/MyDrive/GII.bufr', columns=("latitude", "longitude", "kIndex", "koIndex", "precipitableWater"))

# Filter data based on latitude and longitude range
df = df[
    (df['latitude'] >= 7.22)
    & (df['latitude'] <= 37.454)
    & (df['longitude'] >= 43.753)
    & (df['longitude'] <= 102.363)
]

print(df)
# Create the base map
fig = plt.figure(figsize=(16, 10))
ax = plt.axes(projection=ccrs.PlateCarree())
ax.set_extent([43.753, 102.363, 7.22, 34.454])

# Add map features
ax.add_feature(cfeature.LAND, edgecolor='black', facecolor='lightgray')
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS, linestyle=':')
ax.add_feature(cfeature.OCEAN, facecolor='lightblue')

# Plot the KIndex
sc = ax.scatter(df['longitude'], df['latitude'], c=df['kIndex'], cmap='terrain', transform=ccrs.PlateCarree(), s=1)

# Add a colorbar
cbar = plt.colorbar(sc)
cbar.set_label('KIndex')

# Add a title
plt.title('K-Index Plot')

# Set the projection to EPSG:4326
# ax.set_global()

# Show the plot
plt.show()