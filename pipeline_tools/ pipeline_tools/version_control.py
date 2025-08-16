import os
import datetime

def manage_versions(render_dir):
    """
    Manage render output versions and track changes
    """
    versions = [f for f in os.listdir(render_dir) if os.path.isfile(os.path.join(render_dir, f))]
    print(f"Found {len(versions)} versions in {render_dir}")
    
    # Sort versions by modification time
    version_info = []
    for version in versions:
        path = os.path.join(render_dir, version)
        mod_time = os.path.getmtime(path)
        version_info.append((version, mod_time))
    
    version_info.sort(key=lambda x: x[1], reverse=True)
    
    print("Recent versions:")
    for version, mod_time in version_info[:5]:
        date_str = datetime.datetime.fromtimestamp(mod_time).strftime('%Y-%m-%d %H:%M:%S')
        print(f"  {version} - {date_str}")

def create_version_backup(file_path):
    """
    Create versioned backup of a file
    """
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    filename, ext = os.path.splitext(file_path)
    backup_path = f"{filename}_v{timestamp}{ext}"
    
    with open(file_path, 'rb') as source, open(backup_path, 'wb') as backup:
        backup.write(source.read())
    
    print(f"Created backup: {backup_path}")

if __name__ == "__main__":
    manage_versions("path_to_renders")
