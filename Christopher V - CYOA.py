class Item(object):
    def __init__(self, name):
        self.name = name

    def pick_up(self):
        print("You picked up %s" % self.name)


class Money(Item):
    def __init__(self, name, trade):
        super(Money, self).__init__(name)
        self.trade = trade

    def trade(self):
        print("You have made a trade with %s" % self.name)


class MonsterWeapon(Item):
    def __init__(self, close_range, damage, name):
        super(MonsterWeapon, self).__init__(name)
        self.close_range = close_range
        self.damage = damage


class Fangs(MonsterWeapon):
    def __init__(self, close_range, damage, name):
        super(Fangs, self).__init__(close_range, damage, name)

    def attacked(self):
        print("You were attacked by a Wolf with %s" % self.name)


class Weapon(Item):
    def __init__(self, name, damage, durability):
        super(Weapon, self).__init__(name)
        self.damage = damage
        self.durability = durability

    def equip(self):
        print("You equip a %s" % self.name)


class KeyItem(Item):
    def __init__(self, name):
        super(KeyItem, self).__init__(name)


class Map(KeyItem):
    def __init__(self, name, check):
        super(Map, self).__init__(name)
        self.check = check


class Map2(KeyItem):
    def __init__(self, name, check):
        super(Map2, self).__init__(name)
        self.check = check


class CarKeys(KeyItem):
    def __init__(self, name, ignite):
        super(CarKeys, self).__init__(name)
        self.ignite = ignite
        

class ToyBone(KeyItem):
    def __init__(self, name, throw):
        super(ToyBone, self).__init__(name)
        self.throw = throw


class StrangeEye(KeyItem):
    def __init__(self, name, place):
        super(StrangeEye, self).__init__(name)
        self.place = place


class Healing(Item):
    def __init__(self, name, restoration, cure, buffs):
        super(Healing, self).__init__(name)
        self.restoration = restoration
        self.cure = cure
        self.buffs = buffs

    def heal(self):
        print("You gained %s thanks to a potion." % self.buffs)

        
class Fruit(Healing):
    def __init__(self, name, restoration, cure, buffs):
        super(Fruit, self).__init__(name, restoration, cure, buffs)


class Potion(Healing):
    def __init__(self, name, restoration, cure, buffs):
        super(Potion, self).__init__(name, restoration, cure, buffs)

    def heal(self):
        print("You gained %s thanks to a potion." % self.buffs)


class Armor(Item):
    def __init__(self, name, defense, magic_defense):
        super(Armor, self).__init__(name)
        self.defense = defense
        self.magic_defense = magic_defense

    def equip(self):
        print("You have protection thanks to your %s" % self.name)


class Magic(Item):
    def __init__(self, name, magic_damage, close_range, far_range):
        super(Magic, self).__init__(name)
        self.magic_damage = magic_damage
        self.close_range = close_range
        self.far_range = far_range

    def magic_attack(self):
        print("You attacked with %s" % self.name)


class Minor(Magic):
    def __init__(self, name, magic_damage, close_range, far_range):
        super(Minor, self).__init__(name, magic_damage, close_range, far_range)


class Drain(Magic):
    def __init__(self, name, magic_damage, close_range, far_range, life_drain):
        super(Drain, self).__init__(name, magic_damage, close_range, far_range)
        self.life_drain = life_drain


class Accessories(Item):
    def __init__(self, name):
        super(Accessories, self).__init__(name)

    def equip(self):
        print("You equipped %s" % self.name)


class Amulet(Accessories):
    def __init__(self, name, magic_defense):
        super(Amulet, self).__init__(name)
        self.magic_defense = magic_defense

    def protection(self):
        print("You took less magic damage thanks to your %s" % self.name)


class Shield(Accessories):
    def __init__(self, name, defense):
        super(Shield, self).__init__(name)
        self.defense = defense

    def protection(self):
        print("You took less damage thanks to your %s" % self.name)


class HeroMedal(Accessories):
    def __init__(self, name, damage_up):
        super(HeroMedal, self).__init__(name)
        self.damage_up = damage_up

    def buff(self):
        print("You feel more courages thanks to %s, Damage Up!" % self.name)


