import random
# variables
hpMonster = 100
attacks = 0
hpUser = 20
maxAttack = 10
# fuctions

#option to attack, heal or run
def option():
    global hpUser
    global hpMonster
    global attacks
    print(hpUser, hpMonster , attacks)
    optionq = input("What do you want to do?")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    optionq = optionq.lower()
    if optionq == "attack":
        print("attack")
        attacks = attacks + 1
        option()
    elif optionq == "run":
        input("Press enter to continue...")
        pass
    elif optionq == "heal":
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print("placeholder text for healing use item here")
        print("you have ", hpUser, "hp")
        hpUser = hpUser + 5
        print("you have ", hpUser, "hp")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        
        option()
        return hpUser


def attackUser():
    global hpUser
    global hpMonster
    global attacks
    global maxAttack
    attackPlayer = random.randint(-1, maxAttack)
    print(attackPlayer)
    hpMonster = hpMonster - attackPlayer
    hpUser = hpUser - 3

# When player interacts, the monster attacks
    # if hpuser <= 0:player dies
    # if hpmonster <= 0:player wins

if __name__ == "__main__":
    attackUser()