import colour
import random

import ModuleLocation


print("Hello player, welcome to the game!")
name = input("What is your name? ")
print("Hello " + name + ", let's start the game!")
print("You are in a dark room.")
print("There is a door to your right and left.")
print("Which one do you take?")
door = input("Type R for right and L for left: ")
while True:
    if door == "R":
        print("There is a monster in the room!")
        print("What do you do?")
        print("1. Fight the monster")
        print("2. Run away")
        ModuleLocation.locationVillage()
        fight = input("Type 1 or 2: ")
        if fight == "1":
            print("You fought the monster and won!")
            print("You are now free!")
            break
        elif fight == "2":
            print("You ran away and lost the game!")
            break
        else:
            print("Invalid input! You lose!")
            break
    elif door == "L":
        print("You found the treasure!")
        print("You win!")
        break
    else:
        print("Invalid input! You lose!")
        break
print("Game over!")
input("Press enter to continue...")
start = input("Do you want to play again? (Y/N): ")
while True:
    if start == "Y":
        print("Hello player, welcome to the game!")
        name = input("What is your name? ")
        print("Hello " + name + ", let's start the game!")
        print("You are in a dark room.")
        print("There is a door to your right and left.")
        print("Which one do you take?")
        door = input("Type R for right and L for left: ")
        print (start)
    elif start == "N":
        print("Goodbye!")
        break
    else:
        print("Invalid input! Game closes!")
        break