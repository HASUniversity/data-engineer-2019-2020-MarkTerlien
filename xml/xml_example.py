from xml.dom import minidom

# Build DOM
doc = minidom.parse("xml_tim_small.xml")

# Get list op operations
operations = doc.getElementsByTagName("operation")

# Iterate over operations and process each operation 
for operation in operations:
    
    # operationId
    operationId = operation.getElementsByTagName("operationId")[0]
    print(operationId.firstChild.data)
    
    # code
    code = operation.getElementsByTagName("code")[0]
    print('Code: ' + code.firstChild.data)
    code = operation.getElementsByTagName("code")[1]
    print('Code: ' + code.firstChild.data)
    
    # asset/device/code
    deviceCode = operation.getElementsByTagName("asset")[0].getElementsByTagName("device")[0].getElementsByTagName("code")[0]
    print(deviceCode.firstChild.data)

    # timestamp
    timeStamp = operation.getElementsByTagName("timestamp")[0]
    print(timeStamp.firstChild.data)

    # lattitude and longitude
    latitude = operation.getElementsByTagName("latitude")[0]
    longitude = operation.getElementsByTagName("longitude")[0]
    print(latitude.firstChild.data)
    print(latitude.firstChild.data)

    # speed
    speed = operation.getElementsByTagName("speed")[0]
    print(speed.firstChild.data)



