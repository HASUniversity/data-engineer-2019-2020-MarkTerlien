# Import libraries
import requests
import json

# HTTP headers
headerss = {
    'Accept': 'application/json',
    'token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3N1ZWR0byI6Im0udGVybGllbkBoYXMubmwiLCJyZXNvdXJjZSI6WyIqIl0sImlhdCI6MTU3MDA4MzQ5Nn0.Tjx5Oon053nujYHWYcfrw4MqgF7eetuKE8EGCKy4CL8', 
}

# Build URL
url = 'https://agrodatacube.wur.nl/api/v2/rest/meteodata?output_epsg=28992&meteostation=251&fromdate=20150101&todate=20150121&page_size=25&page_offset=0'

# Execute HTTP request
response = requests.get(url, headers=headerss)

# TO DO: Open database connection

# Get result
if response.status_code == 200 :
    print ('Request OK')
    #print(json.dumps(response.json(), indent=8, sort_keys=True))
    for feature in response.json()['features'] :
        for key in feature['properties'] :
            # Get attributes datum and mean temperature
            if key == 'datum' :
                datum = key['datum']
            # TO DO: Get mean temperature
            # TO DO: Build and execute SQL INSERT statement nto table observations
else :
    print ('Request failed with :' + str(response.status_code))

# TO DO: Commit and close database connection



    
