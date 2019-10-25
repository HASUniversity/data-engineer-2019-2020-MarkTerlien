# Make list
my_list = []

# Add element to list
print('Add element to list')
print('-------------------------------')
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
print('-------------------------------')

# Print list
print('Print list')
print('-------------------------------')
print(my_list)
print('-------------------------------')

# Iterate over list
print('Iterate over list')
print('-------------------------------')
for item in my_list:
    print(item)
print('-------------------------------')

# Select single item by index
print('Select single item by index')
print('-------------------------------')
print(my_list[2])
print('-------------------------------')

# Make dictionary
my_dict ={}

# Add element to dictionary
print('Add element to dictionary')
print('-------------------------------')
my_dict["one"] = 1
my_dict["two"] = 2
my_dict["three"] = 3
print('-------------------------------')

# Print dictionary
print('Print dictionary')
print('-------------------------------')
print(my_dict)
print('-------------------------------')

# Iterate over dict
print('Iterate over dict')
print('-------------------------------')
for key in my_dict:
    print(key)
    print(my_dict[key])
print('-------------------------------')
    
# Select single item by key
print('Select single item by key')
print('-------------------------------')
print(my_dict['two'])
print('-------------------------------')
