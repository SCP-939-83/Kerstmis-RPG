import random
randomencounter = []
def enemygen():
    z = random.randint(1, 1000)
    global randomencounter
    global enemy
    enemy6 = 1 
    if z >= 1 and z <= 5:
        enemy = ("\033[1;31m enemy1 ")
        randomencounter.append("enemy1")
    elif z >= 6 and z <= 25:
        enemy = ("\033[1;33m enemy2 ")
        randomencounter.append("enemy2")
    elif z >= 0 and z <= 200:
        enemy = ("\033[1;35m enemy3 ")
        randomencounter.append("enemy3")
    elif z >= 201 and z <= 500:
        enemy = ("\033[1;34m enemy4 ")
        randomencounter.append("enemy4")
    elif z >= 501 and z <= 700:
        enemy = ("\033[1;32m enemy5 ")
        randomencounter.append("enemy5")
    elif z >= 701 and z <= 1000:
        enemy = ("\033[1;0m", enemy6)
        randomencounter.append("enemy6")
    print("\033[1;0m", enemy + "\033[1;0m heeft je aangevallen!!")
    return randomencounter, enemy
def enemyrandom():
    if enemy == "enemy6":
        print("duck")
for i in range(100):
    enemygen()


