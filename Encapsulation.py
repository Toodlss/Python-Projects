class Health:
    def __init__(self):
        # Private attribute because of the __ that sets health
        self.__health = 1000

    def getHealth(self):
        return self.__health

    def setHealth(self, amount):
        #changes the private health attribute
        self.__health -= amount
        print(self.__health)

        #prints if players health is at or below 0
        if self.__health <= 0:
            print("Player dies")

player = Health()

player.setHealth(500)

#kills player
player.setHealth(500)


