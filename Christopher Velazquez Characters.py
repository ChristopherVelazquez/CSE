class Character(object):
    def __init__(self, stat_total, health, description, name, attack, defense,speed,magic_defense, inventory, abilities, experience):

        self.name = name
        self.stat_total = stat_total
        self.health = health
        self.description = description
        self.attack_amt = attack
        self.defense = defense
        self.magic_defense = magic_defense
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
Mummy = Character(40, 35, "A mummy brought back to life by some kind of sinister force.", 'Mummy', 7, 5, 2, 0,
                  'Undead Hand',None, None)
Skeleton = Character(38, 25, "A pile of bones reanimated by black magic.",'Skeleton', 5, 5, 3, 0, 'Rusted Sword',
                     None, None)
Gargoyle = Character(34,25, "Demons summoned from other world.", 'Gargoyle', 4, 3, 2, 0,'Stone_Lance', None, None)
Servants = Character(0, 35,"Servants of the God of Death.", 'Servants', 8, 6, 4, 3, 'Minor', 'Summon', None)










