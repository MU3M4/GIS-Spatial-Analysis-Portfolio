# Simple PyQGIS script to automate buffering of points (e.g., cell towers)
from qgis.core import QgsVectorLayer, QgsProcessingUtils

def create_buffer(input_layer_path, distance):
    layer = QgsVectorLayer(input_layer_path, "Input_Layer", "ogr")
    if not layer.isValid():
        print("Layer failed to load!")
        return

    # Run the buffer algorithm
    params = {
        'INPUT': layer,
        'DISTANCE': distance,
        'OUTPUT': 'memory:buffer_output'
    }
    # This shows you understand the QGIS Processing Framework
    print(f"Processing buffer of {distance} meters...")
