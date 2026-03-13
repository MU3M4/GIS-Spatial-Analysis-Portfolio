# GIS & Spatial Data Science Portfolio
**Focus:** Automated Spatial Analysis, Remote Sensing, and AI Data Preparation.

## Project 1: Automated Land Cover Classification (QGIS + Python)
**Objective:** To prepare high-quality training labels for an AI model identifying urban sprawl.
* **Tools:** QGIS, Semi-Automatic Classification Plugin (SCP), PyQGIS.
* **Workflow:** 1. Imported Sentinel-2 satellite imagery.
    2. Performed atmospheric correction and NDVI (Normalized Difference Vegetation Index) calculation.
    3. Used a Random Forest classifier to categorize land into: Urban, Water, Vegetation, and Bare Soil.
* **Outcome:** Generated a 10m resolution raster mask used for training a U-Net segmentation model.

## Project 2: Network Analysis for Urban Infrastructure
**Objective:** Optimizing logistics routes using OpenStreetMap (OSM) data.
* **Tools:** QGIS Network Analysis Toolset, GRASS GIS.
* **Workflow:** 1. Cleaned topology errors in road network layers.
    2. Calculated "Service Areas" based on 5, 10, and 15-minute drive times.
* **Visual:** [Link to Map in /output folder]

## Technical Skills
* **Software:** QGIS (Advanced), ArcGIS Pro, Google Earth Engine.
* **Programming:** Python (Pandas, GeoPandas, PyQGIS), SQL (PostGIS).
* **Data Formats:** GeoJSON, Shapefiles, Cloud Optimized GeoTIFF (COG), KML.
