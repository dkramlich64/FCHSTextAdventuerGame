"This section is dedicated to the items section multipe item classes are listed here such as: treasure,healing,Armor,Cure, Weapons"


class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        itemStr = ""
        itemStr = itemStr + "(Item) Name: " + self.name + "\n"
        itemStr = itemStr + "(Item) Description: " + self.description + "\n"
        return itemStr


class Armor(Item):
    def __init__(self, name, description, hp):
        self.hp = hp
        super().__init__(name, description)

    def __str__(self):
        armorStr = ""
        armorStr += "(Armor) Name: " + self.name + "\n (Armor) Description: " + self.description + "\n"
        armorStr = armorStr + "(Armor) HP: " + str(self.hp) + "\n"
        return armorStr


class Weapons(Item):
    def __init__(self, name, description, damage):
        self.name = name
        self.description = description
        self.damage = damage

    def __str__(self):
        weaponStr = ""
        weaponStr = weaponStr + "(Weapon) Name: " + self.name + "\n"
        weaponStr = weaponStr + "(Weapon) Description: " + self.description + "\n"
        weaponStr = weaponStr + "(Weapon) Damage: " + str(self.damage) + "\n"
        return weaponStr


class Cures(Item):
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        cureStr = ""
        cureStr = cureStr + "(Cure) Name: " + self.name + "\n"
        cureStr = cureStr + "(Cure) Description: " + self.description + "\n"
        return cureStr


class Gen(Item):
    def __init__(self, name, description, value):
        self.value = value
        super().__init__(name, description)

    def __str__(self):
        genStr = ""
        genStr += "(General Items) Name: " + self.name + "\n (General Items) Description: " + self.description + "\n"
        genStr = genStr + "(General Items) HP: " + str(self.value) + "\n"
        return genStr
