import os
import shutil

def organize_files():
    # Set paths
    knowledge_dir = "knowledge"
    set1_dir = os.path.join(knowledge_dir, "set1")
    set2_dir = os.path.join(knowledge_dir, "set2")

    # Create directories if they don't exist
    os.makedirs(set1_dir, exist_ok=True)
    os.makedirs(set2_dir, exist_ok=True)

    # Get all files in knowledge directory
    for filename in os.listdir(knowledge_dir):
        # Skip directories
        if os.path.isdir(os.path.join(knowledge_dir, filename)):
            continue
            
        # Skip if file is already in set1 or set2
        if filename.startswith("set1") or filename.startswith("set2"):
            continue

        # Determine target directory based on first character
        if filename[0].isupper():
            target_dir = set2_dir
        else:
            target_dir = set1_dir

        # Move the file
        source = os.path.join(knowledge_dir, filename)
        destination = os.path.join(target_dir, filename)
        shutil.move(source, destination)

if __name__ == "__main__":
    organize_files()
