import random
inventory = []
def itemgen():
    z = random.randint(1, 1000)
    global inventory
    if z >= 1 and z <= 5:
        loot = ("\033[1;31m apple ")
        inventory.append("apple")
    elif z >= 6 and z <= 25:
        loot = ("\033[1;33m mushroom ")
        inventory.append("mushroom")
    elif z >= 26 and z <= 75:
        loot = ("\033[1;35m flower ")
        inventory.append("flower")
    elif z >= 76 and z <= 200:
        loot = ("\033[1;34m potato ")
        inventory.append("potato")
    elif z >= 201 and z <= 500:
        loot = ("\033[1;32m rock ")
        inventory.append("rock")
    elif z >= 501 and z <= 1000:
        loot = ("\033[1;0m stick ")
        inventory.append("stick")
    print("\033[1;0m Je hebt een" + loot + "\033[1;0mitem gekregen!!")
    return inventory

if __name__ == "__main__":
    while True:
        try:
            integer = int(input("Hoeveel items wil je hebben?: "))
        except ValueError:
            print("Vul een getal in, geen letters of tekens!")
            continue
        else:
            print(f'Je vulde dit getal in: {integer}')
            break

    for i in range(integer):
        itemgen()


    stick = inventory.count("stick") 
    rock = inventory.count("rock")
    potato = inventory.count("potato")
    flower = inventory.count("flower")
    mushroom = inventory.count("mushroom")
    apple = inventory.count("apple")

    y = len(inventory)
    print(stick, "sticks")
    print(rock, "rocks")
    print(potato, "potatoes")
    print(flower, "flowers")
    print(mushroom, "mushrooms")
    print(apple, "apples")
    print(y, "total items")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    inventory.sort()
    inventory.reverse()
    print(inventory)

    # z = random.randint(1, 1000)
    # if z >= 1 and z <= 1000: loot = ("\033[1;31m mythical ")

