import os
import json

def get_json_sizes(directory):
    total_sizes = {}
    
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            filepath = os.path.join(directory, filename)
            try:
                with open(filepath, 'r') as f:
                    # Get the file size in bytes
                    file_size = os.path.getsize(filepath)
                    # Load JSON to verify it's valid
                    json.load(f)
                    # Store both size and directory
                    total_sizes[filename] = (file_size, directory)
            except json.JSONDecodeError:
                print(f"Error: {filename} is not a valid JSON file")
            except Exception as e:
                print(f"Error processing {filename}: {str(e)}")
    
    return total_sizes

def main():
    directories = ["knowledge/set2/", "knowledge/set3/"]
    sizes = {}
    
    for directory in directories:
        sizes.update(get_json_sizes(directory))
    
    if sizes:
        print("\nJSON file sizes:")
        print("-" * 60)
        # Sort by size in descending order
        for filename, (size, directory) in sorted(sizes.items(), key=lambda x: x[1][0], reverse=True):
            dir_name = directory.split('/')[-2]  # Extract set2 or set3
            print(f"{filename} ({dir_name}): {size:,} bytes")
    else:
        print("No JSON files found in the specified directories")

if __name__ == "__main__":
    main()
