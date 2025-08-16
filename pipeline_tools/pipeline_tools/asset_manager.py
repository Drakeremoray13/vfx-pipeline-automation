import os
import shutil

def organize_assets(asset_root):
    """
    Organize VFX assets into standardized folder structure
    """
    print(f"Organizing assets in {asset_root}")
    
    # Standard VFX folder structure
    folders = ["footage", "renders", "plates", "elements", "scripts", "textures"]
    
    for folder in folders:
        path = os.path.join(asset_root, folder)
        if not os.path.exists(path):
            os.makedirs(path)
            print(f"Created folder: {path}")

def move_assets_by_type(source_dir, target_dir):
    """
    Move assets to appropriate folders based on file type
    """
    file_types = {
        '.nk': 'scripts',
        '.exr': 'renders',
        '.mov': 'footage',
        '.jpg': 'plates',
        '.png': 'elements'
    }
    
    for filename in os.listdir(source_dir):
        file_ext = os.path.splitext(filename)[1].lower()
        if file_ext in file_types:
            target_folder = os.path.join(target_dir, file_types[file_ext])
            if not os.path.exists(target_folder):
                os.makedirs(target_folder)
            
            source_path = os.path.join(source_dir, filename)
            target_path = os.path.join(target_folder, filename)
            shutil.move(source_path, target_path)
            print(f"Moved {filename} to {file_types[file_ext]}")

if __name__ == "__main__":
    organize_assets("path_to_assets")
