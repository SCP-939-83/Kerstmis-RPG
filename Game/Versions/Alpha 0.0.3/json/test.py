import json
with open("test.json") as f:
    test = json.load(f)

for i in test:
    print(test[i])

    