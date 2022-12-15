
level = 1
xp = 0
skill_points = 0

skills = {
  "HP": 0,
  "Damage": 0,
  "Armor": 0,
  "Charisma": 0,
  "Intelligence": 0
}

def level_up():
  global level, skill_points

  next_level_up_xp = 100 * (level+1)
  

  if xp >= next_level_up_xp:

    level += 1
    skill_points += 1

    print(f"Congratulations! You are now level {level} and have {skill_points} skill points to spend.")
  else:

    print(f"You need {next_level_up_xp} experience points to reach level {level+1}.")

def spend_skill_point():
  global skill_points

  if skill_points > 0:

    print("Which skill do you want to level up?")
    for skill in skills:
      print(f"- {skill} (level {skills[skill]})")
    skill = input("> ")
    

    if skill in skills:

      skills[skill] += 1
      skill_points -= 1

      print(f"You have spent a skill point on {skill}. You have {skill_points} skill points remaining.")
    else:

      print(f"You don't have the skill {skill}.")
  else:

    print("You don't have enough skill points to spend.")

xp += 50
level_up()
xp += 100
level_up()
spend_skill_point()
xp += 350
level_up()
spend_skill_point()