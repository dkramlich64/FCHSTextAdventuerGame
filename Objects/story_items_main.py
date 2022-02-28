from items import Weapons, Armor, Cures, Item

from enemies import Enemy

from npc import NPC

npcs = []
enemies = []
weapons = []
armors = []
Cures_1 = []
items = []

#reading from the items_general.txt file
fo = open("items_general.txt")
items_lines = fo.readlines()
fo.close()
#========================

#reading from the items_armor.txt file
fo = open("items_cure.txt")
cure_lines = fo.readlines()
fo.close()
#========================

#reading from the items_armor.txt file
fo = open("items_armor.txt")
armors_lines = fo.readlines()
fo.close()
#========================

#reading from the npc.txt file
fo = open("npc.txt")
npc_lines = fo.readlines()
fo.close()
#========================

#reading lines from items_weapons.tct
fo = open("items_weapons.txt")
weapons_lines = fo.readlines()
fo.close()
#=========================

#reading from enemy.txt file
fo = open("enemy.txt")
enemies_lines = fo.readlines()
fo.close()
#=========================
"""
Enemy Index
0 = Teacher Monster
1 = Principle Monster
2 = Student Monster
3 = Gym Coach mini Monster
"""
for i in range(0, len(enemies_lines), 4):
    name = enemies_lines[i].rstrip()
    description = enemies_lines[i + 1].rstrip()
    hp = float(enemies_lines[i + 2].rstrip())
    damage = float(enemies_lines[i + 3].rstrip())
    new_enemy = Enemy(name, description, hp, damage)
    enemies.append(new_enemy)

#====================================================
"""
Npc index
0 = Steven
1 = Mr.NickleBottom
2 = Kaori
3 = Marissa
4 = Geoff
"""
for i in range(0, len(npc_lines), 2):
    name = npc_lines[i].rstrip()
    description = npc_lines[i + 1].rstrip()
    new_npc = NPC(name, description)
    npcs.append(new_npc)

#====================================================
"""
Weapons index
Baseball_Bat 
Pencils and pens
Scissor
Fire_Extigisher
"""
for i in range(0, len(weapons_lines), 3):
    name = weapons_lines[i].rstrip()
    description = weapons_lines[i + 1].rstrip()
    damage = float(weapons_lines[i + 2].rstrip())
    new_weapon = Weapons(name, description, damage)
    weapons.append(new_weapon)

#====================================================
"""
Armor Index
0 = Football helmet
1 = Football chestplate
2 = Lacrosse goggles
3 = Lacrosse gauntlets
4 = Knee pads
"""
for i in range(0, len(armors_lines), 3):
    name = armors_lines[i].rstrip()
    description = armors_lines[i + 1].rstrip()
    hp = float(armors_lines[i + 2].rstrip())
    new_armor = Armor(name, description, hp)
    armors.append(new_armor)

#====================================================
"""
Cure Index
0 = Hydrogen peroxide
1 = Magnesium
2 = Iodine 
3 = Cortizone 
4 = Wite out
"""
for i in range(0, len(cure_lines), 2):
    name = cure_lines[i].rstrip()
    description = cure_lines[i + 1].rstrip()
    new_cure = Cures(name, description)
    Cures_1.append(new_cure)

#====================================================
"""
Items Index
0 = Teacher’s Keys
1 = Backpack
2 = Healing
3 = Textbook
"""
for i in range(0, len(items_lines), 3):
    name = items_lines[i].rstrip()
    description = items_lines[i + 1].rstrip()
    value = float(items_lines[i + 2].rstrip())
    new_items = Item(name, description, value)
    items.append(new_items)

#====================================================

for armor in armors:
    print(armor)

for cure in Cures_1:
    print(cure)

for weapons in weapons:
    print(weapons)

for npc in npcs:
    print(npc)

for enemy in enemies:
    print(enemy)

for item in items:
    print(item)
