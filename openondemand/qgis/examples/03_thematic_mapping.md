# Creating Thematic Maps in QGIS

Thematic maps visualize spatial patterns in data using colors, symbols, or sizes.

## Single Symbol Styling

All features display with same symbol (default).

1. Right-click layer → **Properties**
2. Go to **Symbology** tab
3. Ensure "Single Symbol" is selected
4. Click color box to change color
5. Adjust other properties (size, stroke, etc.)
6. Click **OK**

## Categorized Styling

Different symbols for discrete categories (e.g., land use types).

1. Open layer **Properties → Symbology**
2. Change dropdown from "Single Symbol" to **"Categorized"**
3. **Value**: Select attribute column with categories
4. **Color ramp**: Choose color scheme
5. Click **Classify** to generate categories
6. Adjust colors by clicking on each color
7. Click **OK**

**Example**: Land use with categories "Forest", "Urban", "Agriculture"

## Graduated Styling

Colors representing numeric ranges (e.g., population density).

1. **Properties → Symbology**
2. Select **"Graduated"**
3. **Value**: Choose numeric attribute
4. **Color ramp**: Select color scheme
5. **Mode**: Choose classification method:
   - **Equal Interval**: Divides range into equal parts
   - **Quantile**: Equal number of features per class
   - **Natural Breaks (Jenks)**: Minimizes within-class variance
   - **Standard Deviation**: Based on mean and std dev
6. **Classes**: Set number of categories (default 5)
7. Click **Classify**
8. Adjust break values if needed
9. Click **OK**

**Example**: Population per district with 5 classes from low to high

## Proportional Symbols

Symbol size represents magnitude of values.

1. **Properties → Symbology**
2. Select **"Graduated"**
3. **Value**: Numeric attribute
4. **Method**: Change to **"Size"**
5. Set **Size**: Min and Max point sizes
6. Click **Classify**
7. Adjust as needed

**Example**: Circle size proportional to city population

## Adding Labels

1. **Properties → Labels**
2. Change dropdown to **"Single Labels"**
3. **Value**: Select attribute to display
4. Adjust:
   - **Text**: Font, size, color
   - **Formatting**: Number format, text case
   - **Buffer**: Background for readability
   - **Placement**: Position relative to features
5. Click **OK**

## Color Ramps

### Choosing Colors
- **Sequential**: Light to dark (single hue) for ordered data
- **Diverging**: Two colors from center for data with meaningful middle
- **Qualitative**: Distinct colors for categories

### Creating Custom Color Ramp
1. In color ramp dropdown, click **"Create New Color Ramp"**
2. Choose **"Gradient"** or **"Catalog"**
3. Set colors for endpoints
4. Name and save

## Creating a Legend

For print layouts:

1. **Project → New Print Layout**
2. Name your layout, click **OK**
3. **Add Item → Add Map** (draw rectangle on canvas)
4. **Add Item → Add Legend**
5. In **Item Properties**:
   - Remove unwanted layers
   - Adjust fonts and spacing
   - Resize as needed

## Example Workflow: Population Density Map
