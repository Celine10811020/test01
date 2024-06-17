import os
import sys
import json
import re

# Define the path to the hoho folder and JSON file
hoho3_path = 'hoho'
json_file_path = 'hoho.json'

# Get the list of changed files from the command line argument
with open(sys.argv[1], 'r', encoding='utf-8') as f:
    changed_files = [line.strip().strip('"').decode() for line in f]

print("Changed files:", changed_files)  # 输出更改的文件以供调试

# Initialize an empty list to hold the JSON data
json_data = []

# Load the existing JSON data if the file exists
if os.path.exists(json_file_path):
    with open(json_file_path, 'r', encoding='utf-8') as json_file:
        json_data = json.load(json_file)

# Define regex patterns for each filename format
patterns = [
    r'診所(\d{8})\.jpg',
    r'診所(\d{8})-(\d{4})\.jpg',
    r'診所(\d{8})-(\d{8})\.jpg'
]

# Function to parse the filename and extract dates
def parse_filename(file_name):
    for pattern in patterns:
        match = re.match(pattern, file_name)
        if match:
            if len(match.groups()) == 1:
                start_date = match.group(1)
                end_date = start_date
            elif len(match.groups()) == 2:
                start_date = match.group(1)
                if len(match.group(2)) == 4:
                    end_date = start_date[:4] + match.group(2)
                else:
                    end_date = match.group(2)
            return start_date, end_date
    return None, None

# Iterate over the changed files and extract the necessary information
for file_name in changed_files:
    path = os.path.join(hoho3_path, os.path.basename(file_name))
    start_date, end_date = parse_filename(os.path.basename(file_name))

    if start_date and end_date:
        # Create a dictionary with the extracted data
        file_data = {
            'path': path,
            'start': start_date,
            'end': end_date
        }
        # Append the dictionary to the JSON data list
        json_data.append(file_data)

# Write the JSON data to the file
with open(json_file_path, 'w', encoding='utf-8') as json_file:
    json.dump(json_data, json_file, ensure_ascii=False, indent=2)

print(f'Updated {json_file_path} with {len(json_data)} entries.')
