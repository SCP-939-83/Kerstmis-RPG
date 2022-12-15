import json

with open("save.json") as f:
    save = json.load(f)

for save in save["block "]:
    print(save["block"])