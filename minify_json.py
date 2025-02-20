import json
import os

def minify_json_files(directory):
    # Ensure the directory exists
    if not os.path.exists(directory):
        print(f"Directory {directory} does not exist!")
        return

    # Get all .json files in the directory
    json_files = [f for f in os.listdir(directory) if f.endswith('.json')]
    
    for filename in json_files:
        file_path = os.path.join(directory, filename)
        try:
            # Read the JSON file
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # Write back the minified JSON
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, separators=(',', ':'))
            
            print(f"Successfully minified: {filename}")
            
        except json.JSONDecodeError as e:
            print(f"Error processing {filename}: Invalid JSON - {str(e)}")
        except Exception as e:
            print(f"Error processing {filename}: {str(e)}")

if __name__ == '__main__':
    knowledge_dir = 'knowledge'
    print(f"Starting JSON minification in {knowledge_dir}/...")
    minify_json_files(knowledge_dir)
    print("Minification complete!")
