#python: 3.11.7
#author: Kaden Bilyeu
#purpose: The Tech Academy - Python Course, Creating our first program together.
#         Demonstrating how to pass variable from function to funtion while
#         producing a functional game.



def start(nice=0,mean=0,name=""):
    # get user's name
    name = describe_game(name)
    nice,mean,name = nice_mean(nice,mean,name)

def describe_game(name) :
    # meaning, if we do not already have this users name,
    # then they are a new player and we need their name
    if name != "":
        print("\nThank you for playing again, {}!".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = input("\nWhat is your name? \n>>>").capitalize()
                if name != "":
                    print("\nWelcome, {}!".format(name))
                    print("\nIn this game, you will be greeted \nby several diffent people \nYou can choose to be nice or mean")
                    print("but at the end of the game your fate \nwill be sealed by your actions")
                    stop = False
        return name


def nice_mean(nice,mean,name):
    stop = True
    while stop:
        show_score(nice,mean,name)
        pick = input("\nA stranger approches you for a \nconversation. will you be nice \nor mean? (N/M) \n>>>: ").lower()
        if pick == "n":
            print("\nThe stranger walks away smilling...")
            nice = (nice+1)
            stop = False
        if pick == "m":
            print ("\nThe stranger glares at you \nmenacingly and storms off...")
            mean = (mean + 1)
            stop = False
    score(nice,mean,name) # pass on the three variables to the score()

def show_score(nice,mean,name) :
    #score funtion is being passed the values
    print ("\n{}, your current total: \n({},Nice) and ({}, Mean)".format(name,nice,mean))
def score(nice,mean,name) :
    if nice > 2:
        win(nice,mean,name)
    if mean > 2:
        lose(nice,mean,name)
    else:
        nice_mean(nice,mean,name)


def win(nice,mean,name) :
    print("\nNice job {}, you win! \nEveryone loves you and you've \nmade lots of friend along the way!".format(name))
    again(nice,mean,name)


def lose(nice,mean,name) :
     print("\nAhhh too bad, game over! \n{}, you live in a dirty beat up van wreched and alone!".format(name))
     again(nice,mean,name)


def again(nice,mean,name) :
    stop = True
    while stop:
        choice = input("\nDo you want to play again? (y/n):\n>>>").lower()
        if choice == "y":
            stop = False
            reset(nice,mean,name)
        if choice == "n":
            print("\nOh, so sad, sorry to see you go!")
            stop = False
            quit()
        else:
            print("\nEnter ( Y ) for 'yes', ( N ) for 'NO' :\n>>>")


def reset(nice,mean,name) :
    nice = 0
    mean = 0
    start(nice,mean,name)
    



















if __name__ == "__main__":
    start()
