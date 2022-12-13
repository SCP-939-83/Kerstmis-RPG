# Alpha version 0.01
# creation date = 12-09-2022
# last update = 12-09-2022
# author = @HetGameBoekje

import ModuleRandomDMG
import ModuleLocation
import ModuleRandomINV
questionAttack = input("Do you want to fight a monster? (Y/N): ")
questionAttack = questionAttack.upper()
if questionAttack == "Y":
    attack = 0
    while ModuleRandomDMG.hp > 0:
        ModuleRandomDMG.random_dmg()
        print("You attacked the monster!")
        print("The monster has", ModuleRandomDMG.hp, "hp")
        print("You did", ModuleRandomDMG.dmg, "dmg")
        print("Now , the monster has", ModuleRandomDMG.hp, "hp")
        attack = attack + 1
        print(attack, "attacks dealth")
        print("------------------")
        if ModuleRandomDMG.hp <= 0:
            print("You won and defeated monster!")
            pass
    input("Press enter to continue...")
else:
    print("You did not fight the monster")
    input("Press enter to continue...")



# while True and ModuleLocation.location == "Forest":
#     if ModuleRandomDMG.hp <= 0:
#         print("You won and defeated monster!")
#         ModuleRandomINV.gold = ModuleRandomINV.gold + 5
#         ModuleRandomINV.xp = ModuleRandomINV.xp + 3
#         break
#     else:
#         ModuleRandomDMG.random_dmg()


import random

# variables
hp_monster = 20
attacks = 0
hp_user = 20
max_attack_damage = 10
attack_amount = 0
monster_heal = 0

# option to attack, heal or run
def option():
    global hp_user
    global hp_monster
    global attacks
    global max_attack_damage
    global attack_amount
    print(hp_user, hp_monster, attacks)
    if hp_monster <= 1:
        print("You have won. You attacked", attacks, "times")
        pass
    elif hp_user <= 1:
        print("You have died")
        exit()
    else:
        optionq = input("What do you want to do?")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        optionq = optionq.lower()
        if optionq == "attack":
            print("attack")
            attacks = attacks + 1
            attack_user()
            option()
        elif optionq == "run":
            input("Press enter to continue...")
            pass
        elif optionq == "heal": # player heals itself with a random int between 3-6 and monster has a chance to attack or heal it self with random int, and if int is 1-3 it heals, if 4-10 it strikes back
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            print("placeholder text for healing use item here")
            print("you have ", hp_user, "hp")
            hp_user = hp_user + random.randint(5,10)
            print("you have healed up to ", hp_user, "hp")
            monster_attack()
            # monster has a chance to attack or heal it self with random int, and if int is 1-3 it heals, if 4-10 it strikes back
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            option()
            return hp_user
        else:
            print("Invalid option")
            option()

# RPG Fighting Module

# Define player class
class Player:
  def __init__(self, name, max_health, attack, defense):
    self.name = name
    self.max_health = max_health
    self.current_health = max_health
    self.attack = attack
    self.defense = defense
  
  # Define attack method
  def attack(self, enemy):
    damage = self.attack - enemy.defense
    enemy.current_health -= damage
    print(f"{self.name} attacked {enemy.name} for {damage} damage")

# Define enemy class
class Enemy:
  def __init__(self, name, max_health, attack, defense):
    self.name = name
    self.max_health = max_health
    self.current_health = max_health
    self.attack = attack
    self.defense = defense

# Create player and enemy instances
player = Player("Bob", 100, 20, 10)
enemy = Enemy("Goblin", 50, 15, 5)

# Initiate fight
while player.current_health > 0 and enemy.current_health > 0:
  player.attack(enemy)
  enemy.attack(player)

# Print outcome
if player.current_health > 0:
  print(f"{player.name} has defeated {enemy.name}!")
else:
  print(f"{player.name} has been defeated by {enemy.name}.")
