# import json

# # Define a Python dictionary
# my_dict = {
#     "name": "John Smith",
#     "age": 35,
#     "city": "New York"
# }

# # Open a file for writing
# with open("my_file.json", "w") as f:
#     # Write the JSON string to the file
#     json.dump(my_dict, f)

# for i in my_dict:
#     print(my_dict[i])


import json
import os

# Define a Python dictionary
my_dict = {
    "name": "John Smith",
    "age": 35,
    "city": "New York"
}

# Define the directory where the file should be saved
my_dir = "\GitHub\Kerstmis-RPG\Game\Versions\Alpha 0.0.3"

# Use the os.path.join() method to combine the directory and file name
file_path = os.path.join(my_dir, "my_file.json")

# Open the file for writing
with open(file_path, "w") as f:
    # Write the JSON string to the file
    json.dump(my_dict, f)

# Define a Python dictionary
my_file = {
    "name": "John Smith",
    "age": 35,
    "city": "New York"
}

# Convert the dictionary to a JSON string
json_string = json.dumps(my_file)

# Print the JSON string
print(json_string)

# Open a file for writing
with open("my_file.json", "w") as f:
    # Write the JSON string to the file
    json.dump(my_file, f)

# Open the JSON file for reading and writing
with open("my_file.json", "r+") as f:
    # Load the JSON string from the file
    data = json.load(f)

    # Increase the value of the "age" field
    data["age"] += 1

    # Move the file pointer to the beginning of the file
    f.seek(0)

    # Write the updated dictionary to the file
    json.dump(data, f)

print(json_string)
