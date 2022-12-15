
def level_up(level: int, xp: int, xp_level: int) -> int:

  if xp >= xp_level:

    level += 1

    xp -= xp_level

    xp_level = int(xp_level * 2)
 
  return level, xp, xp_level


level = 1
xp = 11000000
xp_level = 100
combat = 1
while combat == 1:
  level, xp, xp_level = level_up(level, xp, xp_level)


  print(f"Player's level: {level}")
  print(f"Player's current XP: {xp}")
  print(f"Player's XP needed to reach the next level: {xp_level}")


  player = 100
  new_level = 1
  if level >= new_level:
    new_level = int(new_level + 1)
    player = int(player * 1.1)

  print(player)
  print(new_level)
  if xp_level >= xp:
    break