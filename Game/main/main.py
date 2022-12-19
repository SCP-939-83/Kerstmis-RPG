import FightModule
import LevelupModule
import ModuleLocation
import ModuleRandomINV

print("Welcome to the game")
print("You are in a forest, you see a cave, a river and a house")

ModuleLocation.startGame()

print("You have found a cave, do you want to go in?")
if input("yes/no: ") == "yes":
    print("You are in the cave")
    print("You see a chest")
    if input("Do you want to open it?") == "yes":
        for i in range (3):
            ModuleRandomINV.itemgen()
            print("You have found " + str(i) + " items")
            print("you encounter a monster") 
            FightModule.option()
input("Press enter to continue")
