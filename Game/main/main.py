import gamesave
import time
import ModuleLocation
import ModuleRandomINV
import FightModule
karma = 0
tasks_completed = 0

gamesave.playerfilecheck()
level = gamesave.level
savelevel = gamesave.savelevel
inventory = ModuleRandomINV.inventory
gamesave.inventory = ModuleRandomINV.inventory + gamesave.inventory
gamesave.karma = FightModule.karma + gamesave.karma

def shoppingcheck():
    global savelevel
    if ModuleLocation.shopping <= 0:
        print("Maybe you should go back to the store. You didnt get anything yet")
        time.sleep(1.3)
        ModuleLocation.locationStore()
        shoppingcheck()
    elif ModuleLocation.shopping >= 1:
        print("You passed on to home...")
        savelevel += 1
        main()
    else:
        savelevel += 1
        pass
    return level


def main():
    match savelevel:
        case 1:
            print("            On a cold December morning, ", gamesave.name, '''wakes up and goes through their morning routine.
            It's Saturday, a week before Christmas, and ''', gamesave.name, ''' looks at the Christmas tree in the distance.
            It's from the old hag across the neighborhood, and though most elderly people here love the decorative tree,
            it's old-fashioned and used up.
            ''', gamesave.name, '''is thinking of becoming a Santa themselves, making the younger people happy since the elderly are lacking love for            the younger.
            You go to the store and get food and toys for the younger kids. ''')
            ModuleLocation.locationStore()
            shoppingcheck()
            main()
        case 2:
            print("You decided to go home")
            print("\x1B[3m" + '''
the moment you are coming home, they hear a honking car and a big bang. They look out the window and see two cars have crashed into each other - one car and a tanker. The tanker is leaking an unknown fluid and the car driver is dead. There doesn't seem to be anyone in the tanker, but there is an unknown bystander - a homeless person with a Christmas hat. The mess is cleaned up and the body is buried near the tree as a memorial to the incident. It was the old hag, who no one appreciated. 
            ''' + "\x1B[0m")
            print("You are able to make your own twist to this story.")
            print('''
            The homeless person runs away, The old hag is hurt
            
             ''')
            time.sleep(3)
            print("The old hag is recovering in her home...")
            gamesave.savelevel = 3
            gamesave.savegame()
            
            main()
        case 3:
            print("You decided to visit the old hag across the neighborhood.")
            ModuleLocation.locationHag()
            gamesave.savelevel += 1
            gamesave.savegame()
        case 4:
            print("You decide to spend the day helping out in the village.")
            ModuleLocation.locationVillage()
            global tasks_completed
            while tasks_completed < 5:
                print(
                    "You see three villagers who could use some help with various tasks.")
                print("Villager 1: Hello there! I could use some help fixing the roof on my house. It's been leaking in the rain lately.")
                print("Villager 2: Hey, do you have any spare time to help me tend to my garden? The weeds have been growing out of control.")
                print("Villager 3: Hi there! I'm trying to fix the well in the village, but I could use an extra hand. Do you think you could help?")
                task = input(
                    "Which task do you want to help with? (1, 2, or 3) ")
                if task == "1":
                    print(
                        "You decide to help the first villager fix the roof on their house.")
                    print("Villager 1: Thank you so much for your help! The roof is finally fixed and no longer leaking. Here, let me tell you a bit about the history of this village. Did you know that the tree in the center of the village used to be a gathering place for the villagers to share stories and celebrate important events?")
                    tasks_completed += 1
                elif task == "2":
                    print(
                        "You decide to help the second villager tend to their garden.")
                    print("Villager 2: Thank you for your help! The garden looks so much better now. Here, let me tell you a bit about the history of this village. Did you know that the tree in the center of the village used to be a sacred place for the villagers, and they would leave offerings there to honor their ancestors?")
                    tasks_completed += 1
                elif task == "3":
                    print(
                        "You decide to help the third villager fix the well in the village.")
                    print("Villager 3: Thank you for your help! The well is finally fixed and the village has access to clean water again. Here, let me tell you a bit about the history of this village. Did you know that the tree in the center of the village used to be a beacon of hope for the villagers during times of hardship, and they would go to the tree to pray for a better future?")
                    tasks_completed += 1
                else:
                    print("Invalid choice. Please choose a valid task to help with.")
            print("You have completed all three tasks and learned more about the history of the village and the tree. It was a fulfilling day spent helping out and learning new things.")
            if tasks_completed > 5:
                gamesave.savelevel = 6
                gamesave.savegame
            elif tasks_completed > 2 and tasks_completed < 5:
                print("You helped some villagers, but not enough. Would you like to help more villagers?")
                helpVillagers = input("Yes / No")
                helpVillagers = helpVillagers.lower()
                if helpVillagers == "yes":
                    main()
                else:
                    gamesave.savelevel = 5
            gamesave.savegame()
            main()
        case 5:
            print("You decide not to help anyone in the village and instead go after the homeless person you chased earlier.")
            print("After a long chase, you lose the homeless person and end up near the old hag's house.")
            print("Exhausted and hurt, you decide to rest at the old hag's house.")
            sleep_decision = input("Do you want to sleep? (yes/no) ")
            if sleep_decision == "yes":
                print("You decide to sleep and fall into a deep slumber.")
                print("Suddenly, you hear a weird noise and wake up to find the homeless person standing over you with a knife.")
                print("You try to call for help, but realize that you have no cellular data available.")
                print("You fight the homeless person, but are severely injured in the process.")
                FightModule.Endbattle()
                print("You manage to survive the fight, but are left with severe injuries.")
                gamesave.savelevel = 7
                gamesave.savegame()
                main()
            else: 
                print("8")
                gamesave.savelevel = 8
                print(gamesave.savelevel)
                gamesave.savegame()
                main()
        case 6:
            print("You have given away all your presents and managed to keep the homeless person at bay.")
            print("As you walk around the village, you notice the old, decrepit tree in the center of the village. You remember hearing stories about its history and realize that it's time for it to be taken down.")
            cut_tree = input("Do you want to cut down the evil tree? (yes/no) ")
            if cut_tree == "yes":
                print("You decide to cut down the evil tree.")
                print("With determination and strength, you manage to bring down the old tree. The villagers cheer and thank you for your bravery and selflessness.")
            else:
                print("You decide not to cut down the tree and leave it be.")
            print("It's the end of the holiday season and you feel a sense of accomplishment and joy from being able to bring happiness to those around you.")
            print("Thank you for playing! The game has now ended.")
        case 7:
            print("You are severely injured and unable to fight back against the homeless person.")
            print("As the homeless person approaches you with the intention of killing you, you realize that you have one last chance to protect the village.")
            print("With all the strength you have left, you manage to kamikaze the homeless person, sacrificing yourself in the process.")
            print("You die, but your bravery and selflessness have saved the village from further harm.")
            print("Thank you for playing. The game has now ended.")
        case 8:
            print("You have become consumed by evil and decide to turn against the villagers.")
            for i in range(17):
                FightModule.option()
            if FightModule.karma > 20:
                print("You have become too evil and are no longer able to continue on this path.")
                print("Your actions have caused harm to others and brought misery to the village.")
                print("As a result, your save game is reset and you are given the opportunity to start anew and make better choices.")
                gamesave.savelevel = 1
                main()
            elif FightModule.karma < 10:
                print("You have not fully embraced your evil side and are not deemed worthy of staying in the village.")
                print("You are kicked out of the village and are unable to return.")
    
                gamesave.savelevel = 100
                main()
            elif FightModule.karma == 0:
                print("You have managed to maintain a balance between good and evil, and your actions have brought happiness to the village.")
                print("Everyone is grateful for your help and kindness, and you are rewarded with a special message:")
                print("'You are a true hero, and your actions will always be remembered in the village.'")
                print("Thank you for playing. The game has now ended on a positive note.")
            else:
                print("You have successfully become evil and have caused harm to others.")
                print("However, your actions have not gone unnoticed and you are eventually brought to justice for your crimes.")
                print("Thank you for playing. The game has now ended.")

        case _:
            print("You are in an unknown level")
            for i in range(5):
                time.sleep(1)
                print("ZZzzz....")
            time.sleep(1)
            reset = input("Reset gamelevel?")
            if reset == "yes":
                gamesave.savelevel = 1
                gamesave.savegame()
                main()
            else: 
                print("Maybe later...")
            main()
if __name__ == "__main__":
    main()