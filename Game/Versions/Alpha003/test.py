import json
import os

# Define a Python dictionary


class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city


def playerfile():
    global my_dict
    Person.name = input("name:")
    Person.age = int(input("age:"))
    Person.city = input("city:")
    my_dict = {
        "name": Person.name,
        "age": Person.age,
        "city": Person.city
    }
    return my_dict




def savegame():
    global data
    # Define the directory where the file should be saved
    my_dir = "Game\Versions\Alpha003"

    # Use the os.makedirs() method to create the directory if it doesn't exist
    os.makedirs(my_dir, exist_ok=True)

    # Use the os.path.join() method to combine the directory and file name
    file_path = os.path.join(my_dir, "my_file.json")

    # Open the file for writing, and write the JSON string to the file
    with open(file_path, "w") as f:
        json.dump(my_dict, f)

    # Open the JSON file for reading and writing
    with open("my_file.json", "r+") as f:
        # Load the JSON string from the file
        data = json.load(f)
        # Move the file pointer to the beginning of the file
        f.seek(0)

        # Write the updated dictionary to the file
        json.dump(data, f)


def loadgame():
    my_dir = "Game\Versions\Alpha003"

    # Use the os.makedirs() method to create the directory if it doesn't exist
    os.makedirs(my_dir, exist_ok=True)

    # Use the os.path.join() method to combine the directory and file name
    file_path = os.path.join(my_dir, "my_file.json")

    # Open the file for reading
    with open(file_path, "r") as f:
        # Load the JSON string from the file and convert it to a dictionary
        data = json.load(f)

    # Print the contents of the dictionary
    print(data["age"])
    global age , name , city
    age = data["age"]
    name = data["name"]
    city = data["city"]
    print(name, age , city, "Are you sure you want to load this game?")


