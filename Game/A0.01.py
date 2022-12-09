# Alpha version 0.01
# creation date = 12-09-2022
# last update = 12-09-2022
# author = @HetGameBoekje

import ModuleRandomDMG
import ModuleLocation
import ModuleRandomINV

print("Hello player, welcome to the game!")
name = input("What is your name? ")
print("Hello " + name + ", let's start the game!")
print("You are in a dark room.")
print("There is a door to your right and left.")
print("You decided to go to the right door.")
print("There is a monster in the room!")
print("What do you do?")
print("1. Fight the monster")
print("2. Run away")
ModuleRandomDMG.randomDMG()