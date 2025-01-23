import rhinoscriptsyntax as rs
import random

def random_color():
    """Generate a random RGB color."""
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def organize_selected_objects_by_prefix():
    # Get selected objects in the scene
    objects = rs.SelectedObjects()
    if not objects:
        print("No objects selected! Please select objects and try again.")
        return
    
    for obj in objects:
        # Get the name of the object
        obj_name = rs.ObjectName(obj)
        if not obj_name:
            print("Object {} has no name, skipping.".format(obj))
            continue
        
        # Extract the prefix (everything up to the word 'Object', excluding the suffix)
        if "Object" in obj_name:
            prefix = obj_name.split("_Object")[0]
        else:
            print("Object {} does not contain 'Object' in its name, skipping.".format(obj))
            continue
        
        # Check if the layer with the prefix name exists, if not, create it
        if not rs.IsLayer(prefix):
            rs.AddLayer(prefix)  # Create the new layer
            layer_color = random_color()  # Generate a random color
            rs.LayerColor(prefix, layer_color)  # Set the layer color
            print("Created new layer: {} with color: {}".format(prefix, layer_color))
        
        # Assign the object to the corresponding layer
        rs.ObjectLayer(obj, prefix)
    
    print("Selected objects have been organized into layers based on their prefixes!")

# Run the script
organize_selected_objects_by_prefix()