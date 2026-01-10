# Geoprocessing Operations in QGIS

Geoprocessing tools analyze spatial relationships between features.

## Accessing Geoprocessing Tools

**Vector → Geoprocessing Tools →** [tool name]

Or search in **Processing Toolbox** (Ctrl+Alt+T)

## Clip

Extract features from one layer that fall within boundary of another.

**Use case**: Extract buildings within study area

1. **Vector → Geoprocessing Tools → Clip**
2. **Input layer**: Features to clip (e.g., buildings)
3. **Overlay layer**: Boundary (e.g., district polygon)
4. **Clipped**: Output file location
5. Run

**Result**: Only buildings inside district boundary

## Intersection

Find where two layers overlap, keeping only overlapping parts with attributes from both.

**Use case**: Find protected forest areas

1. **Vector → Geoprocessing Tools → Intersection**
2. **Input layer**: Forests
3. **Overlay layer**: Protected areas
4. **Intersection**: Output location
5. Run

**Result**: Only forest areas that are also protected, with attributes from both layers

## Union

Combine two layers, keeping all features and attributes from both.

**Use case**: Combine multiple land ownership layers

1. **Vector → Geoprocessing Tools → Union**
2. **Input layer**: First ownership layer
3. **Overlay layer**: Second ownership layer
4. **Union**: Output
5. Run

**Result**: All features from both layers, split where they overlap

## Difference

Subtract overlaying features, keeping only parts that don't overlap.

**Use case**: Find unprotected forest (all forest minus protected areas)

1. **Vector → Geoprocessing Tools → Difference**
2. **Input layer**: All forests
3. **Overlay layer**: Protected areas
4. **Difference**: Output
5. Run

**Result**: Forest areas that are NOT protected

## Symmetrical Difference

Features from both layers that don't overlap.

**Use case**: Find areas that changed between two datasets

1. **Vector → Geoprocessing Tools → Symmetrical Difference**
2. **Input layer**: Year 2020 land use
3. **Overlay layer**: Year 2025 land use
4. **Symmetrical difference**: Output
5. Run

**Result**: Areas that appear in one year but not the other

## Dissolve

Merge features based on common attribute.

**Use case**: Combine districts into provinces

1. **Vector → Geoprocessing Tools → Dissolve**
2. **Input layer**: Districts
3. **Dissolve field(s)**: Province name
4. **Dissolved**: Output
5. Run

**Result**: One feature per province (districts merged)

**Tip**: Leave dissolve field empty to merge ALL features into one

## Buffer

(Covered in detail in 04_buffer_analysis.md)

Create zone of specified distance around features.

## Convex Hull

Smallest convex polygon containing all features.

**Use case**: General boundary around scattered points

1. **Vector → Geoprocessing Tools → Convex Hull**
2. **Input layer**: Points or lines
3. Run

**Result**: Polygon enclosing all features

## Centroid

Find geometric center of each feature.

**Use case**: Convert polygons to points at their center

1. **Vector → Geometry Tools → Centroids**
2. **Input layer**: Polygons
3. Run

**Result**: Point layer with points at polygon centers

## Voronoi Polygons (Thiessen Polygons)

Create polygons where any location inside is closer to that point than any other.

**Use case**: Service areas for point facilities

1. **Vector → Geometry Tools → Voronoi Polygons**
2. **Input layer**: Points (e.g., hospitals)
3. **Buffer region**: % to expand (usually 0)
4. Run

**Result**: Polygons dividing space into nearest-neighbor regions

## Spatial Join

Transfer attributes from one layer to another based on spatial relationship.

**Use case**: Add district name to every building

1. **Vector → Data Management Tools → Join Attributes by Location**
2. **Input layer**: Buildings (points)
3. **Join layer**: Districts (polygons)
4. **Geometric predicate**: 
   - **Intersects**: Most common
   - **Within**: Points must be inside polygons
   - **Contains**: For opposite direction
5. **Join type**:
   - **Take attributes of first located feature only**: One match per feature
   - **Take attributes of all located features**: All matches (creates multiple records)
6. Run

**Result**: Buildings with district attributes attached

## Merge (Combine Layers)

Combine multiple layers of same geometry type into one.

**Use case**: Combine multiple county shapefiles into one national layer

1. **Vector → Data Management Tools → Merge Vector Layers**
2. **Input layers**: Select all layers to merge
3. **Merged**: Output
4. Run

**Result**: Single layer with all features from all inputs

## Split Vector Layer

Divide one layer into multiple based on attribute.

**Use case**: Split national dataset into one shapefile per province

1. **Processing Toolbox → Search "split vector layer"**
2. **Input layer**: National dataset
3. **Unique ID field**: Province name
4. **Output directory**: Folder for output files
5. Run

**Result**: Separate file for each unique value in field

## Extract by Location

Select features based on spatial relationship with another layer.

**Use case**: Find schools within 1km of roads

1. Create 1km buffer around roads (see 04_buffer_analysis.md)
2. **Vector → Research Tools → Select by Location**
3. **Select features from**: Schools
4. **Where the features**: Intersect
5. **By comparing to features from**: Road buffer
6. Run
7. Selected schools are those near roads
8. **Right-click schools → Export → Save Selected Features As** to create new layer

## Aggregate

Combine features based on expression (advanced dissolve).

**Use case**: Sum population by region while merging polygons

1. **Vector → Geoprocessing Tools → Aggregate**
2. **Input layer**: Districts
3. **Group by expression**: "region_name"
4. **Aggregates**: Define for each field:
   - Geometry: first_value
   - population: sum
   - name: concatenate (with delimiter)
5. Run

**Result**: Merged features with calculated statistics

## Common Workflows

### Workflow 1: Protected vs Unprotected Forest
Goal: Calculate how much forest is protected vs unprotected

Load forest layer (polygons)
Load protected areas layer (polygons)
Intersection:
Input: forest
Overlay: protected areas
Output: "protected_forest"
Difference:
Input: forest
Overlay: protected areas
Output: "unprotected_forest"
Open attribute tables:
Add "area_ha" field to both
Calculate: $area / 10000
Statistics Panel:
Sum of protected_forest area_ha
Sum of unprotected_forest area_ha
Compare results

### Workflow 2: Service Area Analysis
Goal: Find underserved areas (far from health facilities)

Load health facilities (points)
Load district boundaries (polygons)
Buffer health facilities:
Distance: 5000 (5km)
Dissolve: Yes
Output: "served_areas"
Difference:
Input: districts
Overlay: served_areas
Output: "underserved_areas"
Calculate underserved area:
Open underserved_areas attribute table
Add "area_sqkm" field
Calculate: $area / 1000000
Identify districts with large underserved areas

### Workflow 3: Land Use by District
Goal: Calculate area of each land use type per district

Load land use (polygons with "type" field)
Load districts (polygons with "district_name" field)
Intersection:
Input: land use
Overlay: districts
Output: "land_use_by_district"
Dissolve:
Input: land_use_by_district
Dissolve fields: district_name, type
Output: "dissolved"
Calculate areas:
Add "area_ha" field
Calculate: $area / 10000
Pivot table (in spreadsheet):
Rows: district_name
Columns: type
Values: sum of area_ha

## Tips

- **Always check CRS**: All layers should use same projected CRS for analysis
- **Validate geometries**: Run **Vector → Geometry Tools → Check Validity** first
- **Temporary layers**: Use for intermediate steps, save final results
- **Processing History**: View → Panels → Processing History shows all operations
- **Graphical Modeler**: **Processing → Graphical Modeler** to automate workflows
- **Backup data**: Always keep original data unchanged
