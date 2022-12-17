import json
import os

my_dir = "Game\Versions\Alpha003"

os.makedirs(my_dir, exist_ok=True)
file_path = os.path.join(my_dir, "my_file.json")
def inputuser():
    global name, age, city, level, xp , my_dict
    name = input("What is your name? ")
    age = input("What is your age? ")
    city =  input("What is your city? ")
    level = 1
    xp = 0

    my_dict = {
    "name": name,
    "age": age,
    "city": city,
    "level": level,
    "xp": xp,
}
    savegame()
    return name, age, city, level, xp, my_dict




def savegame():
    my_dict = {
    "name": name,
    "age": age,
    "city": city,
    "level": level,
    "xp": xp,
}
    os.makedirs(my_dir, exist_ok=True)
    file_path = os.path.join(my_dir, "my_file.json")
    print("game saved")
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

    print("game loaded")
    global age , name , city , level
    age = data["age"]
    name = data["name"]
    city = data["city"]
    level = data["level"]
    xp = data["xp"]
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
            inputuser()
            
    
            
if __name__ == "__main__":
    playerfilecheck()
    level += 1
    savegame()
    print("level = ", level)
