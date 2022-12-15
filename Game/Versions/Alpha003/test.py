import json
import os

# Define a Python dictionary
name = input("What is your name? ")
age = int(input("How old are you? "))
city = input("Where do you live? ")
my_dict = {
    "name": name,
    "age": age,
    "city": city
}


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
    print(data)

def update():
    my_dir = "Game\Versions\Alpha003"

    # Use the os.makedirs() method to create the directory if it doesn't exist
    os.makedirs(my_dir, exist_ok=True)

    # Use the os.path.join() method to combine the directory and file name
    file_path = os.path.join(my_dir, "my_file.json")

    # Open the file for reading
    with open(file_path, "r") as f:
        # Load the JSON string from the file and convert it to a dictionary
        data = json.load(f)


    # Increase the value of the "age" field
    data["age"] += 1

    # Move the file pointer to the beginning of the file
    f.seek(0)

    # Write the updated dictionary to the file
    json.dump(data, f)

savegame()
loadgame()
update()
loadgame()