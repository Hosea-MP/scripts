import os
import shutil

def move_files():
    source_dir = "knowledge/set2"
    target_dir = "knowledge/set3"
    
    # Ensure target directory exists
    os.makedirs(target_dir, exist_ok=True)
    
    # List of files to move with their expected sizes
    files_to_move = {
        "Jakes AIO Fletcher v141 by Jacob192.json": 287125,
        "AIORooftops by xRyan.json": 181957,
        "AIORooftops by 86015866.json": 178493,
        "Boots F2P Skiller by oldboot.json": 137334,
        "Lava Dragons by Andre Hazes.json": 124043,
        "GOTR by Andre Hazes.json": 104447,
        "VarrockMuseumMiniquest by Penguin123.json": 98999,
        "Daddys Home Miniquest by Sabertooth.json": 73980,
        "KiwiBuilder - Quest - The Corsair Curse by Kiwiszn.json": 67804
    }
    
    for filename, expected_size in files_to_move.items():
        source_path = os.path.join(source_dir, filename)
        target_path = os.path.join(target_dir, filename)
        
        if not os.path.exists(source_path):
            print(f"Error: Source file not found: {filename}")
            continue
            
        # Verify file size before moving
        actual_size = os.path.getsize(source_path)
        if actual_size != expected_size:
            print(f"Warning: Size mismatch for {filename}")
            print(f"Expected: {expected_size:,} bytes")
            print(f"Actual: {actual_size:,} bytes")
            continue
            
        try:
            shutil.move(source_path, target_path)
            print(f"Moved: {filename}")
        except Exception as e:
            print(f"Error moving {filename}: {str(e)}")

if __name__ == "__main__":
    move_files()
