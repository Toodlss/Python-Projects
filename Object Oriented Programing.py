# Class (blueprint)
class Player:
    def __init__(self, gold, level):
        self.gold = gold
        self.level = level


# Character classes
class Warrior(Player):
    def __init__(self, gold, level, health, manna):
        super().__init__(gold, level)
        self.health = health
        self.manna = manna

class Mage(Player):
    def __init__(self, gold, level, health, manna):
        super().__init__(gold, level)
        self.health = health
        self.mana = manna

# Objects
player1 = Warrior(2, 3, 100, 50)
player2 = Mage(3, 35, 50, 100)