class SwiftBand(Accessories):
    def __init__(self, name, speed_up):
        super(SwiftBand, self).__init__(name)
        self.speed_up = speed_up

    def buff(self):
        print("You feel faster thanks to %s, Speed Up!" % self.name)


class Bow(Weapon):
    def __init__(self, name, damage, far_ranged, durability):
        super(Bow, self).__init__(name, damage, durability)
        self.far_ranged = far_ranged

    def attack(self):
        print("You attack from a distance with your %s." % self.name)


class Sword(Weapon):
    def __init__(self, name, damage, close_range, speed_up, durability):
        super(Sword, self).__init__(name, damage, durability)
        self.close_range = close_range
        self.speed_up = speed_up

    def attack(self):
        print("You attack with your %s." % self.name)


class TrainingSword(Sword):
    def __init__(self, name, damage, close_range, speed_up, durability):
        super(TrainingSword, self).__init__(name, damage, close_range, speed_up, durability)

    def attack(self):
        print("You attack with your %s" % self.name)


class Rapier(Sword):
    def __init__(self, name, damage, close_range, speed_up, durability, armor_piercing, beast_slaying):
        super(Rapier, self).__init__(name, damage, close_range, speed_up, durability)
        self.armor_piercing = armor_piercing
        self.beast_slaying = beast_slaying


class Lance(Weapon):
    def __init__(self, name, damage, close_range, defense_up, durability):
        super(Lance, self).__init__(name, damage, durability)
        self.close_range = close_range
        self.defense_up = defense_up
        self.durability = durability

    def attack(self):
        print("You attack with your %s." % self.name)


class GoldSpear(Lance):
    def __init__(self, name, damage, close_range, far_range, defense_up, durability):
        super(GoldSpear, self).__init__(name, damage, close_range, defense_up, durability)
        self.far_range = far_range


class Axe(Weapon):
    def __init__(self, name, damage, close_range, damage_up, durability):
        super(Axe, self).__init__(name, damage, durability)
        self.close_range = close_range
        self.defense = damage_up

    def attack(self):
        print("You attack with your %s." % self.name)


class MagicRobe(Armor):
    def __init__(self, name, defense, magic_defense, magic_up):
        super(MagicRobe, self).__init__(name, defense, magic_defense)
        self.magic_up = magic_up

    def protection(self):
        print("You took less magic damage, and gained more magic thanks to your %s" % self.name)


class Room(object):
    def __init__(self, name, east, south, north, west, desc, items):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.description = desc
        self.items = items

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


ConstructionSite = Room("ConstructionSite", 'Job', 'Home', None, None,
                        "It's just a building in contruction however something catches your eye with a shine."
                        "You can go east or south.", None)
HomeEntrance = Room("HomeEntrance", 'Garage', 'Living Room', 'Construction Site', None,
                    "Home sweet Home except that your house been ruined!"
                    "The thieves left a treasure map you found a while back, they thought it was fake probably,"
                    "your only hope is to find treausre fast. You can go east, south, and north.", None)
HomeLivingRoom = Room("HomeLivingRoom", 'Home', 'Kitchen', None, None,
                      "The best part of the day ruined. You can go North or West.", [TrainingSword])
Job = Room("Job", None, 'InTown', None, 'ConstructionSite', "Where you spend most of your day."
                        "You don't really hate it. Just no one to talk to. "
                        "You can go west or south.", None)
Kitchen = Room("Kitchen", 'Home-Living Room', None, None, None,
               "Nothing usual here, get your food before your adventure, can't rely on fast food. You can go east.",
               [Fruit, Fruit, Fruit, Fruit, Fruit])
Freeway = Room("Freeway", 'Garage', 'Playground', None, 'Intown',
               "Not much traffic today. You can go West, South or East", None)
Playground = Room("Playground", None, 'Park', 'Freeway', None,
                  "Don't stay here for to long, the map has a X somewhere around here. You can go south or north.",
                  [ToyBone])
InTown = Room("In Town", 'Store', 'Airport', 'Job', 'Freeway',
              "Busy as ever, the town leads to mutiple directions. You can go North, East, South or West.", None)
Garage = Room("Garage", 'InTown', None, None, 'HomeEntrance',
              "You only use your car for buniess trips so you mainly walk. You can go east or west.", [CarKeys])
