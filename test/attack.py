# Import the random module to generate random numbers
import random

# Define the attributes of the player
class Player:
    def __init__(self, name, health, power, armor):
        self.name = name
        self.health = health
        self.power = power
        self.armor = armor

    # Define a method for the player to attack an enemy
    def attack(self, enemy):
        # Generate a random number between 0 and the player's power
        damage = random.randint(0, self.power)
        # Reduce the enemy's health by the amount of damage dealt
        enemy.health -= damage
        print(f"{self.name} deals {damage} damage to {enemy.name}")

    # Define a method to check if the player is alive
    def is_alive(self):
        return self.health > 0

# Define the attributes of the enemy
class Enemy:
    def __init__(self, name, health, power, armor):
        self.name = name
        self.health = health
        self.power = power
        self.armor = armor

    # Define a method for the enemy to attack the player
    def attack(self, player):
        # Generate a random number between 0 and the enemy's power
        damage = random.randint(0, self.power)
        # Reduce the player's health by the amount of damage dealt
        player.health -= damage
        print(f"{self.name} deals {damage} damage to {player.name}")

    # Define a method to check if the enemy is alive
    def is_alive(self):
        return self.health > 0

# Create a player
player = Player("Timo", 100, 20, 10)

# Create an enemy
enemy = Enemy("Martina", 100, 20, 10)

# Print the player and enemy's initial stats
print(f"{player.name} has {player.health} health, {player.power} power, and {player.armor} armor")
print(f"{enemy.name} has {enemy.health} health, {enemy.power} power, and {enemy.armor} armor")

# Loop until one of the characters is dead
while player.is_alive() and enemy.is_alive():
    # Have the player attack the enemy
    player.attack(enemy)

    # If the enemy is still alive, have it attack the player
    if enemy.is_alive():
        enemy.attack(player)

# Print the final stats of the player and enemy
print(f"{player.name} has {player.health} health remaining")
print(f"{enemy.name} has {enemy.health} health remaining")
