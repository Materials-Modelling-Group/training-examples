# Attribute Table Operations in QGIS

The attribute table stores non-spatial data about features.

## Opening Attribute Table

1. Right-click layer → **Open Attribute Table**
2. Or click layer, press **F6**
3. Or click **Open Attribute Table** icon in toolbar

## Understanding the Attribute Table

- **Rows**: Each feature (point, line, polygon)
- **Columns**: Attributes (properties) of features
- **Header**: Column names (field names)

## Selecting Features

### Select by Clicking in Table
1. Click row number to select feature
2. **Ctrl+Click**: Select multiple
3. **Shift+Click**: Select range
4. Selected features highlight on map

### Select by Expression
1. **Select features using an expression** (icon or Ctrl+F)
2. **Expression dialog** opens
3. Build expression, examples:
"population" > 10000
"district" = 'Nairobi'
"area_sqkm" >= 100 AND "area_sqkm" <= 500
"name" LIKE 'Mt%'  (starts with "Mt")

4. Click **Select Features**
5. Features matching expression are selected

### Select All
- **Select All** button (Ctrl+A)

### Deselect All
- **Deselect All** button (Ctrl+Shift+A)

### Invert Selection
- **Invert Selection** button (Ctrl+R)

## Viewing Selected Features Only

At bottom of attribute table:
- **Show All Features** (default)
- **Show Selected Features**: View only selected
- **Show Features Visible on Map**: Based on current map extent

## Sorting Data

Click column header to sort by that field:
- First click: Ascending order
- Second click: Descending order

## Filtering Data

1. Click **Filter/Select features** button (bottom left)
2. **Column filter** appears below headers
3. Type in any column to filter
4. Only matching rows display

Or use **Advanced Filter (Expression)**:
1. Filter icon → **Advanced Filter**
2. Build expression like selection
3. Click **OK**

## Calculating New Fields

### Field Calculator

1. **Open Attribute Table**
2. Click **Field Calculator** icon (abacus) or Ctrl+I
3. **Expression** tab opens

**To create new field:**
1. Check **Create a new field**
2. **Output field name**: Name your field
3. **Output field type**: 
   - **Integer**: Whole numbers
   - **Decimal (real)**: Numbers with decimals
   - **String**: Text
   - **Date**: Dates
4. **Output field length**: Max characters
5. **Precision**: Decimal places (for real numbers)
6. Build expression
7. Click **OK**

### Examples

**Calculate area in square kilometers:**
$area / 1000000

(Assumes layer is in projected CRS with meters)

**Calculate population density:**
"population" / "area_sqkm"

**Concatenate text fields:**
"first_name" || ' ' || "last_name"

**Conditional calculation:**
CASE
WHEN "population" > 100000 THEN 'Large'
WHEN "population" > 10000 THEN 'Medium'
ELSE 'Small'
END

**Current date:**
now()


**Length of line features:**
$length

**Perimeter of polygons:**
$perimeter


## Editing Attribute Values

### Enable Editing
1. Click **Toggle Editing Mode** (pencil icon) or press Ctrl+E
2. Table cells become editable

### Manual Editing
1. Double-click cell to edit
2. Type new value
3. Press Enter

### Edit Multiple Features
1. Select features to edit
2. **Open Field Calculator**
3. **Uncheck** "Create a new field"
4. Check **Update existing field**
5. Choose field to update
6. Build expression
7. Check **Only update selected features**
8. Click **OK**

### Save Edits
1. Click **Save Edits** icon or Ctrl+S
2. Changes are permanent

### Cancel Edits
1. Click **Toggle Editing Mode** again
2. Click **Discard** to cancel changes

## Adding New Fields

1. **Toggle Editing Mode**
2. **New Field** button (or Ctrl+W)
3. Set:
   - **Name**: Field name (no spaces, start with letter)
   - **Type**: Integer, Real, String, Date
   - **Length**: Maximum characters
   - **Precision**: Decimal places (for Real)
4. Click **OK**

## Deleting Fields

1. **Toggle Editing Mode**
2. **Delete Field** button
3. Select field(s) to delete
4. Click **OK**
5. **Save Edits**

## Joining Tables

Attach attributes from one table to another based on common field.

### Example: Join census data to districts

1. Load district polygons
2. Load census CSV with matching district names/codes
3. **Right-click district layer → Properties → Joins tab**
4. Click **Green Plus** (+) button
5. Set:
   - **Join layer**: Census table
   - **Join field**: ID field in census (e.g., "district_code")
   - **Target field**: Matching field in districts (e.g., "code")
   - **Custom field name prefix**: Optional prefix for joined fields
6. Click **OK**
7. Open attribute table - census fields now appear

**Tip**: To make join permanent, export layer: **Right-click → Export → Save Features As**

## Relating Tables (One-to-Many)

When one feature relates to multiple records (e.g., one farm, multiple crops).

1. **Properties → Relations tab**
2. Click **Add Relation**
3. Configure relationship
4. Click **OK**

In attribute table, related records show in form view.

## Exporting Attribute Data

### As CSV
1. **Right-click layer → Export → Save Features As**
2. **Format**: CSV
3. **File name**: Choose location
4. Check **Export only selected features** if needed
5. Click **OK**

### Copy to Clipboard
1. Select cells or rows
2. **Ctrl+C** to copy
3. Paste into spreadsheet

## Statistics Panel

Quick statistics for any field:

1. **View → Panels → Statistics Panel**
2. In attribute table, click column header
3. Statistics Panel shows: Count, Sum, Mean, Median, Min, Max, etc.

## Finding Features

1. **Find** button in toolbar
2. Type search term
3. Matching features highlight

Or use **Select by Expression** for complex searches

## Form View vs Table View

Toggle between views:
- **Table View**: Spreadsheet style (default)
- **Form View**: One feature at a time with form layout

Switch with icons at bottom-right of attribute table

## Tips

- **Read-only formats**: Some formats (like WFS) can't be edited
- **Field names**: No spaces, start with letter, keep short
- **Backup**: Always backup before editing
- **Virtual fields**: Create calculated fields that update automatically
  - Field Calculator → **Create virtual field** checkbox
- **Conditional formatting**: Style features based on attributes
  - Symbology → Rule-based or Data defined override

## Common Workflows

### Calculate area for all polygons
Open attribute table
Enable editing
Add new field "area_ha" (Real type)
Field Calculator:
Update existing field: "area_ha"
Expression: $area / 10000
Save edits

### Select features by multiple criteria
Select by Expression
Expression: "land_use" = 'Forest' AND "area_ha" > 100 AND "slope_percent" < 15
Select Features
Export selected as new layer

### Update field based on another field
Enable editing
Field Calculator
Update existing field: "status"
Expression: CASE WHEN "area_ha" > 1000 THEN 'Large' WHEN "area_ha" > 100 THEN 'Medium' ELSE 'Small' END
OK
Save edits
