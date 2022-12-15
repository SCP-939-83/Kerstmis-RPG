# x = 1
# def start():  
#     status = 1,1
#     global x
#     match status:
#         case 1,1:
#             print(x + x)
#             start()
#             return x


class Persoon:
    level = 1
    hp = 100
    def level_up(self):
        Persoon.level += self
        Persoon.hp += self*10


print(Persoon.level)
print(Persoon.hp)
Persoon.level_up(float(input("hoeveel level wil je levelen? ")))
print("=====")
print(Persoon.level)
print(Persoon.hp)
