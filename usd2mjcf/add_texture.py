import os
import glob
import xml.etree.ElementTree as ET
import shutil

def add_texture_to_xml():
    # Define paths
    material_dir = "/home/ps/BEHAVIOR-1K/OmniGibson/omnigibson/data/og_dataset/objects/bottle_of_gin/qzgcdx/material/"
    xml_file = "/home/ps/BEHAVIOR-1K/OmniGibson/omnigibson/data/og_dataset/objects/bottle_of_gin/qzgcdx/usd/MJCF/try.xml"
    visuals_dir = "/home/ps/BEHAVIOR-1K/OmniGibson/omnigibson/data/og_dataset/objects/bottle_of_gin/qzgcdx/usd/MJCF/visuals/"
    
    # Create visuals directory if it doesn't exist
    os.makedirs(visuals_dir, exist_ok=True)
    
    # Find all PNG files in material directory
    png_files = glob.glob(os.path.join(material_dir, "*.png"))
    
    if not png_files:
        print("No PNG files found in the material directory")
        return
    
    # Use the first PNG file found
    texture_file = png_files[0]
    texture_filename = os.path.basename(texture_file)
    
    # Copy texture file to visuals directory
    destination_file = os.path.join(visuals_dir, texture_filename)
    shutil.copy2(texture_file, destination_file)
    print(f"Copied texture file to: {destination_file}")
    
    # Parse XML file
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    # Find the material element and its parent
    material_elem = None
    material_parent = None
    
    # Search through all elements to find the material and its parent
    for parent in root.iter():
        for child in parent:
            if child.tag == "material" and child.get("name") == "OmniGlass":
                material_elem = child
                material_parent = parent
                break
        if material_elem is not None:
            break
    
    if material_elem is None:
        print("Material 'OmniGlass' not found in XML file")
        return
    
    # Create texture element
    texture_name = "ceramic"
    texture_elem = ET.Element("texture")
    texture_elem.set("file", f"visuals/{texture_filename}")
    texture_elem.set("name", texture_name)
    
    # Insert texture element before material element
    index = list(material_parent).index(material_elem)
    material_parent.insert(index, texture_elem)
    
    # Add texture attribute to material element
    material_elem.set("texture", texture_name)
    
    # Save the modified XML
    tree.write(xml_file, encoding="utf-8", xml_declaration=True)
    print(f"Successfully updated XML file: {xml_file}")
    
    print(f"Added texture: {texture_filename}")
    print(f"Texture reference: visuals/{texture_filename}")

if __name__ == "__main__":
    add_texture_to_xml()
