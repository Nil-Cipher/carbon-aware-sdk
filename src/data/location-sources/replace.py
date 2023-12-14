import json

# Your JSON data
json_file_path = "gke-regions.json"

with open(json_file_path, "r") as json_file:
    data = json.load(json_file)

# Iterate through each key in the JSON and update the "Name" field
for key in data:
    data[key]["Name"] = key

# Specify the file path to save the updated JSON data
output_file_path = 'output.json'

# Save the updated JSON data to the specified file
with open(output_file_path, 'w') as output_file:
    json.dump(data, output_file, indent=4)

print(f'Updated JSON data has been saved to {output_file_path}')
