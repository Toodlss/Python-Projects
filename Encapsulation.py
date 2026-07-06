class Health:
    def __init__(self):
        self.__health = 1000

    def getHealth(self):
        return self.__health

    def setHealth(self, amount):
        self.__health = amount

        if self.__health <= 0:
            print("Player dies")


player = Health()

player.setHealth(500)
print(player.getHealth())

player.setHealth(0)
print(player.getHealth())
