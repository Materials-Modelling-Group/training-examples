# QGIS Examples

Examples and workflows for QGIS on KENET HPC Remote Desktop.

## About QGIS

QGIS is a free and open-source Geographic Information System (GIS) for creating, editing, visualizing, analyzing, and publishing geospatial data.

## Directory Structure

- `examples/` - Step-by-step guides for common QGIS tasks
- `workflows/` - Complete analysis workflows for real-world scenarios
- `sample_data/` - Information about sample datasets (not included)

## Requirements

- QGIS 3.x
- Remote Desktop session from Open OnDemand
- Spatial data in standard formats (Shapefile, GeoJSON, GeoTIFF, etc.)

## Getting Started

1. Launch Remote Desktop from Open OnDemand
2. Open QGIS from Applications menu
3. Follow examples in order to learn basic operations
4. Try workflows for complete analysis scenarios

## Common File Formats

- **Vector**: Shapefile (.shp), GeoJSON (.geojson), GeoPackage (.gpkg)
- **Raster**: GeoTIFF (.tif), IMG, HDF
- **Tabular**: CSV with coordinates, Excel with location data

## Coordinate Systems

Common CRS for Kenya and East Africa:
- **WGS84 (EPSG:4326)**: Geographic, lat/lon, good for GPS data
- **UTM Zone 36S (EPSG:32736)**: Projected, good for Kenya
- **UTM Zone 37S (EPSG:32737)**: Projected, good for eastern Kenya
- **Arc 1960 (EPSG:4210)**: Traditional reference for East Africa

## Resources

- QGIS Documentation: https://docs.qgis.org/
- QGIS Training Manual: https://docs.qgis.org/latest/en/docs/training_manual/
- Sample data: Natural Earth (https://www.naturalearthdata.com/)
