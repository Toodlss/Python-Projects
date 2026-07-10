# Import the ABC module so we can create abstract classes
# Import random to generate random damage
from abc import ABC, abstractmethod
import random

class Player(ABC):

    #adds health
    def __init__(self):
        self.health = 100
        
    def die(self):
        print("AAAAAHHHHHH!!!!!!")

    # Abstract method
    @abstractmethod
    def attack(self, opponent):
        pass
        

class Warrior(Player):
    def attack(self, opponent):
        #calculates damage
        damage = random.randint(10, 25)
        #subtracts damage
        opponent.health -= damage
        #attacks
        print("THE WARRIOR ATTACKS SLASH!!!!!!!", damage, opponent.health)

        if opponent.health <= 0:
            print("The Monster has died!")
            opponent.die()

class Monster(Player):
    def attack(self, opponent):
        #random damage calculation
        damage = random.randint(10, 25)
        #calculates damage
        opponent.health -= damage 
        #attacks
        print("THE MONSTER ATTACKS CRASH!!!!!!!", damage,opponent.health) 

        #kills the opponent
        if opponent.health <= 0:
            print("The Warrior has died!")
            opponent.die()

# Create the objects
player = Warrior()
player1 = Monster()

# Call the child class method until one dies
while player.health > 0 and player1.health > 0:
    player.attack(player1)

    if player1.health <= 0:
        break

    player1.attack(player)


