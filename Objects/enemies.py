"This is the enemy section where the main eniems are placed. Listed below are several eniemes from weak grunts  and to boss level eneiems. The eniems Name HP,damage are listed as well."


class Enemy:
    def __init__(self, name, description, hp, damage):
        self.name = name
        self.description = description
        self.hp = hp
        self.damage = damage

    def is_alive(self):
        return self.hp > 0

    def __str__(self):
        enemyStr = ""
        enemyStr = enemyStr + "(Enemy) Name: " + self.name + "\n"
        enemyStr = enemyStr + "(Enemy) Description: " + self.description + "\n"
        enemyStr = enemyStr + "(Enemy) Hp: " + str(self.hp) + "\n"
        enemyStr = enemyStr + "(Enemy) Damage: " + str(self.damage) + "\n"
        return enemyStr
