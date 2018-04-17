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

Rabbid_Wolf = Character()






