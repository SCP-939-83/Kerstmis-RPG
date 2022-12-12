# have yet to build the main game, will be added in next patch after succelful merge request

import FightModule
import LevelupModule
import ModuleLocation
import ModuleRandomINV

print("Welcome to the game")
print("You are in a forest, you see a cave, a river and a house")

ModuleLocation.startGame()

print("You have found a cave, do you want to go in?")
if input("yes/no: ") == "yes":
    for i in range (19):
        ModuleRandomINV.itemgen()
ModuleRandomINV.inventoryshow()
input("Press enter to continue")
