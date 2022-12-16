# player is at village and has to go to the forest

import FightModule
import ModuleRandomINV


def locationVillage():
    global location
    print("You are at the village")
    print("You can go to the forest or the mountain")
    print("Which one do you choose?")
    location = input("Type F for forest and M for mountain: ")
    if location == "F":
        locationForest()
    elif location == "M":
        locationMountain()
    elif location == "stop":
        pass
    else:
        print("Invalid input! Game closes!")
        exit()


def locationForest():
    global location
    print("You are in the forest")
    FightModule.option()
    if input("item?") == "yes":
        print("placeholder text for item use")
        ModuleRandomINV.itemgen()
    print("You can go to the village or the mountain")
    print("Which one do you choose?")
    location = input("Type V for village and M for mountain: ")
    if location == "V":
        locationVillage()
    elif location == "M":
        locationMountain()
    elif location == "stop":
        pass
    else:
        print("Invalid input! Game closes!")
        exit()


def locationMountain():
    global location
    print("You are in the mountain")
    print("You can go to the village or the forest")
    print("Which one do you choose?")
    location = input("Type V for village and F for forest: ")
    if location == "V":
        locationVillage()
    elif location == "F":
        locationForest()
    elif location == "stop":
        pass
    else:
        print("Invalid input! Game closes!")
        exit()


def startGame():
    global location
    print("Hello player, welcome to the game!")
    location = input(
        "Do you want to go to the village, forest or mountain? (V/F/M): ")
    if location == "V":
        locationVillage()
    elif location == "F":
        locationForest()
    elif location == "M":
        locationMountain()
    elif location == "stop":
        pass
    else:
        print("Invalid input! Game closes!")
        exit()


if __name__ == "__main__":
    startGame()
    print(location)
    input("Press enter to continue...")
