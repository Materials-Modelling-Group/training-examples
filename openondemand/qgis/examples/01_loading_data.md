# Loading Data in QGIS

## Vector Data

### Loading a Shapefile
1. Click **Layer → Add Layer → Add Vector Layer** (or Ctrl+Shift+V)
2. Click the **...** button next to "Vector Dataset(s)"
3. Navigate to your shapefile (.shp)
4. Click **Add**
5. The layer appears in the Layers Panel

**Tip**: Shapefiles consist of multiple files (.shp, .shx, .dbf, .prj). Always keep them together.

### Loading GeoJSON
1. **Layer → Add Layer → Add Vector Layer**
2. Browse to your .geojson or .json file
3. Click **Add**

### Loading GeoPackage
1. **Layer → Add Layer → Add Vector Layer**
2. Browse to your .gpkg file
3. If the GeoPackage contains multiple layers, select which to load
4. Click **Add**

**Advantage**: GeoPackage can store multiple layers in a single file.

### Loading CSV with Coordinates
1. **Layer → Add Layer → Add Delimited Text Layer**
2. Select your CSV file
3. In "Geometry Definition":
   - Choose "Point coordinates"
   - Set X field (longitude) and Y field (latitude)
   - Set Geometry CRS (usually EPSG:4326 for lat/lon)
4. Click **Add**

## Raster Data

### Loading GeoTIFF
1. **Layer → Add Layer → Add Raster Layer** (or Ctrl+Shift+R)
2. Browse to your .tif or .tiff file
3. Click **Add**

### Loading Satellite Imagery
1. **Layer → Add Layer → Add Raster Layer**
2. Navigate to your satellite data file
3. For multi-band imagery:
   - Right-click layer → Properties
   - Go to Symbology tab
   - Choose band combinations for RGB display

## Online Data Sources

### Adding OpenStreetMap Basemap
1. Install QuickMapServices plugin:
   - **Plugins → Manage and Install Plugins**
   - Search "QuickMapServices"
   - Click **Install Plugin**
2. **Web → QuickMapServices → OSM → OSM Standard**

### Adding XYZ Tiles
1. **Browser Panel → XYZ Tiles → Right-click → New Connection**
2. Enter:
   - Name: "OpenStreetMap"
   - URL: `https://tile.openstreetmap.org/{z}/{x}/{y}.png`
3. Click **OK**
4. Drag the connection onto the map canvas

## Checking Loaded Data

After loading:
1. Check layer appears in **Layers Panel**
2. Right-click layer → **Zoom to Layer** to see it
3. Right-click → **Open Attribute Table** to view data
4. Right-click → **Properties → Source** to check CRS

## Common Issues

**Layer doesn't display:**
- Check if layer is checked (visible) in Layers Panel
- Verify CRS matches or can be reprojected
- Check if layer has valid extent (Zoom to Layer)

**Coordinates in wrong location:**
- Wrong CRS assumed during import
- Reload with correct CRS specification
- Or reproject: Right-click → Export → Save Features As (choose correct CRS)
