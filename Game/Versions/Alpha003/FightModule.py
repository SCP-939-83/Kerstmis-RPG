import random
import ModuleRandomINV
# variables

hpMonster = 3
attacks = 0
hpUser = 20
maxAttackDamage = 10
attackAmount = 0
monsterHeal = 0
karma = 0
# fuctions

#option to attack, heal or run
def option():
    global hpUser , hpMonster , attacks , maxAttackDamage , attackAmount , monsterHeal , karma
    print(hpUser, hpMonster , attacks)
    if hpMonster <= 1:
        print("You have won. You attacked", attacks, "times")
        karma += 1
        print(karma)
        hpMonster = 3
        attacks = 0
        maxAttackDamage = 10
        attackAmount = 0
        monsterHeal = 0
        ModuleRandomINV.itemgen()
        pass
    elif hpUser <= 1:
        print("You have died")
        exit()
    else :
        optionq = input("What do you want to do?")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        optionq = optionq.lower()
        if optionq == "attack":
            print("attack")
            attacks += 1
            attackUser()
            option()
        elif optionq == "run":
            input("Press enter to continue...")
            pass
        elif optionq == "heal" and hpUser <= 30: # player heals itself with a random int between 3-6 and monster has a chance to attack or heal it self with random int, and if int is 1-3 it heals, if 4-10 it strikes back
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            print("placeholder text for healing use item here")
            print("you have ", hpUser, "hp")
            hpUser = hpUser + random.randint(5,10)
            print("you have healed up to ", hpUser, "hp")
            monsterAttack()
            # monster has a chance to attack or heal it self with random int, and if int is 1-3 it heals, if 4-10 it strikes back
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            option()
            return hpUser
        else:
            print("You cannot do that")
            option()
    return hpMonster , attacks , hpUser , maxAttackDamage , attackAmount , monsterHeal , karma

def attackUser():
    global hpUser
    global hpMonster
    global attacks
    global maxAttackDamage
    global attackAmount
    attackPlayer = random.randint(-5, maxAttackDamage)
    print(attackPlayer, "attackplayer damage")
    if hpUser >= 1:
        hpUser = hpUser - random.randint(1,3)
        pass
    else:
        print("You died")
        exit()
    print("You got hurt, opponent dealt some damage")
    print("you have ", hpUser, "hp")
    if hpMonster >= 1:
        if attackPlayer >= 1:
            hpMonster = hpMonster - attackPlayer
            print("You dealt ", attackPlayer, "damage")
            print("Opponent has ", hpMonster, "hp")
            attackAmount = attackAmount + 1
            print("You have attacked ", attackAmount, "times")
        else:
            print("You missed")
            if hpMonster <= 30:
                hpMonster = hpMonster + monsterHeal
            else: 
                print("Opponent has ", hpMonster, "hp")
                print("Opponent tried to heal but it is at max hp")
            print("Opponent healed ", monsterHeal, " hp. The opponenet has ", hpMonster, "hp")
    else :
        print("The developer doesn't know how you got here but you won")
        print("You attacked", attacks, "times")
        print("You have won, i guess")
        print(hpUser, hpMonster , attacks)
        pass

def monsterAttack():
    global hpMonster
    global hpUser
    global monsterHeal
    monsterHeal = random.randint(4,7)
    monsterAttackHeal = random.randint(1,10)
    if monsterAttackHeal <= 3 and hpMonster <= 30:
        print("Opponent healed ", monsterHeal, " hp. The opponenet has ", hpMonster, "hp")
    else:
        print("Opponent dealt ", monsterHeal, " damage. The opponent has ", hpMonster, "hp")
        hpUser = hpUser - monsterHeal
        print("You got hurt, opponent dealt some damage")
        print("you have ", hpUser, "hp")



if __name__ == "__main__":
    option()


