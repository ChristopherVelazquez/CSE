class Item(object):
    def __init__(self, name):
        self.name = name

    def pick_up(self):
        print("You picked up %s" % self.name)

class Weapon(Item):
    def __init__(self, name, damage):
        super(Weapon, self).__init__(name)
        self.damage = damage

    def equip(self):
        print("You equip a %s" % Weapon)

class Healing(Item):
    def __init__(self, name, restoration, curing, buffs):
        super(Healing, self).__init__(name)
        self.restoration = restoration
        self.curing = curing
        self.buffs = buffs

    def heal(self):
        print("You start %s thanks to a potion" % Healing)

class Armor(Item):
    def __init__(self, name, defense, magic_defense):
        super(Armor, self).__init__(name)
        self.defense = defense
        self.magic_defense = magic_defense

    def equip(self):
         print("You have protection thanks to your %s" % Armor)


class Magic(Item):
    def __init__(self, name, magic_damage, close_range, far_range,):
        super(Magic, self).__init__(name)
        self.magic_damage = magic_damage
        self.close_range = close_range
        self.far_range = far_range

    def magic_attack(self_target):
        print("You attacked with %s" % Magic)

class Acessories(Item):
    def __init__(self, name):
        super(Acessories, self).__init__(name)

    def equip(self):
        print("You equipped %s" % Acessories)

class Amulet(Acessories):
    def __init__(self, name, magic_defense):
        super(Amulet, self).__init__(name)
        self.magic_defense = magic_defense

    def protection(self):
        print("You took less magic damage thanks to your %s" % Amulet)

class Shield(Acessories):
    def __init__(self, name, defense):
        super(Shield, self).__init__(name)
        self.defense = defense

    def protection(self):
        print("You took less damage thanks to your %s" % Shield)

class Hero_Medal(Acessories):
    def __init__(self, name, damage_up):
        super(Hero_Medal, self).__init__(name)
        self.damage_up = damage_up

    def buff(self):
        print("You feel more courages thanks to %s, Damage Up!" % Shield)


class Swift_Band(Acessories):
    def __init__(self, name, speed_up):
        super(Swift_Band, self).__init__(name)
        self.speed_up = speed_up

    def buff(self):
        print("You feel faster thanks to %s, Speed Up!" % Swift_Band)


class Bow(Weapon):
    def __init__(self, name, damage, ranged):
        super(Bow, self).__init__(name, damage)
        self.range = range

    def Attack (self_target):
        print("You attack from a distance with your %s." % Bow)

class Sword(Weapon):
    def __init__(self, name, damage, close_range, speed_up):
        super(Sword, self).__init__(name, damage)
        self.close_range = close_range
        self.speed_up = speed_up

    def Attack (self_target):
        print("You attack with your %s." % Sword)

class Lance(Weapon):
    def __init__(self, name, damage, close_range, defense_up):
        super(Lance, self).__init__(name, damage)
        self.close_range = close_range
        self.defense_up = defense_up

    def Attack (self_target):
        print("You attack with your %s." % Lance)

class Axe(Weapon):
    def __init__(self, name, damage, close_range, damage_up):
        super(Axe, self).__init__(name, damage)
        self.close_range = close_range
        self.defense = damage_up

    def Attack (self_target):
        print("You attack with your %s." % Axe)

class Magic_Robe(Armor):
    def __init__(self, defense, magic_defense, magic_up):
        super(Magic_Robe, self).__init__(defense, magic_defense)
        self.magic_up = magic_up

    def protection(self):
        print("You took less magic damage, and gained more magic thanks to your %s" % Magic_Robe)


class Character(object):
    def __init__(self, stats, health, description, name, attack, defense,speed, inventory, abilities):

        self.name = name
        self.stats = stats
        self.health = health
        self.description = description
        self.attack_amt = attack
        self.defense = defense
        self.inventory = inventory
        self.abilities = abilities
        self.speed = speed

    def attack(self, enemy):
        enemy.take_damage(self.attack_amt)

    def take_damage(self, dmg):
        total_damage = dmg - self.defense
        if total_damage < 0:
            total_damage = 0
        self.health -= total_damage
        if self.health <= 0:
            print("You died...")


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


L_Soldier = Character (89,30,"A generic enemy soldier", None, 34, 25, 25, 'Iron_lance', None)

ConstructionSite = Room("Construction Site", 'Job', 'Home', None, None,
                        "It's just a building in contruction however something catches your eye with a shine. "
                        "You can go east or south.")
HomeEntrance = Room("Home-Entrance", 'Garage', 'Living Room', 'Construction Site', None,
                "Home sweet Home except that your house been ruined! The thieves left a treasure map you found a "
                "while back,they thought it was fake probably, "
                "your only hope is to find treausre fast. You can go east, south, and north.")
HomeLivingRoom = Room("Home-Living Room", 'Home', 'Kitchen', None, None,
                   "The best part of the day ruined. You can go North or West.")
Job = Room("Job", None, 'In_Town', None, 'Construction Site',
           "Where you spend most of your day. You don't really hate it. Just no one to talk to. "
            "You can go west or south.")
Kitchen = Room("Kitchen", 'Home-Living Room', None, None, None,
               "Nothing usual here, get your food before your adventure, can't rely on fast food. You can go east.")
Freeway = Room("Freeway", 'Garage', 'Playground', None, 'Intown',
               "Not much traffic today. You can go West, South or East")
Playground = Room("Playground", None, 'Park', 'Freeway', None,
                  "Don't stay here for to long, the map has a X somewhere around here. You can go south or north.")
InTown = Room("In Town", 'Store', 'Airport', 'Job', 'Freeway',
              "Busy as ever, the town leads to mutiple directions. You can go North, East, South or West.")
Garage = Room("Garage",'Intown', None ,None, 'HomeEntrance',
              "You only use your car for buniess trips so you mainly walk. You can go east or west.")
Store = Room("Store", None, None, None, 'Intown',
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
short_direction = ['n', 's', 'e', 'w']

while True:
    print(current_node.name)
    print(current_node.description)
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
