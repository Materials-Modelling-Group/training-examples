# Workflow 2: Site Suitability Analysis

Identify optimal locations based on multiple spatial criteria.

## Objective

Find suitable locations for a facility (e.g., solar farm, school, clinic) based on multiple geographic constraints.

## Example Scenario

Find suitable locations for a solar farm requiring:
- Flat terrain (slope < 5°)
- Near roads (within 1km)
- Away from settlements (> 2km)
- Not in protected areas
- Not on agricultural land
- Sufficient area (> 10 hectares contiguous)

## Data Requirements

- Digital Elevation Model (DEM) raster
- Roads layer (lines)
- Settlements layer (points or polygons)
- Protected areas layer (polygons)
- Land use layer (polygons)
- Study area boundary (polygon)

## Step 1: Prepare Data

### Set Project CRS
1. Check all layers CRS
2. Choose appropriate projected CRS (UTM zone for area)
3. Reproject all layers if needed

### Clip to Study Area
1. **Vector → Geoprocessing Tools → Clip**
2. Clip each vector layer to study area boundary
3. **Raster → Extraction → Clip Raster by Mask Layer**
4. Clip DEM to study area

## Step 2: Criterion 1 - Slope

### Calculate Slope from DEM
1. **Raster → Analysis → Slope**
2. **Input layer**: DEM
3. **Slope expressed as**: Percent
4. **Output**: "slope.tif"
5. Run

### Reclassify Slope (Suitable = slope < 5%)
1. **Raster → Raster Calculator**
2. Expression:
"slope@1" <= 5) * 1
3. **Output**: "slope_suitable.tif"
4. Run

**Result**: 1 = suitable, 0 = unsuitable

## Step 3: Criterion 2 - Distance to Roads

### Buffer Roads (1km)
1. **Vector → Geoprocessing Tools → Buffer**
2. **Input**: Roads
3. **Distance**: 1000 (meters)
4. **Dissolve**: Yes
5. **Output**: "roads_1km_buffer"
6. Run

### Rasterize Buffer
1. **Raster → Conversion → Rasterize**
2. **Input**: roads_1km_buffer
3. **Fixed value**: 1
4. **Output resolution**: Match DEM (check DEM properties for pixel size)
5. **Extent**: Study area
6. **Output**: "roads_suitable.tif"
7. Run

**Result**: 1 = near roads (suitable), 0 = far from roads

## Step 4: Criterion 3 - Distance from Settlements

### Buffer Settlements (2km exclusion)
1. **Vector → Geoprocessing Tools → Buffer**
2. **Input**: Settlements
3. **Distance**: 2000 (meters)
4. **Dissolve**: Yes
5. **Output**: "settlements_2km_buffer"
6. Run

### Rasterize (Invert Logic)
1. **Raster → Conversion → Rasterize**
2. **Input**: settlements_2km_buffer
3. **Fixed value**: 0
4. Match DEM resolution and extent
5. **Output**: "temp_settlements.tif"
6. Run

### Invert (Make areas OUTSIDE buffer = 1)
1. **Raster → Raster Calculator**
2. Expression:
("temp_settlements@1" = 0) * 1
3. **Output**: "settlements_suitable.tif"
4. Run

**Result**: 1 = far from settlements (suitable), 0 = near settlements

## Step 5: Criterion 4 - Not in Protected Areas

### Create Protected Areas Mask
1. **Raster → Conversion → Rasterize**
2. **Input**: Protected areas polygons
3. **Fixed value**: 0 (unsuitable)
4. Match DEM resolution and extent
5. **Output**: "temp_protected.tif"
6. Run

### Invert
1. **Raster → Raster Calculator**
2. Expression:
("temp_protected@1" = 0) * 1
3. **Output**: "protected_suitable.tif"

**Result**: 1 = not protected (suitable), 0 = protected

## Step 6: Criterion 5 - Not Agricultural Land

### Extract Land Use Code
(Assuming "type" field in land use layer)

1. Select agricultural features:
   - Open attribute table
   - Select by Expression: `"type" = 'Agriculture'`
   - Export selected: "agriculture.shp"

