# player is at village and has to go to the forest

import FightModule
import random
import gamesave
import time
import ModuleRandomINV
import main

shopping = 0


def locationVillage():
    global location
    scene = random.randint(1, 601)
    if scene <= 10:
        print("You went to the old hag's house to check whats going on")
        time.sleep(1)
        print("You turned on her PC and logged into the name of chell")
        time.sleep(1)
        print("GlaDOS booting...")
        time.sleep(1)
        print("You looked around while the computer is booting")
    elif scene >= 11 and scene <= 100:
        print("you went to the old hags house but the homeless person is there.")
        time.sleep(1)
        print("\x1B[3m" + "Wheatley, What do i do?" + "\x1B[0m")
        time.sleep(1)
        print("\x1B[3m" + "You said this will work and completely remove GlaDOS but this stupid PC still boots into this old OS" + "\x1B[0m")
    elif scene >= 101 and scene <= 500:
        print("You talked to some villagers in the village.")
        time.sleep(1)
    elif scene >= 501 and scene <= 600:
        print("You found an item")
        time.sleep(1)
    else:
        print(3)
    print("You are at the village")
    time.sleep(1)
    print("You can go to the forest or the mountain")
    time.sleep(1)
    print("Which one do you choose?")
    startGame()


def locationForest():
    global location
    scene = random.randint(1, 601)
    if scene <= 10:
        print("You encountered a strange looking place...")
        time.sleep(1.2)
    elif scene >= 11 and scene <= 100:
        print("You found an item!")
    elif scene >= 101 and scene <= 500:
        time.sleep(4)
        print("You walked arount but nothing happened")
        time.sleep(1)
        startGame()
    elif scene >= 501 and scene <= 600:
        print("Drunk person is attacking you!")
        FightModule.drunk()        
        time.sleep(1.76)
        startGame()
    else:
        print(3)
    print("You can go to the village or the mountain")
    print("Which one do you choose?")
    startGame()


def locationMountain():
    global location
    scene = random.randint(1, 601)
    if scene <= 10:
        print("You went up the mountain.")
        time.sleep(3)
        print("Oh no... You're falling...")
        time.sleep(5)
        print("You landed and you landed softly on a flowerbed")
        time.sleep(0.4)
        print("A flower, Goats and skeletons are down here in some kind of ruin.")
        time.sleep(1)
        print("You are loved but decided not to stick here. You left the underground.")
    elif scene >= 11 and scene <= 100:
        print("its too cold you went back")
        startGame()
    elif scene >= 101 and scene <= 500:
        print("You found an item!")
        ModuleRandomINV.itemgen()
    elif scene >= 501 and scene <= 600:
        for i in range(3):
            ModuleRandomINV.itemgen()
    else:
        print(3)
    startGame()


def startGame():
    global location
    time.sleep(4)
    print('''You are able to travel to the next locations.
     - forest
     - village
     - mountain
     - store ''')
    time.sleep(1)
    print('''Here is a map of your area.
Note you cannot travel to some of those locations!
     Big tree - Village
         |         |
    Home - Place of Delict -  Store
       |   |
       | Mountain
       |   |
      Forest
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
    scene = random.randint(1, 601)
    if scene <= 10:
        print("The store is closed, come back later.")
        time.sleep(1)
        startGame()
        pass
    elif scene >= 11 and scene <= 100:
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
            time.sleep(2)
            startGame()
        print("You got everthing from the store and went outside...")
        time.sleep(1.2)
        shopping += 1
        print("You decided to travel somewhere")
        time.sleep(1)
        startGame()
    elif scene >= 101 and scene <= 500:
        print("You went inside and got everything you needed.")
        shopping += 1
        print(shopping)
        print("You decided to travel somewhere")
        time.sleep(1)
        startGame()
        return shopping
    elif scene >= 501 and scene <= 600:
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
        time.sleep(2)
        startGame()
    else:
        time.sleep(2)
        print("Oh no, You stared at a wall.")
        time.sleep(1)
        print("You felt silly for walking into that wall.")
        time.sleep(1)
        locationStore()

def locationHag():
        conversation = input("Do you want to talk to the old hag? (yes/no) ")
        if conversation == "yes":
            main.tasks_completed += 1
            print("You approach the old hag and start a conversation.")
            time.sleep(1)
            print("Old hag: Hello there, young one. What brings you to my humble abode?")
            response = input("What do you say? ")
            print("You: " + response)
            time.sleep(1)
            print("Old hag: Ah, I see. Well, I was just about to make myself a cup of tea. Would you be so kind as to help an old hag like me?")
            help_decision = input("Do you help the old hag make a cup of tea? (yes/no) ")
            if help_decision == "yes":
                main.tasks_completed += 1
                print("You decide to help the old hag make a cup of tea.")
                time.sleep(1)
                print("Old hag: Thank you so much, dear. It's not easy for an old hag like me to do everything on my own. Here, have a cup of tea with me.")
                time.sleep(1)
                print("You sit down and enjoy a cup of tea with the old hag. She tells you stories of her younger days and you both have a nice chat.")
                time.sleep(1)
            else:
                print("You decide not to help the old hag make a cup of tea.")
                gamesave.karma += 10
                print("Old hag: Ah, well never mind then. It was nice talking to you. Take care now.")
                time.sleep(1)
                print("A few days pass and you hear that the old hag has passed away from severe injuries.")
                time.sleep(1)
                print("The villagers decide to bury her next to her favorite tree as a final resting place.")
                time.sleep(1)      
        else:
            print("You decide not to talk to the old hag and leave the location.")
            pass
