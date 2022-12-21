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
            print("            On a cold December morning, " , gamesave.name , '''wakes up and goes through their morning routine.
            It's Saturday, a week before Christmas, and ''' , gamesave.name, ''' looks at the Christmas tree in the distance.
            It's from the old hag across the neighborhood, and though most elderly people here love the decorative tree,
            it's old-fashioned and used up.
            ''',gamesave.name, '''is thinking of becoming a Santa themselves, making the younger people happy since the elderly are lacking love for            the younger.
            You go to the store and get food and toys for the younger kids. ''')
            ModuleLocation.locationStore()
            shoppingcheck()
            main()
        case 2:
            print("You decided to go home")
            print("\x1B[3m" + '''
the moment you are coming home, they hear a honking car and a big bang. They look out the window and see two cars have crashed into each other - one car and a tanker. The tanker is leaking an unknown fluid and the car driver is dead. There doesn't seem to be anyone in the tanker, but there is an unknown bystander - a homeless person with a Christmas hat. The mess is cleaned up and the body is buried near the tree as a memorial to the incident. It was the old hag, who no one appreciated. 
            '''+ "\x1B[0m")
            print("You are able to make your own twist to this story.")
            print('''
            The homeless person runs away, The old hag is hurt
            
             ''')
            time.sleep(10)
            print("The old hag is recovering in her home...")
            gamesave.savelevel == 3
            main()
        case 3:
            print("You decided to visit the old hag across the neighborhood.")
            ModuleLocation.locationHag()
            gamesave.savelevel += 1
            gamesave.savegame()
        case _:
            print("You are in an unknown level")
            time.sleep(0.1)
            global ik 
            ik = ik + 1        
            print(ik , "times")
            time.sleep(0.1)
            main()
            return ik
def shoppingcheck():
    global savelevel
    if ModuleLocation.shopping <=0 :
        print("Maybe you should go back to the store. You didnt get anything yet")
        time.sleep(1.3)
        ModuleLocation.locationStore()
        shoppingcheck()
    elif ModuleLocation.shopping >=1 :
        print("You passed on to home...")
        savelevel += 1
        main()
    else: 
        savelevel += 1
        pass
    return level
main()
            