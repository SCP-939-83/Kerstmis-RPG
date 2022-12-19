import turtle

# create a turtle object
my_turtle = turtle.Turtle()

# set the turtle's shape
my_turtle.shape("turtle")

# set the turtle's pen color
my_turtle.pencolor("green")

# set the turtle's speed
my_turtle.speed(0)

# move the turtle to the top of the screen
my_turtle.penup()
my_turtle.sety(200)
my_turtle.pendown()

# write the title of the menu
my_turtle.write("Skill Menu", align="center", font=("Arial", 24, "bold"))

# move the turtle down
my_turtle.penup()
my_turtle.sety(-100)
my_turtle.pendown()

# write the skills
level = 1337
turtle.title(level)
my_turtle.write("HP: 0", align="center", font=("Arial", 16))
my_turtle.penup()
my_turtle.sety(-125)
my_turtle.pendown()
my_turtle.write("Damage: 0", align="center", font=("Arial", 16))
my_turtle.penup()
my_turtle.sety(-150)
my_turtle.pendown()
my_turtle.write("Armor: 0", align="center", font=("Arial", 16))
my_turtle.penup()
my_turtle.sety(-175)
my_turtle.pendown()
my_turtle.write("Charisma: 0", align="center", font=("Arial", 16))
my_turtle.penup()
my_turtle.sety(-200)
my_turtle.pendown()
my_turtle.write("Intelligence: 0", align="center", font=("Arial", 16))

# hide the turtle
my_turtle.hideturtle()

# keep the window open until the user closes it
turtle.mainloop()




level = 1
xp = 200
skill_points = 0

BASE_HP = 100
HP_PER_LEVEL = 10

BASE_DAMAGE = 10
DAMAGE_PER_LEVEL = 5

BASE_ARMOR = 0
ARMOR_PER_LEVEL = 2

BASE_CHARISMA = 0
CHARISMA_PER_LEVEL = 1

BASE_INTELLIGENCE = 0
INTELLIGENCE_PER_LEVEL = 1

skills = {
  "HP": 0,
  "Damage": 0,
  "Armor": 0,
  "Charisma": 0,
  "Intelligence": 0
}

def level_up():
  global level, skill_points, next_level_up_xp

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
      if skill == "HP":
        print("You have gained 10 HP")
      elif skill == "Damage":
        print("You have gained 1 Damage")
      elif skill == "Armor":
        print("You have gained 10 Armor")
      elif skill == "Charisma":
        print("You have gained 1 Charisma")
      elif skill == "Intelligence":
        print("You have gained 1 Intelligence")
    else:

      print(f"You don't have the skill {skill}.")
  else:

    print("You don't have enough skill points to spend.")

level_up()
spend_skill_point()

total_hp = BASE_HP + HP_PER_LEVEL * skills["HP"]
total_damage = BASE_DAMAGE + DAMAGE_PER_LEVEL * skills["Damage"]
total_armor = BASE_ARMOR + ARMOR_PER_LEVEL * skills["Armor"]
total_charisma = BASE_CHARISMA + CHARISMA_PER_LEVEL * skills["Charisma"]
total_intelligence = BASE_INTELLIGENCE + INTELLIGENCE_PER_LEVEL * skills["Intelligence"]

print(f"Total HP: {total_hp}")
print(f"Total Damage: {total_damage}")
print(f"Total Armor: {total_armor}")
print(f"Total Charisma: {total_charisma}")
print(f"Total Intelligence: {total_intelligence}")
