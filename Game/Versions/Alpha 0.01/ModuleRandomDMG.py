import random

print('''
-=-=-=-=-=-=--=-=-=-=-=-=--=-=-=-=-=-=--=-=-=-=-=-=--=-=-=-=-=-=--=-=-=-=-=-=-
Combat system Timothy
Made on 12/08/2022
HetGameBoekje
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
''')
hp = 100
attacks = 0
hpuser = 20
def random_dmg():
    global dmg
    global hp
    dmg = random.randint(-5, 10)
    if dmg >=1:
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print("You hit!")
        print("the monster has", hp, "hp")
        print("You did", dmg, "dmg")
        hp = hp - dmg
        print("Now , the monster has", hp, "hp")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        return hp
    else:
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print("You missed!")
        
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")


def attack():
    global attacks
    global hpuser
    global hp
    random_dmg()
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("You attacked the monster!")
    print("The monster has", hp, "hp")
    print("You did", dmg, "dmg")
    print("Now , the monster has", hp, "hp")
    attacks = attacks + 1
    print(attacks, "attacks dealth")
    print("------------------")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    if hp <= 0:
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print("You won and defeated monster!")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        input("Press enter to continue...")
        pass
    else:
        questionAttack = input("Do you want to attack a monster? (Y/N): ")
        questionAttack = questionAttack.upper()
        if questionAttack == "Y":
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            print("The monster attacked you!")
            hpuser = hpuser - 3
            print ("You have", hpuser, "hp")
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            if hpuser >= 1:
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
                print("You have", hpuser, "hp")
                print("the monster dealth 3 damage")
                print("The monster has", hp, "hp")
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
                attack()
            else:
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
                print("You died")
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
                input("Press enter to exit...")
                # add death screen here , and reset the game.
                exit()
        else:
            option()
    return hp and attacks and hpuser

def option():
    global hpuser 
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("Attack")
    print("Run")
    print("Heal")
    optionq = input("What do you want to do?")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    optionq = optionq.lower()
    if optionq == "attack":
        attack()
    elif optionq == "run":
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print("You ran away")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        input("Press enter to continue...")
    elif optionq == "heal":
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print("placeholder text for healing use item here")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        hpuser = hpuser + 5
        option()
        return hpuser
        
        
    else:
        print(optionq)
        print("You did not enter a valid option")
        input("Press enter to continue...")
        option()


if __name__ == "__main__":
    option()


    # attack = int(input("How many attacks do you want to do? "))
    # for i in range(attack):
    #     print("------------------")
    #     print("Round", i+1)
    #     print("You have", hp, "hp")
    #     random_dmg()
    #     print(hp, "hp")
    #     print(dmg, "dmg")
    #     print("------------------")




        # implentatie van een if statement die zegt dat als hp <= 0 je hebt gewonnen en de code stopt dan, geeft gebruiker 5 gold en 3 xp
        # if hp <= 0:
        #     print("You won and defeated monster!")