Store = Room("Store", None, None, None, 'Intown',
             "A store where you can buy items. You can go west.", [Potion, Rapier])
AbandonedPark_Entrance = Room("Abandonded Entrance-Front", None, 'Forest', 'Playground', None,
                              "It is closed off to the public since wild animals live here. It is also very huge."
                              "Get ready to protect yourself. You can go North or South.", None)
AbandonedPark = Room("Abandoned Park", None, 'Forest', 'AbandonedPark_Entrance', None,
                     "You have a chance of running into enemies. Stay on guard. You can go south or north.", None)
Forest = Room("Forest", None, None, None, "Shrine",
              "The X on the map is just west of here.", None)
Shrine = Room("Shrine", 'Forest', None, None, None,
              "There's a shovel near the old shrine. You can go east.", [StrangeEye])
Airport = Room("Airport", 'Egypt', 'Mexico', 'In town', 'Japan',
               "Depending on which one you choose, the difficulty may change, choose north to back.", None)


class Character(object):
    def __init__(self, stat_total, health, description, name, attack, defense, speed, magic_defense, item,
                 abilities, experience):

        self.name = name
        self.stat_total = stat_total
        self.health = health
        self.description = description
        self.attack_amt = attack
        self.defense = defense
        self.magic_defense = magic_defense
        self.item = item
        self.abilities = abilities
        self.speed = speed
        self.experience = experience

    def attack(self, enemy):
        enemy.take_damage(self.attack_amt)

    def take_damage(self, dmg):
        total_damage = dmg - self.defense
        if total_damage < 0:
            total_damage = 0
        self.health -= total_damage
        if self.health <= 0:
            print("You died...")


You = Character(0, 25, "The main character of the story.", 'MC', 7, 5, 4, 2, [TrainingSword, Fruit], 'Multi Wield', 1)
Rabbid_Wolf = Character(25, 15, "A wolf that looks very hungry.", 'Rabbid Wolf', 2, 3, 5, 0, [Fangs], None, None)
Mummy = Character(40, 35, "A mummy brought back to life by some kind of sinister force.", 'Mummy', 7, 5, 2, 0,
                  'Undead Hand', None, None)
Skeleton = Character(38, 25, "A pile of bones reanimated by black magic.", 'Skeleton', 5, 4, 3, 0, 'Rusted Sword',
                     None, None)
Gargoyle = Character(34, 25, "Demons summoned from other world.", 'Gargoyle', 4, 3, 2, 0, 'Stone_Lance', None, None)
Servants = Character(51, 35, "Servants of the God of Death.", 'Servants', 8, 5, 4, 3, 'Minor', 'Summon', None)
Minatours = Character(58, 40, "Half Man, half monsters who wield gaint axes.", 'Minatours', 7, 5, 3, 0, "Giant Axe",
                      None, None)
Souls = Character(44, 30, "Cursed souls forced to fight.", 'Soldier', 4, 4, 4, 2, 'Rusted Axe', None, None)
Aknes = Character(38, 25, "A large serpent like creature.", 'Aknes', 3, 3, 6, 1, 'Poisonius Fangs', None, None)
Mini_Phoenix = Character(31, 20, "Offsprings of a legendary bird.", 'Mini_Phoenix', 3, 2, 4, 2, 'Talons', None, None)
Phoenix = Character(0, 50, "The flaming bird of legend.", 'Phoenix', 10, 10, 10, 5, [], 'Reproduce', None)
Anubis = Character(0, 60, "The God of Death himself.", 'Anubis', 25, 15, 12, 7, 'Sycthe', 'Command', None)
Saiper = Character(0, 45, 'Giant spider-Like, web maker.', 'Saiber', 8, 5, 7, 1, 'Poisinous Claws', 'Trap', None)
Pharaoh = Character(0, 50, "Their bodies are barely decomposed.", 'Pharaoh',  9, 7, 4, 2, 'Staff of Order', 'Command',
                    None)
Elites = Character(0, 40, "Great Soldiers of the undead.", 'Elites', 8, 8, 8, 4, [HeroMedal, GoldSpear], None, None)


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
        pos = short_direction.index(command)
        command = directions[pos]

    if command in directions:
        try:
            current_node.move(command)
        except KeyError:
            print('Command not recongized')
            print()
