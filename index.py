# GII - k-Index
import pdbufr
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from matplotlib.colors import Normalize

# Read BUFR data
# (Assuming 'df' is already defined)
productKey = 'kIndex'
productLabel = 'k-Index'
colorScheme = 'Spectral'
# Filter data based on latitude and longitude range
filtered_df = df[
    (df['latitude'] >= 20)
    & (df['latitude'] <= 40)
    & (df['longitude'] >= 50)
    & (df['longitude'] <= 90)
    & (df[productKey] >= -50)
    & (df[productKey] <= 20)
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

# Define color ranges and corresponding normalization values
ranges = [20, 10, 0, -10, -20, -30, -40, -50]
norm = Normalize(vmin=min(ranges), vmax=max(ranges))

# Plot the KIndex
sc = ax.scatter(filtered_df['longitude'], filtered_df['latitude'], c=filtered_df[productKey], cmap=colorScheme, transform=ccrs.PlateCarree(), s=1, norm=norm)

# Add a colorbar with fixed ticks and labels
cbar = plt.colorbar(sc, ticks=ranges, orientation='vertical')
cbar.set_label(productLabel)

# Add a title
plt.title(productLabel + ' Plot')


# GPT Code
# Given the code use custom palette colors 

# -20 -> -10 -> 0 ->  -10 ->  20  (20 brown shade shades decreasing , E each b/w i.e -20 -> -10) 
# 20 to 30  (5 purple shades decreasing ) 
# 30to 40  (5 yellow shades decreasing ) 
# 40to 50  (5 red shades decreasing ) 