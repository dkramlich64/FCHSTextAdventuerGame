class player:
    def __init__(self, player):
        self.player = player

        #self.health = 4

#self.armor = 0

    def print_help():
        print(
            'Please try one of the following commands: north, south, east, west, enter, exit, inventory or quit to quit the game.\n\n'
        )


class movement(player):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.rooms = [(0, 0), (0, 2), (0, 4), (2, 0), (2, 1), (2, 2), (2, 4),
                      (4, 0), (4, 2), (4, 4), (8, 0), (8, 2), (8, 4)]

    '''
  north 
  no parameters are needed for this function
  This function will move the player up one to the north by decreasing the y vaule by 1. If the player is unable to move in that direction they will be given a prompt stateing why they can not move forward.
  no vauled is returned in this function
  '''

    def north(self):
        move = False
        for room in self.rooms:
            if (self.x, (self.y - 1)) == room:
                print("You cannot do that right now. The room blocks the way!")
                move = True
                break
        if (self.y - 1 < 0 or move):
            print('NO! \nGo another way cause I said so.')
        else:
            self.y -= 1
            print("You moved North, your location is area: " + '(' +
                  str(self.x) + ',' + str(self.y) + ')' +
                  " in the y direction")

    '''
  south 
  no parameters are needed for this function
  This function will move the player down one to the south by increasing the y vaule by 1. If the player is unable to move in that direction they will be given a prompt stateing why they can not move forward.
  no vauled is returned in this function
  '''

    def south(self):
        move = False
        for room in self.rooms:
            if (self.x, (self.y + 1)) == room:
                print("You cannot do that right now. The room blocks the way!")
                move = True
                break
        if (self.y + 1 > 4 or move):
            print('NO! \nGo another way cause I said so.')
        else:
            self.y += 1
            print("You moved South, your location is area: " + '(' +
                  str(self.x) + ',' + str(self.y) + ')' +
                  " in the y direction")

    '''
  west
  no parameters are needed for this function
  This function will move the player left one to the west by decreasing the x vaule by 1. If the player is unable to move in that direction they will be given a prompt stateing why they can not move forward.
  no vauled is returned in this function
  '''

    def west(self):
        move = False
        for room in self.rooms:
            if ((self.x - 1), self.y) == room:
                print("You cannot do that right now. The room blocks the way!")
                move = True
                break
        if (self.x - 1 < 0 or move):
            print('NO! \nGo another way cause I said so.')
        else:
            self.x -= 1
            print("You moved West, your location is area: " + '(' +
                  str(self.x) + ',' + str(self.y) + ')' +
                  " in the x direction")

    '''
  east 
  no parameters are needed for this function
  This function will move the player right one to the east by increasing the x vaule by 1. If the player is unable to move in that direction they will be given a prompt stateing why they can not move forward.
  no vauled is returned in this function
  '''

    def east(self):
        move = False
        for room in self.rooms:
            if ((self.x + 1), self.y) == room:
                print("You cannot do that right now. The room blocks the way!")
                move = True
                break
        if (self.x + 1 > 9 or move):
            print('NO! \nGo another way cause I said so.')
        else:
            self.x += 1
            print("You moved East, your location is area: " + '(' +
                  str(self.x) + ',' + str(self.y) + ')' +
                  " in the x direction")

    def exit(self):
        for room in self.rooms:
            if ((self.x), self.y) == room:
                if (self.x != 8):
                    self.x += 1
                    print("You have exited a room")
                    print("Your location is area: " + '(' + str(self.x) + ',' +
                          str(self.y) + ')' + " in the x direction")
                    return True
                else:
                    self.x -= 1
                    print("You have exited a room")
                    print("Your location is area: " + '(' + str(self.x) + ',' +
                          str(self.y) + ')' + " in the x direction")
                    return True

    def enter(self):
        for room in self.rooms:
            if self.x != 7:
                if ((self.x - 1) == room[0] and self.y == room[1]):
                    self.x -= 1
                    print("You have entered a room")
                    print("Your location is area: " + '(' + str(self.x) + ',' +
                          str(self.y) + ')' + " in the x direction")
                    return False
            elif self.y == 0 or self.y == 2 or self.y == 4:
                self.x += 1
                print("You have entered a room")
                print("Your location is area: " + '(' + str(self.x) + ',' +
                      str(self.y) + ')' + " in the x direction")
                return False

    def getX(self):
        return self.x

    def getY(self):
        return self.y


class inventory(player):
    def __init__(self):
        self.inventory = []
        self.size = 2

    '''
  player can only pick up one item unless backpack 
  is aquired allowing them to pick up max of 5 items
  '''

    def pickup(self, player, item):
        if len(self.inventory) == 2:
            print("Your hands are full. You cannot pick up another item.")
        else:
            self.inventory.append(item)
            print(player, "picked up", item)

    '''
  pickup
  check the size of your inventory if the player is holding the maximum amount of items they can hold they return a statement stating inventory is full
  '''

    def check(self):
        print("Your inventory consists of.")
        for i in self.inventory:
            print('\t', i)
        print("\n\n")

    '''
  check
  prints out the items in the list of the players current inventory
  '''
