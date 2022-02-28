from items import Weapons, Armor, Cures, Item, Gen

from enemies import Enemy

from npc import NPC

from player import player, movement, inventory

from map import EnemyRoom, LootandEnemy, LootRoom, Hallway

import os

""" Function: clearConsole
    Purpose: Clear the console screen
"""
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)
""" Function: introduction
    Purpose: Print out the introduction and set the scene
"""
def introduction():
    print(f"Welcome {player1}!!!\n")
    print("You are in Ms Cackle's room. All the Computers are lined on the wall and the screens are facing the inner part of the room.\n\nIt’s 12:30 PM, lunch time, and you’re supposed to be in the cafeteria but instead you are spending it in the computer science room. Lunch detention is always the worst. Waiting in silence for an hour, the only noise you hear is an occasional cough and the clock on the wall ticking. Unfortunately for you, you got stuck with the Marley twins who only know how to chew with their mouths open and your desk is right next to  Ms. Cackle, the Computer Science teacher. You decide to count the number of ants coming from a crack in the wall to a piece of candy that was discarded on the floor. '12, 13, 14...'\n\nPress <enter> to continue:")
    input()
    print("All of a sudden you hear -\n\t\t*ALARM SOUNDS*\n\t\tCODE RED.\n\t\tCODE RED.\n\n We are now under lock down. Please remain calm and follow through with the proper procedures.\n\nYou snap your head up from your line of ants to see Ms. Cackle stand up from her desk to only fall back down into her chair. She starts to convulse and groan. Her skin begins to get a bluish hue and her nails start to turn into sharp claws. You hear pained moans to you right. You slowly turn your head to the Marley twins foaming at the mouth. Their skin is a bright pink with large green blotches littering  their bodies. In a panic you grab the scissors off of your teachers desk and run to the middle of the room.\n\nIn front of you is the door leading into the hallway.  To your right are the Marley twins. To your left is Ms.Cackle.\n")

npcs = []

enemies = []
weapons = []
armors = []
Cures_1 = []
items = []
All_Items = []
world_map = []

""" Function: read_items
    Purpose: read all of the items from the specific files
            and load the information into All_Items
"""
def read_items():
    #reading from the items_general.txt file
    fo = open("items_general.txt")
    items_lines = fo.readlines()
    fo.close()
    #==================================================
    #reading from the items_armor.txt file
    fo = open("items_cure.txt")
    cure_lines = fo.readlines()
    fo.close()
    #=====================================================
    #reading from the items_armor.txt file
    fo = open("items_armor.txt")
    armors_lines = fo.readlines()
    fo.close()
    #=====================================================
    #reading from the npc.txt file
    fo = open("npc.txt")
    npc_lines = fo.readlines()
    fo.close()
    #=====================================================
    #reading lines from items_weapons.tct
    fo = open("items_weapons.txt")
    weapons_lines = fo.readlines()
    fo.close()
    #=====================================================

    #reading from enemy.txt file
    fo = open("enemy.txt")
    enemies_lines = fo.readlines()
    fo.close()
    #=====================================================
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

    #=====================================================
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

    #=====================================================
    """
  Weapons index
  0 = Baseball_Bat 
  1 = Pencils 
  2 = pens
  3 = Scissor
  4 = Fire_Extigisher
  """
    for i in range(0, len(weapons_lines), 3):
        name = weapons_lines[i].rstrip()
        description = weapons_lines[i + 1].rstrip()
        damage = float(weapons_lines[i + 2].rstrip())
        new_weapon = Weapons(name, description, damage)
        weapons.append(new_weapon)

    #=====================================================
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

    #=====================================================
    """
  Cure Index
  0 = Hydrogen peroxide
  1 = Magnesium
  2 = Iodine 
  3 = Cortizone 
  4 = White out
  """
    for i in range(0, len(cure_lines), 2):
        name = cure_lines[i].rstrip()
        description = cure_lines[i + 1].rstrip()
        new_cure = Cures(name, description)
        Cures_1.append(new_cure)

    #=====================================================
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
        value = items_lines[i + 2].rstrip()
        new_items = Gen(name, description, value)
        items.append(new_items)

    #=====================================================

    All_Items.extend(weapons)
    All_Items.extend(armors)
    All_Items.extend(Cures_1)
    All_Items.extend(items)

