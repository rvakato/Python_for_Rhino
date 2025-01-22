import rhinoscriptsyntax as rs
import random

def move_objects_to_layers():
    # Get all selected objects in the scene
    objects = rs.SelectedObjects()
    if not objects:
        print("No selected objects found in the scene.")
        return

    for obj in objects:
        # Get the name of the object
        obj_name = rs.ObjectName(obj)
        if not obj_name:
            continue

        # Extract the prefix of the name up to the first hyphen (-)
        prefix = obj_name.split("[")[0].strip()

        # Check if the prefix is valid
        if prefix:
            # Create a layer name based on the prefix
            layer_name = prefix
            
            # If the layer does not exist, create it
            if not rs.IsLayer(layer_name):
                rs.AddLayer(layer_name)

            # Move the object to the corresponding layer
            rs.ObjectLayer(obj, layer_name)

    print("Selected objects have been moved to corresponding layers.")

def change_layer_colors_randomly():
    # Get all layers in the document
    layers = rs.LayerNames()
    if not layers:
        print("No layers found in the document.")
        return

    for layer in layers:
        # Generate a random color
        random_color = rs.CreateColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        # Change the layer color
        rs.LayerColor(layer, random_color)

    print("Layer colors have been changed randomly.")

# Execute the functions
move_objects_to_layers()
change_layer_colors_randomly()