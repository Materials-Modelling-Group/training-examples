# Coordinate Reference Systems in QGIS

## Understanding CRS

A Coordinate Reference System (CRS) defines how coordinates relate to positions on Earth.

**Two main types:**
1. **Geographic CRS**: Uses latitude/longitude (degrees)
   - Example: WGS84 (EPSG:4326)
   - Good for: GPS data, global visualization
   
2. **Projected CRS**: Uses x/y in meters or feet
   - Example: UTM Zone 36S (EPSG:32736)
   - Good for: Measurements, distance calculations, local analysis

## Checking Layer CRS

1. Right-click layer → **Properties**
2. Go to **Source** tab
3. Look for "Coordinate Reference System"

**Or** hover over layer name in Layers Panel to see CRS in tooltip.

## Project CRS

The Project CRS determines how layers are displayed together.

**To check/change:**
1. Look at bottom-right corner of QGIS window
2. Click the CRS code (e.g., "EPSG:4326")
3. Search for desired CRS
4. Click **OK**

**Note**: Changing project CRS only affects display, not the actual layer data.

## Recommended CRS for Kenya/East Africa

### For Visualization
- **WGS84 (EPSG:4326)**: Standard geographic CRS

### For Analysis
- **UTM Zone 36S (EPSG:32736)**: For most of Kenya
- **UTM Zone 37S (EPSG:32737)**: For eastern Kenya
- **Arc 1960 (EPSG:4210)**: Traditional reference

### For Web Maps
- **Web Mercator (EPSG:3857)**: Used by Google Maps, OpenStreetMap

## Reprojecting Layers

To actually change a layer's CRS:

1. Right-click layer → **Export → Save Features As...**
2. Choose output format (GeoPackage recommended)
3. Click CRS button
4. Search for target CRS (e.g., "32736" for UTM Zone 36S)
5. Set output filename
6. Click **OK**

## On-the-Fly Reprojection

QGIS automatically reprojects layers for display if they have different CRS.

**To enable/disable:**
1. **Project → Properties → CRS**
2. Check/uncheck "Enable on-the-fly CRS transformation"

**Note**: Always use same CRS for analysis to avoid errors!

## Finding the Right CRS

### For Your Data
1. Check documentation or metadata
2. Look at .prj file (for shapefiles)
3. Check coordinate values:
   - Lat/lon range (-90 to 90, -180 to 180) = Geographic
   - Large numbers (6-7 digits) = Projected

### For Your Analysis
Consider:
- Study area location
- Required measurements (distances, areas)
- Data sources (match their CRS)
- Output requirements

### Search Tools
- **EPSG.io**: https://epsg.io/ (search by location, country)
- **QGIS CRS Selector**: Type keywords like "Kenya UTM"

## Common CRS Codes
- EPSG:4326 
- WGS84 (lat/lon) EPSG:3857 
- Web Mercator EPSG:32636 
- UTM Zone 36N (Northern hemisphere) EPSG:32736 
- UTM Zone 36S (Southern hemisphere, for Kenya) EPSG:32737 
- UTM Zone 37S (Eastern Kenya) EPSG:4210 
- Arc 1960 EPSG:21036 
- Arc 1960 / UTM Zone 36S


1. **Always check CRS** when loading new data
2. **Use projected CRS** (UTM) for measurements and analysis
3. **Keep all layers in same CRS** for analysis
4. **Document CRS** in project notes
5. **Test measurements** - does 1 km actually equal 1 km?