""" Function: read_rooms
    Purpose: read the room from the specific files and load the 
            data into world_map
"""
def read_rooms():
    """These constants sets the room types to a numerical value so that we don't have to change it to an int later"""
    ENEMY_ROOM = 1
    LOOT_ROOM = 2
    LOOT_ENEMY = 3
    HALLWAY = 4
    """These allow us to read from the txt files and sets the data gathered from them to a variable"""
    fo = open("loot.txt")
    loot_room = fo.readlines()
    fo.close()

    fo = open("lootandenemy.txt")
    lootandenemy = fo.readlines()
    fo.close()

    fo = open("hallway.txt")
    hall = fo.readlines()
    fo.close()

    fo = open("enemyR.txt")
    enemyR = fo.readlines()
    fo.close()

    #pulls the information from loot.txt and puts it into world_map
    for i in range(0, len(loot_room), 6):
        typeRoom = loot_room[i].rstrip()
        name = loot_room[i + 1].rstrip()
        des = loot_room[i + 2].rstrip()
        x = loot_room[i + 3].rstrip()
        y = loot_room[i + 4].rstrip()
        item_str = loot_room[i + 5].rstrip()
        item = -1
        for j in range(len(All_Items)):
            if item_str == All_Items[j].name:
                item = j
                break
        new_tile = LootRoom(typeRoom, name, des, x, y, item)
        world_map.append(new_tile)

    #pulls the information from lootandenemy.txt and puts it into world_map
    for i in range(0, len(lootandenemy), 7):
        typeRoom = lootandenemy[i].rstrip()
        name = lootandenemy[i + 1].rstrip()
        des = lootandenemy[i + 2].rstrip()
        x = lootandenemy[i + 3].rstrip()
        y = lootandenemy[i + 4].rstrip()
        item_str = lootandenemy[i + 5].rstrip()
        item = -1
        for j in range(len(All_Items)):
            if item_str == All_Items[j].name:
                item = j
                break
        enemy = lootandenemy[i + 6]
        new_tile = LootandEnemy(typeRoom, name, des, x, y, item, enemy)
        world_map.append(new_tile)

    #pulls the information from hall.txt and puts it into world_map
    for i in range(0, len(hall), 5):
        typeRoom = hall[i].rstrip()
        name = hall[i + 1].rstrip()
        des = hall[i + 2].rstrip()
        x = hall[i + 3].rstrip()
        y = hall[i + 4].rstrip()
        new_tile = Hallway(typeRoom, name, des, x, y)
        world_map.append(new_tile)

    #pulls the information from enemyR.txt and puts it into world_map
    for i in range(0, len(enemyR), 6):
        typeRoom = enemyR[i].rstrip()
        name = enemyR[i + 1].rstrip()
        des = enemyR[i + 2].rstrip()
        x = enemyR[i + 3].rstrip()
        y = enemyR[i + 4].rstrip()
        enemy = enemyR[i + 5].rstrip()
        new_tile = EnemyRoom(typeRoom, name, des, x, y, enemy)
        world_map.append(new_tile)

def read_data_files():
    read_items()
    read_rooms()

in_room = True
z = True
q = False
start = 0
read_data_files()
move = movement()
inven = inventory()


def location():
    for world in world_map:
        map = ("(" + str(world.getX()) + ',' + str(world.getY()) + ')')
        player = ("(" + str(move.getX()) + ',' + str(move.getY()) + ')')
        if (player == map):
            print("Room:", world.getName())
            print(world.getDes())

""" ====== Main Program ====== """
while True:
    if start == 0:
        player1 = input("What is your name? ")
        play = player(player1)
        introduction()
        start += 1
    location()
    response = input("\nEnter a command: ").lower()
    clearConsole()
    if 'quit' in response:
        response = input("To confirm type quit again to quit.").lower()
        response = response
        if 'quit' in response:
            break

    elif 'exit' in response:
        in_room = move.exit()
        in_room = True
        if z:
            q = not q
            z = not z

    elif 'enter' in response:
        in_room = move.enter()
        in_room = False
        if q:
            print("You cannot enter the a room from this position.")
            in_room = True
            q = not q
            z = not z
    
    elif 'help' in response:
        player.print_help()
    
    elif 'inv' in response:
        inven.check()

    if not in_room:
        if 'north' in response:
            move.north()

        elif 'south' in response:
            move.south()

        elif 'west' in response:
            move.west()

        elif 'east' in response:
            move.east()

    elif 'north' in response or 'south' in response or 'west' in response or 'east' in response:
        print("You cannot do that right now. You are within a room!  Try 'exit' first")
