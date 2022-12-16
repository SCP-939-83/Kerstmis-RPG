import json
import os
my_dir = "Game\Versions\Alpha003"

os.makedirs(my_dir, exist_ok=True)
file_path = os.path.join(my_dir, "my_file.json")

class Person:
    def __init__(self, name, age, city, level , xp):
        self.name = name
        self.age = age
        self.city = city
        self.level = level
        self.xp = xp


def playerfile():
    global my_dict
    Person.name = input("name:")
    Person.age = int(input("age:"))
    Person.city = input("city:")
    Person.level = 1
    Person.xp = 0
    my_dict = {
        "name": Person.name,
        "age": Person.age,
        "city": Person.city,
        "level" : Person.level,
        "xp" : Person.xp,
    }
    return my_dict




def savegame():
    global data
    my_dir = "Game\Versions\Alpha003"

    os.makedirs(my_dir, exist_ok=True)

    file_path = os.path.join(my_dir, "my_file.json")

    with open(file_path, "w") as f:
        json.dump(my_dict, f)

    with open("my_file.json", "r+") as f:
        data = json.load(f)
        f.seek(0)

        json.dump(data, f)


def loadgame():
    global file_path
    my_dir = "Game\Versions\Alpha003"

    os.makedirs(my_dir, exist_ok=True)

    file_path = os.path.join(my_dir, "my_file.json")

    with open(file_path, "r") as f:
        data = json.load(f)

    print(data["age"])
    global age , name , city , level
    age = data["age"]
    name = data["name"]
    city = data["city"]
    level = data["level"]
    print(name, "= name")
    print(age, "= age")
    print(city, "= city")
    print(level, "= level")
print(file_path)

def playerfilecheck():
    
    with open("Game\Versions\Alpha003\my_file.json", "r+") as f:
        try:
            json_data = json.load(f)
            f.seek(0)
            json.dump(json_data, f)
            print("File is not empty!")
            loadgame()
            
            pass
        except ValueError:
            print("Empty File!")
            playerfile()
            savegame()
            
    
            

if __name__ == "__main__":
    playerfilecheck()
