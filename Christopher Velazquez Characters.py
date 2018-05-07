class Character(object):
    def __init__(self, stat_total, health, description, name, attack, defense, speed, magic_defense, inventory,
                 abilities, experience):

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


You = Character(0, 25, "The main character of the story.", 'MC', 7, 5, 4, 2, 'Medicine, Sword', 'Multi Wield', 1)
Rabbid_Wolf = Character(25, 15, "A wolf that looks very hungry.", 'Rabbid Wolf', 2, 3, 5, 0, 'Fangs', None, None)
Mummy = Character(40, 35, "A mummy brought back to life by some kind of sinister force.", 'Mummy', 7, 5, 2, 0,
                  'Undead Hand', None, None)
Skeleton = Character(38, 25, "A pile of bones reanimated by black magic.", 'Skeleton', 5, 4, 3, 0, 'Rusted Sword',
                     None, None)
Gargoyle = Character(34, 25, "Demons summoned from other world.", 'Gargoyle', 4, 3, 2, 0, 'Stone_Lance', None, None)
Servants = Character(51, 35, "Servants of the God of Death.", 'Servants', 8, 5, 4, 3, 'Minor', 'Summon', None)
Minatours = Character(58, 40, "Half Man, half monsters who wield gaint axes.", 'Minatours', 7, 5, 3, 0, "Giant Axe",
                      None, None)
Souls = Character(44, 30, "Cursed souls forced to fight.", 'Soldier', 4, 4, 4, 2, 'Rusted Axe', None, None)
Aknes = Character(0, 25, "A large serpent like creature.", 'Aknes', 3, 3, 6, 1, 'Poisonius Fangs', None, None)
Mini_Phoenix = Character(31, 20, "Offsprings of a legendary bird.", 'Mini_Phoenix', 3, 2, 4, 2, 'Talons', None, None)
Phoenix = Character(0, 50, "The flaming bird of legend.", 'Phoenix', 10, 10, 10, 5, 'Flaming Talons', 'Reproduce', None)
Anubis = Character(0, 60, "The God of Death himself.", 'Anubis', 25, 15, 12, 7, 'Sycthe', 'Command', None)
Saiper = Character(0, 45, 'Giant spider-Like, web maker.', 'Saiber', 8, 5, 7, 1, 'Poisinous Claws', 'Trap', None)
Pharaoh = Character(0, 50, "Their bodies are barely decomposed.", 'Pharaoh',  9, 7, 4, 2, 'Staff of Order', 'Command',
                    None)
Elites = Character(0, 40, "Great Soldiers of the undead.", 'Elites', 8, 8, 8, 4, 'Gold Spear', None, None)
