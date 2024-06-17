import os
import json
import re
import sys

# Function to parse the filename and extract start and end dates
def parse_filename(file_name):
    pattern = r'^診所(\d{8})(?:-(\d{8}|\d{4}-\d{4}))?\.jpg$'
    match = re.match(pattern, file_name)
    if match:
        start_date = match.group(1)
        if match.group(2):
            if '-' in match.group(2):
                end_date = match.group(2).replace('-', '')
            else:
                end_date = match.group(1) + match.group(2)
        else:
            end_date = None
        return start_date, end_date
    else:
        return None, None

# Define the path to the hoho folder and JSON file
hoho_path = 'hoho'
json_file_path = 'hoho.json'

# Read changed files from input file
changed_files_txt = sys.argv[1]
with open(changed_files_txt, 'r', encoding='utf-8') as f:
    changed_files = f.read().splitlines()

# Initialize an empty list to hold the JSON data
json_data = []

# Iterate over the changed files and extract the necessary information
for file_name in changed_files:
    path = os.path.join(hoho_path, file_name)
    start_date, end_date = parse_filename(file_name)

    if start_date:
        # Create a dictionary with the extracted data
        file_data = {
            'path': path,
            'start': start_date,
            'end': end_date
        }

        # Append the dictionary to the JSON data list
        json_data.append(file_data)
    else:
        print(f"Skipping {file_name} as it does not match expected format.")

# Write the JSON data to the file
with open(json_file_path, 'w', encoding='utf-8') as json_file:
    json.dump(json_data, json_file, ensure_ascii=False, indent=2)

print(f'Updated {json_file_path} with {len(json_data)} entries.')
