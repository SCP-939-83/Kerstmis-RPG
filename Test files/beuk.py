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
