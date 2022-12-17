import gamesave
import time
import ModuleLocation


gamesave.playerfilecheck()
level = gamesave.level
ik = 0
def main():
    match level:
        case 1:
            print("you entered the first level")
            time.sleep(0.75)
            ModuleLocation.startGame()
        case 2:
            print("You entered the second level")
            gamesave.level += 1
            print(gamesave.level, "level")
            time.sleep(1)
            gamesave.savegame()
            gamesave.playerfilecheck()

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
            