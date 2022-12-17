import gamesave
import time
import ModuleLocation
import ModuleRandomINV
import FightModule

gamesave.playerfilecheck()
level = gamesave.level
savelevel = gamesave.savelevel
inventory = ModuleRandomINV.inventory
gamesave.inventory = ModuleRandomINV.inventory + gamesave.inventory
gamesave.karma = FightModule.karma + gamesave.karma
karma = 0
def main():
    match savelevel:
        case 1:
            print("you entered the first level")
            time.sleep(0.75)
            ModuleLocation.startGame()
            time.sleep(1)
            
            print("You have", gamesave.level, "level")
            print("You have", gamesave.karma, "gamesave karma")
            print("You have", FightModule.karma, "fight module karma")
            print(karma, "karma")
            gamesave.savegame()

        case 2:
            print("You entered the second level")

            main()
        case 3:
            print("You entered the third level")
            gamesave.level += 1
            print(gamesave.level, "level")
            time.sleep(1)
            gamesave.savegame()
            gamesave.playerfilecheck()
        case _:
            print("You are in an unknown level")
            time.sleep(0.1)
            global ik 
            ik = ik + 1        
            print(ik , "times")
            time.sleep(0.1)
            main()
            return ik
            
main()
            