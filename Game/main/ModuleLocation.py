# player is at village and has to go to the forest

import FightModule
import random
import gamesave



def locationVillage():
    global location
    print("You are at the village")
    print("You can go to the forest or the mountain")
    print("Which one do you choose?")



def locationForest():
    global location
    print("You are in the forest")
    FightModule.option()
    print("You can go to the village or the mountain")
    print("Which one do you choose?")
    location = input("Type V for village and M for mountain: ")



def locationMountain():
    global location
    print("You are in the mountain")
    print("You can go to the village or the forest")
    print("Which one do you choose?")
    location = input("Type V for village and F for forest: ")


def startGame():
    global location
    print("Hello player, welcome to the game!")
    print('''You are able to travel to the next locations.
     - forest
     - village
     - mountain
     - store 
    ''')
    location = input("Where would you like to travel to? ")

    location.lower()
    match location:
            case "forest":
                locationForest()
            case "village":
                locationVillage()
            case "mountain":
                locationMountain()
            case "store":
                locationStore()
            case _:
                print("This is not an input.")



def locationStore():
    # print("You walked into the store.")
    scene = random.randint(1,500)
    if scene <= 10:
        print("The store is closed, come back later.")
        pass
    elif scene >=11 and scene <= 500:
        print("two blokes are talking and standing in the way. ")


startGame()
