class MapTile:
    def __init__(self, x, y, des, name):
        self.x = x
        self.y = y
        self.des = des
        self.name = name

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getDes(self):
        return self.des

    def getName(self):
        return self.name


#______________________________________
#is a empty room can't affect player, but they get to talk to npc.
class EmptyRoom(MapTile):
    def __init__(self, x, y, npc, name):
        self.npc = npc
        des = "empty"
        super().__init__(x, y, des, name)


#  def modify_player(self, player):
#    pass


#For rooms that have both enemies and loot
class LootandEnemy(MapTile):
    def __init__(self, typeroom, name, des, x, y, item, enemy):
        self.typeroom = typeroom
        super().__init__(x, y, des, name)
        self.item = item
        self.enemy = enemy

    def __str__(self):
        looteStr = ""
        looteStr = looteStr + "Room Name: " + self.name + "\n"
        looteStr = looteStr + "Description: " + self.des + "\n"
        looteStr = looteStr + "Item: " + self.item + "\n"
        looteStr = looteStr + "Enemy: " + self.enemy + "\n"
        return looteStr


#Loot room lets player add loot to inventory and states where the loot is in the room and what item it is
class LootRoom(MapTile):
    def __init__(self, typeroom, name, des, x, y, item):
        self.typeroom = typeroom
        super().__init__(x, y, des, name)
        self.item = item

    def __str__(self):
        lootStr = ""
        lootStr = lootStr + "Room Name: " + self.name + "\n"
        lootStr = lootStr + "Description: " + self.des + "\n"
        lootStr = lootStr + "item " + self.item + "\n"
        return lootStr


# Create inventory list
#def add_loot(self, player):
#player.inventory.append(self.item)

#def modify_player(self, player):
#self.add_loot(player)


#Enemy Room lets sets where the enemies are and what room they are in and modify their health
class EnemyRoom(MapTile):
    def __init__(self, typeroom, name, des, x, y, enemy):
        self.typeroom = typeroom
        super().__init__(x, y, des, name)
        self.enemy = enemy

    def modify_player(self, the_player):
        if self.enemy.is_alive():
            the_player.hp = the_player.hp - self.enemy.damage
            print("Enemy does {} damage. You have {} HP remaining.".format(
                self.enemy.damage, the_player.hp))

    def __str__(self):
        enemyStr = ""
        enemyStr = enemyStr + "Room Name: " + self.name + "\n"
        enemyStr = enemyStr + "Description: " + self.des + "\n"
        enemyStr = enemyStr + "Enemy: " + self.enemy + "\n"
        return enemyStr


class Hallway(MapTile):
    def __init__(self, typeroom, name, des, x, y):
        self.typeroom = typeroom
        super().__init__(x, y, des, name)

    def __str__(self):
        hallStr = ""
        hallStr = hallStr + "Room Name: " + self.name + "\n"
        hallStr = hallStr + "Description: " + self.des + "\n"
        return hallStr
