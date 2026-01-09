# Geospatial Data Analysis Workflow

import geopandas as gpd
import pandas as pd
import folium

print("Loading geospatial data...")
gdf = gpd.read_file('/home/username/spatial_data.shp')

print(f"Loaded {len(gdf)} features")
print(f"CRS: {gdf.crs}")

# Calculate area
gdf['area_sqkm'] = gdf.geometry.area / 1_000_000

# Create buffer
gdf['geometry_buffered'] = gdf.geometry.buffer(1000)

# Create interactive map
center_lat = gdf.geometry.centroid.y.mean()
center_lon = gdf.geometry.centroid.x.mean()

m = folium.Map(location=[center_lat, center_lon], zoom_start=10)

for idx, row in gdf.iterrows():
    folium.GeoJson(
        row['geometry'],
        tooltip=f"Area: {row['area_sqkm']:.2f} sq km"
    ).add_to(m)

m.save('interactive_map.html')
print("Map saved to interactive_map.html")
