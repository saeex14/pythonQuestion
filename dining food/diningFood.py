import json
import random

orderFood = {}
dining = []

file = open("dining.txt", "r")
content = file.read()
diningfood = json.loads(content)
file.close()

for key, value in diningfood.items():
    if bool(value) == False:
        dining.append(key)

if len(dining) == 0:
    dining = [key for key in diningfood]
    for key in diningfood:
        diningfood[key] = False


temp = dining[int(random.randint(0, len(dining)) - 1)]

diningfood[temp] = True

print("turn of " + temp)

file = open("dining.txt", "w")
file.write(json.dumps(diningfood))
file.close()