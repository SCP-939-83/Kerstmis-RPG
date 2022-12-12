# Alpha version 0.01
# creation date = 12-09-2022
# last update = 12-09-2022
# author = @HetGameBoekje

import ModuleRandomDMG
import ModuleLocation
import ModuleRandomINV

if input("Do you want to fight a monster? (Y/N): ") == "Y":
    ModuleRandomDMG.random_dmg()


# while True and ModuleLocation.location == "Forest":
#     if ModuleRandomDMG.hp <= 0:
#         print("You won and defeated monster!")
#         ModuleRandomINV.gold = ModuleRandomINV.gold + 5
#         ModuleRandomINV.xp = ModuleRandomINV.xp + 3
#         break
#     else:
#         ModuleRandomDMG.random_dmg()

while ModuleRandomDMG.hp > 0:
    global hp
    ModuleRandomDMG.random_dmg()
    print("You attacked the monster!")
    print("The monster has", ModuleRandomDMG.hp, "hp")
    print("You did", ModuleRandomDMG.dmg, "dmg")
    print("Now , the monster has", ModuleRandomDMG.hp, "hp")
    print("------------------")
    if ModuleRandomDMG.hp <= 0:
        print("You won and defeated monster!")
        break