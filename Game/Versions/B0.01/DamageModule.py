import random
import FightModule
import ModuleRandomINV
import ModuleLocation 
import LevelupModule

def monster_stats(player_level):
  global min_hp, max_hp, monster_hp, min_damage, max_damage, monster_hp
  min_hp = player_level * 8
  max_hp = player_level * 12
  
  # Calculate the monster's hit points within the range
  monster_hp = random.randint(min_hp, max_hp)
  
  # Calculate the minimum and maximum damage values for the monster
  min_damage = random.randint(3,6) * player_level 
  max_damage = random.randint(6,9) * player_level + (5*3.13141)
  
  return monster_hp, min_damage, max_damage

# Test the function with a player level of 5
monster_hp, min_damage, max_damage = monster_stats(LevelupModule.level)

print("Monster HP:", monster_hp)
print("Monster Damage Range:", min_damage, "to", max_damage)

