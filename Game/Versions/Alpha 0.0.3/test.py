import json
with open("save.json") as f:
    save = json.load(f)

for i in save:
    print(save[i])

    