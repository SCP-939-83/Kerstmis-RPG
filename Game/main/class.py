class Game:
    name = input("What is your player's name? ")
    age = input("What is your age? ")
    city =  input("What will you name your city? ")
    level = 1
    savelevel = 1
    xp = 0
    karma = 0
    inventory = []

    def doeIets(Self , naam):
        print(naam)


game = Game()
game2 = Game()
game.name = "Erik"
print(game.name)
game2.name = "Raymond"
print(game2.name)
print(game.name)
game.doeIets("Cara")
game2.doeIets("Max")