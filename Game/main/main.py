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
            print("On a cold December morning, " , gamesave.name , '''wakes up and goes through their morning routine.
It's Saturday, a week before Christmas, and ''' , gamesave.name, ''' looks at the Christmas tree in the distance.
It's from the old hag across the neighborhood, and though most elderly people here love the decorative tree,
it's old-fashioned and used up.
''',gamesave.name, '''is thinking of becoming a Santa themselves, making the younger people happy since the elderly are lacking love for the younger.
They go to the store and get food and toys for the younger kids. 
            ''')

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
            