world_map = {
    'CONSTRUCTIONSITE': {
        'NAME': "Contruction Site",
        'DESCRIPTION': "Nothing special, however you have a bad feeling about your house.",
        'PATHS': {
            'EAST': 'JOB',
            'SOUTH': 'HOME'
        }
    },
    'HOME': {
        'NAME': "Home",
        'DESCRIPTION': "The bad feeling was that it was ransacked! Nothing of value was left behind, you decided to go"
                       "on a treasure hunt to recover your valuable's.",
        'PATHS': {
            'WEST': 'GARAGE',
            'SOUTH':'LIVINGROOM',
            'NORTH':'CONSTRUCTIONSITE'
        }

    },
    'LIVINGROOM': {
        'NAME': 'Living Room',
        'DESCRIPTION': "The best part of the day ruined, now a a effort must be made.",
        'PATHS': {
            'NORTH': "HOME",
            'WEST': "KITCHEN"
        }
    },
    'JOB': {
        'NAME': 'Job',
        'DESCRIPTION': "Where you spend most of your hours.",
        'PATHS': {
            'SOUTH': "INTOWN",
            'WEST': "CONSTRUCTIONSITE"
        }
    },
    'FREEWAY': {
        'NAME': 'Freeway',
        'DESCRIPTION': "Worst Part of the day.",
        'PATHS': {
            'NORTH': "INTOWN",
            'EAST': "HOME",
            'WEST': "AIRPORT"
        }
    },
    'AIRPORT': {
     'NAME': 'Airport',
        'DESCRIPTION': "It's time to go and get rich quick or die trying.",
        'PATHS': {
        'EAST': "EGYPT",
        'NORTH': "INTOWN",
        'SOUTH': "MEXICO",
        'WEST': 'JAPAN'
        }
    },
    'INTOWN': {
    'NAME': 'In Town',
        'DESCRIPTION': "Need to get equiped before the adventure.",
        'PATHS': {
        'SOUTH': "FREEWAY",
        'NORTH': "JOB"
        }
    },
    'CAIRO': {
    'NAME': 'Cairo',
    'DESCRIPTION' : "Nearing the end of the adventure, Giza is nearby.",
    'PATHS': {
        'EAST': 'NILERIVER',
        'WEST': 'HOTEL-STEIGINBERGER',
        'NORTH': 'EGYPTIAN-MUSEUM'
        }
    },
    'KITCHEN': {
    'NAME': 'Kitchen',
    'DESCRIPTION': "Nothing out the ordinary. You need food for you're adventure after all, can't really on fast food.",
    'PATHS': {
        'EAST': 'LIVINGROOM'
         }
    },
    'PLAYGROUND': {
    'NAME': 'Playgroud',
    'DESCRIPTION': "Don't stick around for too long. The map says that a piece of the puzzle is somewhere around here.",
    'PATHS': {
        'NORTH': 'FREEWAY',
        'SOUTH': 'ABANDONED_PARK_ENTRANCE'
         }
    },
    'GARAGE': {
    'NAME': 'GARAGE',
    'DESCRIPTION': "You don't use your car since this is dream car that you saved up on.",
    'PATHS': {
        'WEST': 'HOME',
        'EAST': 'FREEWAY'
         }
    },
    'ABANDONDED_PARK_ENTRANCE': {
    'NAME': 'ABANDONED_PARK_ENTRANCE',
    'DESCRIPTION': "You may run into some wild animals here. You may have to fight.",
    'PATHS': {
        'NORTH': 'PLAYGROUND',
        'SOUTH': 'ABANDONED_PARK'
         }
    },
    'ABANDONED_PARK': {
    'NAME': 'ABANDONED_PARK',
    'DESCRIPTION': "The X on the map is closer.",
    'PATHS': {
        'NORTH': 'ABANDONED_PARK_ENTRANCE',
        'SOUTH': 'FOREST'
         }
    },

    'FOREST': {
    'NAME': 'FOREST',
    'DESCRIPTION': "There's a shrine nearby, the X's is directly on it.",
    'PATHS': {
        'NORTH': 'ABANDONED_PARK',
        'WEST': 'SHRINE'
        }
    },
    'SHRINE': {
    'NAME': 'SHRINE',
    'DESCRIPTION': "There's a shovel near an old shrine. ",
    'PATHS': {
        'EAST': 'FOREST'
        }
    },
    'STORE': {
    'NAME': 'STORE',
    'DESCRIPTION': "An shop for adventurers. The items will get better as the game progess.",
    'PATHS': {
        'WEST': 'INTOWN'
        }
    },
}
current_node = world_map['CONSTRUCTIONSITE']
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