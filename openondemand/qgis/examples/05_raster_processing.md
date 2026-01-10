# Raster Data Processing in QGIS

Raster data consists of grid cells (pixels) with values, like satellite imagery or elevation models.

## Loading Raster Data

1. **Layer → Add Layer → Add Raster Layer** (Ctrl+Shift+R)
2. Browse to .tif, .img, or other raster file
3. Click **Add**

## Viewing Raster Properties

1. Right-click raster layer → **Properties**
2. **Information tab**: See dimensions, pixel size, extent, CRS
3. **Symbology tab**: Adjust visualization
4. **Transparency tab**: Set transparency or no-data values

## Changing Color Ramp

1. **Properties → Symbology**
2. **Render type**: 
   - **Singleband gray**: For single-band rasters (elevation)
   - **Multiband color**: For RGB imagery
   - **Singleband pseudocolor**: Color ramp for elevation/values
3. For pseudocolor:
   - Choose **Color ramp** (e.g., "Spectral", "Terrain")
   - Set **Min** and **Max** values
   - **Mode**: Continuous or Equal Interval
   - Click **Classify**
4. Click **OK**

## Hillshade (3D Effect from Elevation)

1. **Raster → Analysis → Hillshade**
2. **Input layer**: Your elevation/DEM layer
3. **Z factor**: Usually 1 (exaggeration)
4. **Azimuth**: Light direction (315° = northwest, default)
5. **Altitude**: Light angle (45° default)
6. **Output**: Choose save location
7. Click **Run**

**Result**: Shaded relief showing terrain

**Tip**: Overlay semi-transparent hillshade on colored elevation for best effect

## Slope Analysis

1. **Raster → Analysis → Slope**
2. **Input**: Elevation layer
3. **Slope expressed as**: Degrees or Percent
4. **Output**: Save location
5. Run

**Result**: Map showing terrain steepness

## Aspect (Direction of Slope)

1. **Raster → Analysis → Aspect**
2. **Input**: Elevation layer
3. Run

**Result**: Direction each slope faces (0°=North, 90°=East, etc.)

## Raster Calculator

Perform mathematical operations on raster bands.

### Example: Calculate NDVI from Satellite Imagery

NDVI = (NIR - Red) / (NIR + Red)

1. **Raster → Raster Calculator**
2. **Expression**: Build formula:
("satellite@4" - "satellite@3") / ("satellite@4" + "satellite@3")

￼
   Where:
   - @4 = Near-Infrared band
   - @3 = Red band
3. **Output layer**: Name (e.g., "ndvi.tif")
4. Click **OK**

**Result**: NDVI values (-1 to 1, higher = more vegetation)

### Example: Convert Elevation from Meters to Feet
"elevation@1" * 3.28084

￼

## Reclassification

Change continuous values to categories.

### Method 1: Raster Calculator

Create categories manually:
("elevation@1" >= 0 AND "elevation@1" < 500) * 1 +
("elevation@1" >= 500 AND "elevation@1" < 1000) * 2 +
("elevation@1" >= 1000 AND "elevation@1" < 2000) * 3 +
("elevation@1" >= 2000) * 4

￼

Result: 1=lowland, 2=hills, 3=mountains, 4=high mountains

### Method 2: r.reclass (GRASS)

1. **Processing → Toolbox → Search "r.reclass"**
2. Define reclassification rules
3. Run

## Clipping Raster

Clip raster to area of interest:

1. **Raster → Extraction → Clip Raster by Extent**
2. **Input**: Raster to clip
3. **Clipping extent**: 
   - Type coordinates
   - Or click **"..."** → Calculate from Layer (choose boundary layer)
4. **Output**: Save location
5. Run

**Or use mask layer**:
1. **Raster → Extraction → Clip Raster by Mask Layer**
2. **Mask layer**: Polygon defining area
3. Run

## Resampling

Change pixel size:

1. **Raster → Projections → Warp (Reproject)**
2. **Input**: Original raster
3. **Target CRS**: Choose if reprojecting
4. **Resampling method**:
   - **Nearest neighbor**: Categorical data (land use)
   - **Bilinear/Cubic**: Continuous data (elevation)
5. **Output resolution**: Set new pixel size
6. Run

## Mosaicking (Merging Rasters)

Combine multiple rasters into one:

1. **Raster → Miscellaneous → Merge**
2. **Input layers**: Select all rasters to merge
3. **Output data type**: Match input or choose
4. **Output**: Save location
5. Run

## Zonal Statistics

Calculate statistics for raster within polygon zones:

1. **Raster → Zonal Statistics → Zonal Statistics**
2. **Raster layer**: Your raster (e.g., elevation)
3. **Vector layer**: Polygons (e.g., districts)
4. **Output column prefix**: Name for new columns
5. **Statistics to calculate**: Check desired (Mean, Min, Max, Sum, Count, etc.)
6. Run

**Result**: Polygon layer gets new attributes with statistics

**Example**: Average elevation per district

## Raster to Vector

Convert raster to polygons:

1. **Raster → Conversion → Polygonize**
2. **Input**: Raster layer
3. **Name of the field**: Attribute name for pixel values
4. **Output**: Vector file location
5. Run

**Use case**: Convert classified land cover raster to polygons

## Tips

- **Large rasters**: Use pyramids for faster display
  - Right-click → Properties → Pyramids → Build Pyramids
- **No-data values**: Set in Properties → Transparency
- **Color consistency**: Save and load .qml style files
- **Processing chains**: Use Graphical Modeler to automate workflows

## Common Applications

- **Elevation analysis**: Slope, aspect, hillshade, watersheds
- **Vegetation monitoring**: NDVI from satellite imagery
- **Suitability mapping**: Combine multiple raster criteria
- **Change detection**: Compare multi-temporal imagery
- **Terrain modeling**: 3D visualization and analysis

