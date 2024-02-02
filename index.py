# GII - k-Index
import pdbufr
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from matplotlib.colors import ListedColormap, Normalize

# Read BUFR data
# (Assuming 'df' is already defined)
productKey = 'kIndex'
productLabel = 'k-Index'

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

# Define custom colors for different ranges
brown_shades = ['#8B4513', '#8B4513', '#A0522D', '#A0522D', '#CD853F', '#CD853F', '#DEB887', '#DEB887', '#FFE4B5', '#FFE4B5',
                '#FFDAB9', '#FFDAB9', '#FFC0CB', '#FFC0CB', '#FFB6C1', '#FFB6C1', '#FF69B4', '#FF69B4', '#FF1493', '#FF1493']
purple_shades = ['#800080', '#7B68EE', '#6A5ACD', '#483D8B', '#4B0082']
green_shades = ['#008000', '#006400', '#228B22', '#32CD32', '#ADFF2F']
red_shades = ['#FF6347', '#FF4500', '#DC143C', '#8B0000', '#800000']

# Concatenate all color shades
colors = brown_shades + purple_shades + green_shades + red_shades

# Define color ranges and corresponding normalization values
ranges = [20, 10 , 0 , -10 , -20, -30 , -40, -50]
norm = Normalize(vmin=min(ranges), vmax=max(ranges))

# Create a custom colormap
cmap = ListedColormap(colors)

# Plot the KIndex
sc = ax.scatter(filtered_df['longitude'], filtered_df['latitude'], c=filtered_df[productKey], cmap=cmap, norm=norm, transform=ccrs.PlateCarree(), s=1)

# Add a colorbar
cbar = plt.colorbar(sc)
cbar.set_label(productLabel)

# Add a title
plt.title(productLabel + ' Plot')

# Show the plot
plt.show()


# GPT Code
# Given the code use custom palette colors 

# -20 -> -10 -> 0 ->  -10 ->  20  (20 brown shade shades decreasing , E each b/w i.e -20 -> -10) 
# 20 to 30  (5 purple shades decreasing ) 
# 30to 40  (5 yellow shades decreasing ) 
# 40to 50  (5 red shades decreasing ) 