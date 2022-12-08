import random

print('''
-=-=-=-=-=-=--=-=-=-=-=-=--=-=-=-=-=-=--=-=-=-=-=-=--=-=-=-=-=-=--=-=-=-=-=-=-
Combat system Timothy
Made on 12/08/2022
HetGameBoekje
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
''')
global hp 
hp = 100
global attack
attack = int(input("How many attacks do you want to do? "))
def random_dmg():
    global dmg
    global hp
    dmg = random.randint(-5, 10)
    if dmg >=1:
        print("You hit!")
        hp = hp - dmg
    else:
        print("You missed!")
    return hp, dmg
    

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