import gamesave

gamesave.playerfilecheck()


match gamesave.level:
    case 1:
        print("You entered the first level")

    case _:
        print("You are in an unknown level")