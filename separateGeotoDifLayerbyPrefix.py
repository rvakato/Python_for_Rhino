import rhinoscriptsyntax as rs
import random

def random_color():
    """Generate a random RGB color."""
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def organize_objects_by_prefix():
    # Get all objects in the scene
    objects = rs.AllObjects()
    if not objects:
        print("No objects found in the scene!")
        return
    
    for obj in objects:
        # Get the name of the object
        obj_name = rs.ObjectName(obj)
        if not obj_name:
            print("Object {} has no name, skipping.".format(obj))
            continue
        
        # Extract the prefix from the object name (split by '_' or '.')
        prefix = obj_name.split('_')[0]
        
        # Check if the layer with the prefix name exists, if not, create it
        if not rs.IsLayer(prefix):
            rs.AddLayer(prefix)  # Create the new layer
            print("Created new layer: {}".format(prefix))
        
        # Assign a random color to the layer, even if it already exists
        layer_color = random_color()  # Generate a random color
        rs.LayerColor(prefix, layer_color)  # Set the layer color
        print("Assigned random color {} to layer: {}".format(layer_color, prefix))
        
        # Assign the object to the corresponding layer
        rs.ObjectLayer(obj, prefix)
    
    print("Objects have been organized into layers based on their prefixes!")

# Run the script
organize_objects_by_prefix()