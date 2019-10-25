import json

# Open file
json_file = open('features.json')
data = json.load(json_file)

# Show keys
for key in data :
    print(key)
    
# Show type
print(data['type'])

# Iterate over features
for feature in data['features'] :
    print(feature['geometry'])
    print(feature['properties']['mean_temperature'])