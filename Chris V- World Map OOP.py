class Room(object):
    def __init__(self, name, east, south, north, west, desc):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.description = desc

    def move(self,direction):
        global current_node
        current_node = globals()[getattr(self,direction)]


# Initialize Rooms
ConstructionSite = Room("Construction Site", 'Job', 'Home', None, None,
                        "It's just a building in contruction however something catches your eye with a shine. "
                        "You can go east or south.")
HomeEntrance = Room("Home-Entrance", 'Garage', 'Living Room', 'Construction Site', None,
                "Home sweet Home except that your house been ruined! The thieves left a treasure map you found a "
                "while back,they thought it was fake probably, "
                "your only hope is to find treausre fast. You can go east, south, and north.")
HomeLivingRoom = Room("Home-Living Room", 'Home', 'Kitchen', None, None,
                   "The best part of the day ruined. You can go North or West.")
Job = Room("Job", None, 'In_Town', None, 'Construction Site'
           "Where you spend most of your day. You don't really hate it. Just no one to talk to. "
            "You can go west or south.")
Kitchen = Room("Kitchen", 'Home-Living Room', None, None, None,
               "Nothing usual here, get your food before your adventure, can't rely on fast food. You can go east.")
Freeway = Room("Freeway", 'Garage', 'Playground', None, 'Intown'
               "Not much traffic today. You can go West, South or East")
Playground = Room("Playground", None, 'Park', 'Freeway', None,
                  "Don't stay here for to long, the map has a X somewhere around here. You can go south or north.")
InTown = Room("In Town", 'Store', 'Airport', 'Job', 'Freeway'
              "Busy as ever, the town leads to mutiple directions. You can go North, East, South or West.")
Garage = Room("Garage",'Intown', None ,None, 'HomeEntrance'
              "You only use your car for buniess trips so you mainly walk. You can go east or west.")
Store = Room("Store", None, None, None, 'Intown'
             "A store where you can but items. You can go west.")
AbandonedPark_Entrance = Room("Abandonded Entrance-Front", None, 'Forest', 'Playground', None,
            "It is closed off to the public since wild animals live here. It is also very huge. "
            "Get ready to protect yourself. You can go North or South.")
AbandonedPark = Room("Abandoned Park", None, 'Forest' , 'AbandonedPark_Entrance' , None,
                     "You have a chance of running into enemies. Stay on guard. You can go south or north.")
Forest = Room("Forest", None, None, None, "Shrine",
              "The X on the map is just west of here.")
Shrine = Room("Shrine", 'Forest', None, None, None,
              "There's a shovel near the old shrine. You can go east.")
Airport = Room("Airport", 'Egypt', 'Mexico', 'In town', 'Japan',
               "Depending on which one you choose, the difficulty may change, choose north to back.")








current_node = ConstructionSite
directions = ['north', 'south', 'east', 'west']
short_direction = {'n', 's', 'e', 'w'}

while True:
    print(current_node['name'])
    print(current_node['description'])
    command = input('>_').lower()
    if command == 'quit':
        quit(0)
    elif command in short_direction:
    # look for which command we typed in
        pos = short_direction.index(command)
        #
        command = directions[pos]

    if command in directions:
        try:
            name_of_node = current_node['PATHS'][command]
            current_node = [name_of_node]
        except KeyError:
            print('Command not recongized')
            print()

