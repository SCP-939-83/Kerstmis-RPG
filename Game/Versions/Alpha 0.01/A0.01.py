# Alpha version 0.01
# creation date = 12-09-2022
# last update = 12-09-2022
# author = @HetGameBoekje

import ModuleRandomDMG
import ModuleLocation
import ModuleRandomINV

ModuleLocation.startGame()
if input("Do you want to fight a monster? (Y/N): ") == "Y":
    ModuleRandomDMG.random_dmg()
