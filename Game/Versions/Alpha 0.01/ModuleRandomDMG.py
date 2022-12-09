import random

print('''
-=-=-=-=-=-=--=-=-=-=-=-=--=-=-=-=-=-=--=-=-=-=-=-=--=-=-=-=-=-=--=-=-=-=-=-=-
Combat system Timothy
Made on 12/08/2022
HetGameBoekje
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
''')

def random_dmg():
    global dmg
    global hp
    hp = 100
    dmg = random.randint(-5, 10)
    if dmg >=1:
        print("You hit!")
        print("the monster has", hp, "hp")
        print("You did", dmg, "dmg")
        hp = hp - dmg
        print("Now , the monster has", hp, "hp")
        return hp, dmg
    else:
        print("You missed!")
    
    
if __name__ == "__main__":
    attack = int(input("How many attacks do you want to do? "))
    for i in range(attack):
        print("------------------")
        print("Round", i+1)
        print("You have", hp, "hp")
        random_dmg()
        print(hp, "hp")
        print(dmg, "dmg")
        print("------------------")
        # implentatie van een if statement die zegt dat als hp <= 0 je hebt gewonnen en de code stopt dan, geeft gebruiker 5 gold en 3 xp
        # if hp <= 0:
        #     print("You won and defeated monster!")