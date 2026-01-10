# Buffer Analysis in QGIS

Buffers create zones of specified distance around features.

## Creating Basic Buffer

1. **Open Processing Toolbox**: 
   - **Processing → Toolbox** (or Ctrl+Alt+T)
   
2. **Search for "buffer"** in toolbox search box

3. **Double-click "Buffer"** tool

4. **Configure parameters**:
   - **Input layer**: Select your point, line, or polygon layer
   - **Distance**: Enter buffer distance
   - **Segments**: Higher number = smoother circles (default 5 is usually fine)
   - **Dissolve result**: Check if you want overlapping buffers merged
   - **Output**: Choose save location or leave as [temporary]
   
5. **Click "Run"**

6. New buffer layer appears on map

## Buffer Distance Units

The distance unit depends on your layer's CRS:
- **Projected CRS** (like UTM): Distance in meters
- **Geographic CRS** (lat/lon): Distance in degrees (not recommended!)

**Best Practice**: Always use projected CRS for buffer analysis

### Converting Units

If your layer is in lat/lon but you need meter buffers:
1. First reproject to projected CRS (see coordinate_systems.md)
2. Then create buffer

**Or** use the Processing tool that handles CRS:
1. Search for "Buffer" in toolbox
2. Look for parameters allowing distance in meters even for geographic layers

## Multiple Distance Buffers

Create multiple buffer rings:

1. **Processing Toolbox → Search "multi-ring buffer"**
2. **Or manually**:
   - Create 100m buffer → Name "buffer_100m"
   - Create 200m buffer → Name "buffer_200m"  
   - Create 300m buffer → Name "buffer_300m"
3. Style each with different colors

## Variable Distance Buffers

Buffer distance from attribute field:

1. **Processing Toolbox → Buffer**
2. **Distance**: Click expression button (ε)
3. Select attribute field with distances
4. Or write expression: `"distance_field" * 1000` (if field is in km)
5. Run

## Negative Buffers

Create inward buffer (erode) on polygons:

1. Use Buffer tool
2. Enter **negative distance** (e.g., -50)
3. Only works on polygon layers

## Buffer Analysis Workflow

### Example: Find buildings within 500m of river
Load rivers layer (lines)
Load buildings layer (points)
Create 500m buffer around rivers:
Processing → Buffer
Input: rivers
Distance: 500
Save as: "river_buffer_500m"
Select buildings within buffer:
Vector → Research Tools → Select by Location
Select features from: buildings
Where the features: intersect
By comparing to: river_buffer_500m
Run
Selected buildings are those within 500m
Export selected:
Right-click buildings → Export → Save Selected Features As
Name: "buildings_near_river"
￼

## Dissolving Buffers

Merge overlapping buffers into single feature:

1. **Create buffers** (don't check "dissolve" option)
2. **Processing → Dissolve**
3. Input: buffer layer
4. Optional: Dissolve by field to group certain buffers together
5. Run

## Buffer with Hole

Create donut-shaped buffer (e.g., 100m-200m from feature):
Create 200m buffer → Save as "outer"
Create 100m buffer → Save as "inner"
Vector → Geoprocessing Tools → Difference
Input: outer
Overlay: inner
Result: donut buffer (100m-200m zone)
￼

## Styling Buffers

Make buffers semi-transparent to see underlying features:

1. Right-click buffer layer → **Properties**
2. **Symbology**
3. Click color → Adjust **Opacity** slider (e.g., 50%)
4. Or change **Fill style** to "No Brush" and use only outline

## Applications

- **Proximity analysis**: What's within X distance?
- **Service areas**: 500m walking distance from bus stops
- **Protection zones**: Environmental buffers around sensitive areas
- **Risk assessment**: Flood risk within 100m of river
- **Land use planning**: Development restrictions near protected areas

