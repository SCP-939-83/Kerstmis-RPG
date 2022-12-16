import gamesave


gamesave.savegame()

print("hoi")
level = gamesave.level
match gamesave.level:
    case 1:
        print("You entered the first level")
        gamesave.level += 1
        print(gamesave.level, "level")
        gamesave.savegame()
        gamesave.playerfilecheck()
    case 2:
        print("You entered the second level")
    case 3:
        print("You entered the third level")
    case _:
        print("You are in an unknown level")