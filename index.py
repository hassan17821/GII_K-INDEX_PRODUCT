# Given the code , issues with this code is
# 1- 'kIndex' has negative values but color bar showing only positive ones
# 2- Given the information about product color contrast of values not good

#  "The GII product consists of a set of indices which describe atmospheric air mass instability in cloud free areas. These indices are highly empirical in nature and might even be only relevant in certain geographic regions or under certain circumstances" 
import pdbufr
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

# Read BUFR data

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

# Plot the KIndex
sc = ax.scatter(filterd_df['longitude'], filterd_df['latitude'], c=filterd_df['kIndex'], cmap='RdBu', transform=ccrs.PlateCarree(), s=1)

# Add a colorbar
cbar = plt.colorbar(sc)
cbar.set_label('K-Index')

# Add a title
plt.title('K-Index Plot')

# Show the plot
plt.show()
