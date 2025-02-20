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
                    total_sizes[filename] = file_size
            except json.JSONDecodeError:
                print(f"Error: {filename} is not a valid JSON file")
            except Exception as e:
                print(f"Error processing {filename}: {str(e)}")
    
    return total_sizes

def main():
    directory = "knowledge/set2/"
    sizes = get_json_sizes(directory)
    
    if sizes:
        print("\nJSON file sizes in knowledge/set2/:")
        print("-" * 40)
        for filename, size in sorted(sizes.items()):
            print(f"{filename}: {size:,} bytes")
    else:
        print("No JSON files found in the specified directory")

if __name__ == "__main__":
    main()
