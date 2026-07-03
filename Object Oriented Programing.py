# Class (blueprint)
class Player:
    def __init__(self, gold, level):
        self.gold = gold
        self.level = level

    def attack(self):
        print("AAAAAHHHHHHH!!!!!")

# Character classes
class Warrior(Player):
    def __init__(self, gold, level, health, manna):
        super().__init__(gold, level)
        self.health = health
        self.manna = manna

    def attack(self):
        print("SLASH!!!!")
    

class Mage(Player):
    def __init__(self, gold, level, health, manna):
        super().__init__(gold, level)
        self.health = health
        self.manna = manna

    def attack(self):
        print("EEEEEEEEXXXXXXPPPPPPLLLLLLLLOOOOOOOOOOOOOOOOOOSSSSSIIIIOOOONNNNNNN")

# Objects
player1 = Warrior(2, 3, 100, 50)
player2 = Mage(3, 35, 50, 100)

while True:
    choice = input("Choose who attacks (P1/P2): ")

    if choice.lower() == "p1":
        player1.attack()
    elif choice.lower() == "p2":
        player2.attack()
    else:
        print("AAAAAAHHHHHHH!!!!!")


