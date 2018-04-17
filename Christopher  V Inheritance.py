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











