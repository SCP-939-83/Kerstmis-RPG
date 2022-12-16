import gamesave

gamesave.playerfilecheck()


match gamesave.level:
    case 1:
        print("You entered the first level")
    case 2:
        print("You entered the second level")
    case 3:
        print("You entered the third level")
    case _:
        print("You are in an unknown level")