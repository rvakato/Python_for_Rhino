import rhinoscriptsyntax as rs
import System.Drawing.Color as Color

# List of layer names with corresponding colors
layers_with_colors = [
    {"name": "3D - OriginalModel", "color": Color.Black},
    {"name": "3D - MATERIAL_NOT_DEFINED", "color": Color.Gray},
    {"name": "3D - Insulated_back_panel", "color": Color.White},
    {"name": "3D - FOR_Precast_Type_3", "color": Color.Green},
    {"name": "3D - FOR_Precast_Type_1", "color": Color.Blue},
    {"name": "3D - FOR_OVC_Dark_Grey", "color": Color.DarkGray},
    {"name": "3D - FOR_OVC_Dark_Grey_Metal", "color": Color.DarkSlateGray},
    {"name": "3D - FOR_Mineral_Wool", "color": Color.Purple},
    {"name": "3D - FOR_Glass", "color": Color.LightBlue},
    {"name": "3D - FOR_Blockwork", "color": Color.Brown},
    {"name": "3D - FOR_Aluminium_Type_1", "color": Color.Orange},
    {"name": "3D - Aluminium_Bronze", "color": Color.Goldenrod},
    {"name": "3D - FOR_Precast_Type_2", "color": Color.Magenta},
    {"name": "3D - Balcony_Deck", "color": Color.Turquoise},
    {"name": "3D - AEC_Concept_-_White", "color": Color.White},
    {"name": "3D - FOR_CavityCloser", "color": Color.DarkOliveGreen},
    {"name": "3D - Roofing_-_AVCL", "color": Color.LightGray},
    {"name": "3D - Metal_-_Aluminum", "color": Color.Silver},
    {"name": "3D - Glass", "color": Color.Aqua},
    {"name": "3D - Aluminium_Bronze_Dark(1)", "color": Color.DarkGoldenrod}
]

# Function to create layers and assign colors
for layer in layers_with_colors:
    layer_name = layer["name"]
    layer_color = layer["color"]
    
    if not rs.IsLayer(layer_name):  # Check if the layer already exists
        rs.AddLayer(layer_name, color=layer_color)  # Create the layer with the color
        print("Layer '{}' created with color {}.".format(layer_name, layer_color))
    else:
        # Update the color if the layer already exists
        rs.LayerColor(layer_name, layer_color)
        print("Layer '{}' already exists. Color updated to {}.".format(layer_name, layer_color))