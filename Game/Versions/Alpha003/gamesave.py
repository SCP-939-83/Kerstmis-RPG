import json
import os
my_dir = "Game\Versions\Alpha003"

os.makedirs(my_dir, exist_ok=True)
file_path = os.path.join(my_dir, "my_file.json")

class Person:
    level = 1
    def __init__(self, name, age, city, level , xp):
        self.name = name
        self.age = age
        self.city = city
        self.level = level
        self.xp = xp


def playerfile():
    global age , name , city , level , xp , data , file_path , my_dir
    global my_dict , name , age , city , level , xp
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
    return my_dict , Person.name , Person.age , Person.city , Person.level , Person.xp




def savegame():
    global data , age , name , city , level , xp , data , file_path , my_dir, my_dict
    my_dir = "Game\Versions\Alpha003"
    print("game saved")

    os.makedirs(my_dir, exist_ok=True)

    file_path = os.path.join(my_dict, "my_file.json")

    with open(file_path, "w") as f:
        json.dump(my_dict, f)

    with open("my_file.json", "r+") as f:
        data = json.load(f)
        f.seek(0)

        json.dump(data, f)
    json_object = json.dumps(my_dict, indent = 4) 
    print(json_object)


def loadgame():
    global file_path , age , name , city , level , xp , data , file_path , my_dir
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
    xp = data["xp"]
    print(name, "= name")
    print(age, "= age")
    print(city, "= city")
    print(level, "= level")
    return age , name , city , level , xp , data , file_path , my_dir



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
    playerfilecheck ()
    Person.level += 1
    print(Person.level)
    
    savegame()