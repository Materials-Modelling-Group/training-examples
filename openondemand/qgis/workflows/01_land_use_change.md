# Workflow 1: Land Use Change Analysis

Compare land use or land cover between two time periods.

## Objective

Identify areas where land use has changed and quantify the changes.

## Data Requirements

- Land use/cover layer from Year 1 (e.g., 2015)
- Land use/cover layer from Year 2 (e.g., 2025)
- Both should have attribute indicating land use type
- Both should be in same CRS (preferably projected)

## Step 1: Prepare Data

### Load Layers
1. **Layer → Add Vector Layer**
2. Load "landuse_2015.shp" → Rename to "LU2015"
3. Load "landuse_2025.shp" → Rename to "LU2025"

### Check CRS
1. Right-click each layer → **Properties → Source**
2. Verify both use same CRS
3. If different, reproject:
   - Right-click → Export → Save Features As
   - Choose target CRS
   - Save as new file

### Check Attributes
1. Open attribute table for each layer
2. Verify land use type field exists (e.g., "type" or "class")
3. Check values are consistent between years

## Step 2: Ensure Same Extent

If layers don't cover exactly the same area:

1. **Vector → Geoprocessing Tools → Clip**
2. Clip both layers to common boundary
3. Or use intersection of both extents

## Step 3: Create Change Detection Layer

### Intersect Both Layers
1. **Vector → Geoprocessing Tools → Intersection**
2. **Input layer**: LU2015
3. **Overlay layer**: LU2025
4. **Output**: "landuse_change"
5. Run

**Result**: Each polygon represents an area with its land use from both years

### Examine Attribute Table
1. Open "landuse_change" attribute table
2. You should see fields from both years:
   - "type_2015" (from Year 1)
   - "type_2025" (from Year 2)

## Step 4: Identify Changes

### Calculate Change Status
1. Open attribute table
2. Enable editing (Ctrl+E)
3. Add new field:
   - Name: "change_status"
   - Type: String
   - Length: 50
4. **Field Calculator**
5. Update existing field: "change_status"
6. Expression:
CASE
WHEN "type_2015" = "type_2025" THEN 'No Change'
ELSE 'Changed'
END
7. OK

### Create Change Category Field
1. Add another field: "change_type"
2. Field Calculator:
CASE
WHEN "type_2015" = "type_2025" THEN 'No Change'
ELSE "type_2015" || ' to ' || "type_2025"
END

Example output: "Forest to Urban", "Agriculture to Forest", etc.

3. Save edits

## Step 5: Calculate Areas

1. Add field: "area_ha" (Decimal, 10.2)
2. Field Calculator:
$area / 10000
3. Save edits

## Step 6: Visualize Changes

### Categorized Symbology
1. **Properties → Symbology**
2. **Categorized**
3. **Value**: "change_type"
4. **Color ramp**: Choose intuitive colors
   - Green shades: Gains in vegetation
   - Red/Brown: Losses in vegetation
   - Blue: Water changes
   - Gray: No change
5. **Classify**
6. Adjust colors for each category
7. OK

### Alternative: Show Only Changes
1. Filter layer to show only changed areas:
   - Bottom of attribute table
   - Advanced Filter (Expression)
   - Expression: `"change_status" = 'Changed'`
   - OK
2. Or select unchanged:
   - Select by Expression
   - `"change_status" = 'No Change'`
   - Right-click layer → Toggle Selected Features

## Step 7: Generate Statistics

### Summary by Change Type
1. Open attribute table
2. **Statistics Panel** (if not visible: View → Panels → Statistics Panel)
3. Select "change_type" column
4. Note Count of each change type

### Calculate Total Areas
1. Select by Expression to isolate specific change:
"change_type" = 'Forest to Urban'
2. Statistics Panel → "area_ha" column
3. Note Sum

Repeat for other important changes

### Export Statistics
1. **Processing → Toolbox → Search "Statistics by categories"**
2. **Input layer**: landuse_change
3. **Field to calculate statistics on**: area_ha
4. **Field with categories**: change_type
5. Run

**Result**: Table with sum of areas by change type

## Step 8: Create Summary Report

### Calculate Percentages
Total changed area ÷ Total area × 100

### Major Changes Table

| Change Type | Area (ha) | % of Total |
|-------------|-----------|------------|
| Forest to Agriculture | 5,240 | 12.3% |
| Agriculture to Urban | 2,100 | 4.9% |
| Forest to Urban | 1,800 | 4.2% |
| No Change | 33,560 | 78.6% |

## Step 9: Create Maps

### Before Map (2015)
1. Create new Print Layout
2. Add map of LU2015 layer
3. Style by land use type
4. Add legend, title, scale bar
5. Export as PDF/PNG

### After Map (2025)
1. New Print Layout
2. Add map of LU2025 layer
3. Same styling
4. Add legend, title, scale bar
5. Export

### Change Map
1. New Print Layout
2. Add map of landuse_change layer
3. Styled by change_type
4. Legend showing change categories
5. Title: "Land Use Change 2015-2025"
6. Export

## Step 10: Export Results

### Export Change Layer
1. Right-click landuse_change → Export → Save Features As
2. GeoPackage or Shapefile
3. Save to project folder

### Export Statistics
1. Right-click layer → Export → Save Features As
2. CSV format
3. Open in spreadsheet for further analysis

## Advanced Analysis

### Transition Matrix

Create matrix showing all transitions:

| From \ To | Forest | Agriculture | Urban | Water |
|-----------|--------|-------------|-------|-------|
| **Forest** | 15,000 | 2,000 | 800 | 50 |
| **Agriculture** | 500 | 20,000 | 1,500 | 100 |
| **Urban** | 0 | 0 | 5,000 | 0 |
| **Water** | 10 | 50 | 0 | 1,200 |

Create using pivot table in spreadsheet from exported data

### Hot Spot Analysis

Find where changes are concentrated:

1. Convert change polygons to points (centroids)
2. **Processing → Heatmap** (Kernel Density)
3. Input: Change centroids
4. Weight field: area_ha
5. Run

**Result**: Raster showing change density hotspots

## Tips

- **Ensure data quality**: Check for topology errors before analysis
- **Consistent classification**: Both years must use same land use categories
- **Minimum mapping unit**: Small slivers may be artifacts, not real change
- **Validation**: Ground-truth significant changes if possible
- **Temporal resolution**: More than 2 time periods = trend analysis
