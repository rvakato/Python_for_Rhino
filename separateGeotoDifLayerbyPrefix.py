import rhinoscriptsyntax as rs

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
            rs.AddLayer(prefix)
            print("Created new layer: {}".format(prefix))
        
        # Assign the object to the corresponding layer
        rs.ObjectLayer(obj, prefix)
    
    print("Objects have been organized into layers based on their prefixes!")

# Run the script
organize_objects_by_prefix()