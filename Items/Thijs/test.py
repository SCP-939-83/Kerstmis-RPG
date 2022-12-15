# define a dictionary that maps stat names to their current levels
stats = {
    "HP": 10,
    "strength": 1,
    "intelligence": 1,   
    "charisma": 1,
    "armor": 1,
}
level = 1
xp = 11000000
xp_level = 1000
def level_up(level: int, xp: int, xp_level: int) -> int:
  if xp >= xp_level:

    level += 1

    xp -= xp_level

    xp_level = int(xp_level * 2)
 
  return level, xp, xp_level


def Levelup():
      new_level = 1
      new_level = int(new_level + 1)
      print("Current stats:")
      for stat, level in stats.items():
          print(f"{stat}: {level}")

      stat_to_level_up = input("Enter the name of the stat you want to level up: ")


      if stat_to_level_up in stats:

            stats[stat_to_level_up] += 1

            print("Updated stats:")
            for stat, level in stats.items():
                print(f"{stat}: {level}")
                print (level)
                print (new_level)
      else:
            print("Invalid stat name. Please try again.")
            return new_level, level 
new_level = 1
while level == new_level:
  level_up(level, xp, xp_level)
  Levelup()

