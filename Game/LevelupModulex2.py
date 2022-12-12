
def level_up(level: int, xp: int, xp_level: int) -> int:

  if xp >= xp_level:

    level += 1

    xp -= xp_level

    xp_level = int(xp_level * 2)
 
  return level, xp, xp_level
def stats():
  player = 100
  new_level = 1
  armor = 5
  damage = 5
  poison = 10
  fire = 10
  while level >= new_level:
    new_level = int(new_level + 1)
    print("Health points(HP), Armor(A), Damage(D), Poison(P), Fire(F)")
    keuze = input('Wat is je keuze? ')  
    if keuze == ("HP"):
        player = (player * 1.1)
    elif keuze == ("A"):
        armor = (armor * 1.1)
    elif keuze == ("D"):
        damage = (damage * 1.1)
    elif keuze == ("P"):
        poison = (poison * 1.1)
    elif keuze == ("F"):
        fire = (fire * 1.1)
        return player, new_level, armor, damage, poison, fire, keuze
    



level = 1
xp = 11000000
xp_level = 100

while xp >= xp_level:
  level, xp, xp_level = level_up(level, xp, xp_level)
  player, new_level, armor, damage, poison, fire, keuze = stats()
  print(f"Player's level:", level)
  print(f"Player's current XP:", xp)
  print(f"Player's XP needed to reach the next level:", xp_level)
  print(f"Next level:",new_level)
  print(f"HP:",player)
  print(f"armor:",armor)
  print(f"damage:",damage)
  print(f"poison damage:",poison)
  print(f"fire damage:",fire)
