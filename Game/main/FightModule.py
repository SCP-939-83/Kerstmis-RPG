import random
import time
import LevelupModule
# variables
hpMonster = 20
attacks = 0
hpUser = 20
maxAttackDamage = 10
attackAmount = 0
monsterHeal = 0
monster_hp = 20
max_damageplayer = 10
min_damageplayer = 1
karma = 0
battle_result = "lose"
# fuctions

#option to attack, heal or run
def monster_stats(player_level):
  global min_hp, max_hp, monster_hp, min_damage, max_damage, monster_hp
  min_hp = player_level * 8
  max_hp = player_level * 12
  
  # Calculate the monster's hit points within the range
  monster_hp = random.randint(min_hp, max_hp)
  
  # Calculate the minimum and maximum damage values for the monster
  min_damage = random.randint(3,6) * player_level
  max_damage = random.randint(6,9) * player_level + (5)
  return monster_hp, min_damage, max_damage
monster_stats(10)
print("Monster HP:", monster_hp)
print("Monster Damage Range:", min_damage, "to", max_damage)
def option():
    global hpUser
    global monster_hp
    global attacks
    global min_damage, max_damage
    global attackAmount
    if monster_hp <= 1:
        print("You have won. You attacked", attacks, "times")
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
        elif optionq == "heal": # player heals itself with a random int between 3-6 and monster has a chance to attack or heal it self with random int, and if int is 1-3 it heals, if 4-10 it strikes back
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
            print("Invalid option")
            option()


def attackUser():
    global hpUser
    global monster_hp
    global attacks
    global max_damageplayer, min_damageplayer
    global attackAmount
    attackPlayer = random.randint(min_damageplayer, max_damageplayer)
    print(attackPlayer, "attackplayer damage")
    if hpUser >= 1:
        hpUser = hpUser - random.randint(1,3)
        pass
    else:
        print("You died")
        exit()
    print("You got hurt, opponent dealt some damage")
    print("you have ", hpUser, "hp")
    if monster_hp >= 1:
        if attackPlayer >= 1:
            monster_hp = monster_hp - attackPlayer
            print("You dealt ", attackPlayer, "damage")
            print("Opponent has ", monster_hp, "hp")
            attackAmount = attackAmount + 1
            print("You have attacked ", attackAmount, "times")
        else:
            print("You missed")
            monster_hp = monster_hp + monsterHeal
            print("Opponent healed ", monsterHeal, " hp. The opponenet has ", monster_hp, "hp")
    else :
        print("You won")
        exit()


Hpuser = 100
playermax_damage = 10
playermin_damage = 5
playerminheal = 4
playermaxheal = 8
hpdrunk = 200
drunkmax_damage = 7
drunkmin_damage = 1
def drunk():
    global Hpuser, hpdrunk, drunkmax_damage, drunkmin_damage, playermax_damage, playermin_damage, playermaxheal, playerminheal 
    print("You have ", Hpuser, "hp")
    print("The drunk has ", hpdrunk, "hp")
    time.sleep(1)
    if Hpuser >= 1:
        drunkdamage = random.randint(drunkmin_damage, drunkmax_damage)
        Hpuser = Hpuser - drunkdamage
        print("You got hurt, opponent dealt" , drunkdamage, "damage")
        choice = input("do you want to attack or heal?")
        if choice == "attack":
            playerdamage = random.randint(min_damageplayer, max_damageplayer)
            hpdrunk = hpdrunk - playerdamage
            print("You dealt ", playerdamage, "damage")
            print("Opponent has ", hpdrunk, "hp")
            drunk()
            return hpdrunk, hpUser
        elif choice == "heal":
            playerheal = random.randint(playerminheal, playermaxheal)
            Hpuser = Hpuser + playerheal
            print("You have healed up to ", Hpuser, "hp")
            drunk()
            return Hpuser, hpdrunk
            
        else:
            print("Invalid option")
            drunk()

    else:
        print("You died")
        exit()
    if hpdrunk <=1:
        print("You won")
        exit()
    return Hpuser, hpdrunk, drunkmax_damage, drunkmin_damage, playermax_damage, playermin_damage, playermaxheal, playerminheal 
    
def monsterAttack():
    global hpMonster
    global hpUser
    global monsterHeal
    monsterHeal = random.randint(4,10)
    monsterchoice = random.randint(1,2)
    damage_monster = random.randint(min_damage, max_damage)
    if monsterchoice == 1:
        print("Opponent healed ", monsterHeal, " hp. The opponenet has ", monster_hp, "hp")
    else:
        print("Opponent dealt ", damage_monster, " damage. The opponent has ", monster_hp, "hp")
        hpUser = hpUser - damage_monster
        print("You got hurt, opponent dealt some damage")
        print("you have ", hpUser, "hp")
    return monsterHeal, monsterchoice, damage_monster

def Endbattle():
    global battle_result
    print("COpy fIghT module to here")
    battle_result = input("Did you win or lose?")
    return battle_result
if __name__ == "__main__":
    option()


