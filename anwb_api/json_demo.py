# Import libraries
import requests
import json

# HTTP headers
headers = {
    'Accept': 'application/json',
}

# Build URL
url = 'https://www.anwb.nl/feeds/gethf'

# Execute HTTP request
response = requests.get(url, headers=headers)

# Get result
if response.status_code == 200 :
    print ('Request OK')
    result = response.json()
    print(result['dateTime'])
    for road in result['roadEntries'] :
        print(road['road'])
        print(road['roadType'])
        for trafficJam in road['events']['trafficJams'] :
            print(trafficJam['from'])
            print(trafficJam['fromLoc']['lat'])
            print(trafficJam['fromLoc']['lon'])
            print(trafficJam['to'])
            print(trafficJam['toLoc']['lat'])
            print(trafficJam['toLoc']['lon'])
            try:
                print(trafficJam['distance'])
            except:
                None
        for roadWork in road['events']['roadWorks'] :
            print(roadWork['from'])
            print(roadWork['fromLoc']['lat'])
            print(roadWork['fromLoc']['lon'])
            print(roadWork['to'])
            print(roadWork['toLoc']['lat'])
            print(roadWork['toLoc']['lon'])

    #print(json.dumps(response.json(), indent=8, sort_keys=True))
else :
    print ('Request failed with :' + str(response.status_code))