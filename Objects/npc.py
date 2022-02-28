"This is the NPC class, it includes the name and description pramaters."


class NPC:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        npcStr = ""
        npcStr = npcStr + "(NPC) Name: " + self.name + "\n"
        npcStr = npcStr + "(NPC) Description: " + self.description + "\n"
        return npcStr
