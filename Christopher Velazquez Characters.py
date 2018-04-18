class Character(object):
    def __init__(self, stat_total, health, description, name, attack, defense,speed, inventory, abilities, experience):

        self.name = name
        self.stat_total = stat_total
        self.health = health
        self.description = description
        self.attack_amt = attack
        self.defense = defense
        self.inventory = inventory
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

Rabbid_Wolf = Character(25, 15, "A wolf that looks very hungry.", 'Rabbid Wolf', 2, 3, 5, 'Fangs', None, None)
Mummy = Character(40, 25, "A mummy brought back to life by some kind of sinister force", 'Mummy', 7, 5, 3, 'Undead Hand',
                  None, None)
Skeleton = Character(35, 35, "A pile of bones reanimated",'Skeleton', 5, 5, 2, 'Rusted Sword', None, None)







