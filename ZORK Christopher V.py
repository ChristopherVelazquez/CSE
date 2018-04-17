world_map = {
    'WESTHOUSE': {
        'NAME': "West of house",
        'DESCRIPTION': "You are west of house.",
        'PATHS': {
            'NORTH': 'NORTHHOUSE',
            'SOUTH': 'SOUTHHOUSE'
        }
    },
    'NORTHHOUSE': {
        'NAME': "Home",
        'DESCRIPTION': "Insert Description here",
        'PATHS': {
            'WEST': 'WESTHOUSE',
            'SOUTH':'SOUTHHOUSE'
        }

    },
    'SOUTHHOUSE': {
        'NAME': 'South of House',
        'DESCRIPTION': "Insert Description Here",
        'PATHS': {
            'NORTH': "WESTHOUSE"
        }
    }
}

current_node = world_map['WESTHOUSE']
print(current_node)
directions = ['NORTH', 'SOUTH', 'EAST', 'WEST']


while True:
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])
    command = input('>_')
    if command == 'quit':
        quit(0)
    if command in directions:
        try:
            name_of_node = current_node['PATHS'][command]
            current_node = world_map[name_of_node]
        except:
            print("You cannot go this way")

    else:
        print('Command not recognized')