### Rasterize and Invert
1. **Raster → Conversion → Rasterize**
2. **Input**: agriculture
3. **Fixed value**: 0
4. **Output**: "temp_agric.tif"
5. Run

6. **Raster Calculator**:
("temp_agric@1" = 0) * 1
7. **Output**: "landuse_suitable.tif"

## Step 7: Combine All Criteria

### Multiply All Suitability Rasters
1. **Raster → Raster Calculator**
2. Expression:
"slope_suitable@1" *
"roads_suitable@1" *
"settlements_suitable@1" *
"protected_suitable@1" *
"landuse_suitable@1"
3. **Output**: "suitability_combined.tif"
4. Run

**Result**: 
- 1 = suitable (meets ALL criteria)
- 0 = unsuitable (fails at least one criterion)

## Step 8: Identify Suitable Areas

### Vectorize Suitable Areas
1. **Raster → Conversion → Polygonize**
2. **Input**: suitability_combined
3. **Name of field**: "suitable"
4. **Output**: "suitable_polygons"
5. Run

### Filter for Suitable Only
1. Open attribute table
2. Select by Expression:
"suitable" = 1
3. Right-click → Export → Save Selected Features As
4. Name: "suitable_areas_all"

## Step 9: Apply Minimum Area Requirement

### Calculate Areas
1. Open suitable_areas_all attribute table
2. Enable editing
3. Add field: "area_ha" (Decimal)
4. Field Calculator:
$area / 10000
5. Save edits

### Filter by Minimum Size
1. Select by Expression:
"area_ha" >= 10
2. Export selected: "suitable_areas_final"

**Result**: Polygons meeting all criteria AND size requirement

## Step 10: Rank Suitability

### Add Ranking Field
1. Open suitable_areas_final attribute table
2. Sort by "area_ha" descending
3. Add field: "rank" (Integer)
4. Manually number 1, 2, 3... or use expression:
@row_number

### Style by Rank
1. **Properties → Symbology → Graduated**
2. **Value**: rank or area_ha
3. **Color ramp**: Green (most suitable) to yellow
4. Classify and OK

## Step 11: Create Final Map

### Print Layout
1. **Project → New Print Layout**
2. Add map canvas
3. Add layers:
   - Background: Basemap or satellite imagery
   - Overlay: Suitable areas (semi-transparent)
   - Reference: Roads, settlements, boundaries

### Legend
1. **Add Item → Add Legend**
2. Show:
   - Suitable areas (by rank)
   - Roads
   - Settlements
   - Protected areas
   - Study area boundary

### Annotations
1. Add text: Criteria used
2. Add labels: Top ranked sites
3. Add North arrow and scale bar

### Export
1. **Layout → Export as Image/PDF**
2. Save

## Step 12: Create Report

### Summary Table

| Rank | Site ID | Area (ha) | Nearest Road (km) | Notes |
|------|---------|-----------|-------------------|-------|
| 1 | A | 45.2 | 0.3 | Largest site |
| 2 | B | 32.1 | 0.5 | Good access |
| 3 | C | 28.7 | 0.8 | Near substation |

### Criteria Summary
Document all criteria and rationale

### Recommendations
List top 3-5 sites with justification

## Advanced: Weighted Suitability

Instead of Boolean (yes/no), assign scores:
Slope (0-5%): Score = 10
Slope (5-10%): Score = 7
Slope (10-15%): Score = 3
Slope (>15%): Score = 0
Distance to roads:
0-500m: Score = 10
500-1000m: Score = 7
1000-2000m: Score = 3

2000m: Score = 0


**Raster Calculator**:
"slope_score@1" * 0.3 +
"roads_score@1" * 0.3 +
"settlements_score@1" * 0.2 +
"landuse_score@1" * 0.2

(Weights sum to 1.0)

**Result**: Scores from 0-10, higher = more suitable

## Tips

- **Sensitivity analysis**: Try different distance thresholds
- **Stakeholder input**: Validate criteria with experts
- **Ground truthing**: Visit top sites to verify
- **Alternative scenarios**: What if criteria change?
- **Document assumptions**: Record all decisions
