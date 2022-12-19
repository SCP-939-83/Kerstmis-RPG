# player is at village and has to go to the forest

import FightModule
import random
import gamesave
import time

shopping = 0

def locationVillage():
    global location
    print("You are at the village")
    print("You can go to the forest or the mountain")
    print("Which one do you choose?")
    startGame()



def locationForest():
    global location
    print("You are in the forest")
    FightModule.option()
    print("You can go to the village or the mountain")
    print("Which one do you choose?")
    startGame()



def locationMountain():
    global location
    print("You are in the mountain")
    print("You can go to the village or the forest")
    print("Which one do you choose?")
    startGame()


def startGame():
    global location
    print('''You are able to travel to the next locations.
     - forest
     - village
     - mountain
     - store 
    ''')
    location = input("Where would you like to travel to? ")
    location = location.lower()
    match location:
            case "forest":
                locationForest()
            case "village":
                locationVillage()
            case "mountain":
                locationMountain()
            case "store":
                locationStore()
            case "stop":
                print("You decided you didnt want to travel")
                pass
            case _:
                print("This is not an input.")
                startGame()



def locationStore():
    # print("You walked into the store.")
    global shopping
    scene = random.randint(1,601)
    if scene <= 10:
        print("The store is closed, come back later.")
        startGame()
        pass
    elif scene >=11 and scene <= 100:
        print("two blokes are talking and standing in the way. ")
        print("Do you want to ask them to move?")
        blokesmove = input("Yes/No")
        blokesmove.lower()
        if blokesmove == "yes":
            print("You asked the blokes to move out of your way.")
            pass
        else:
            print("You decided to let them block your way to the store and travel on your own")
            print("You decided to travel somewhere")
            startGame()
        print("You got everthing from the store and went outside...")
        time.sleep(1.2)
        shopping += 1
        print("You decided to travel somewhere")
        startGame()
    elif scene >=101 and scene <= 300:
        print("You went inside and got everything you needed.")
        shopping += 1 
        print(shopping)
        print("You decided to travel somewhere")
        startGame()
        return shopping
    elif scene >=301 and scene <=600:
        time.sleep(2)
        print("It's a beautiful day outside")
        time.sleep(0.8)
        print("Bird's are singing.")
        time.sleep(0.8)
        print("Flower's are blooming.")
        time.sleep(0.8)
        print("On days like these, kids like you")
        time.sleep(1.4)
        print("Should go outside and get a SANSational gasp of fresh air")
        print("You decided to travel somewhere")
    else:
        time.sleep(2)
        print("Oh no, You stared at a wall.")
        time.sleep(1)
        print("You felt silly for walking into that wall.")
        locationStore()
