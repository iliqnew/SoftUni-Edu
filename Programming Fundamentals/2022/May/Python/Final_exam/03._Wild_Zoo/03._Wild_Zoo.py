line = input()

areas = []
animals = {}

def add(name, needed_food_quantity, area):
    global animals
    if name in animals:
        animals[name][0] += needed_food_quantity
        return
    animals[name] = [needed_food_quantity, area]
    if area not in areas:
        areas.append(area)

def feed(name, food):
    global animals
    if name not in animals:
        return
    animals[name][0] -= food
    if animals[name][0] <= 0:
        print(f"{name} was successfully fed")
        del animals[name]

while line != "EndDay":
    cmd, args = line.split(": ")
    args = args.split("-")
    if cmd == "Add":
        name, needed_food_quantity, area = args
        add(name, int(needed_food_quantity), area)
    elif cmd == "Feed":
        name, food = args
        feed(name, int(food))
    line = input()

print("Animals:")
for animal in animals:
    name = animal
    needed_food_quantity = animals[animal][0]
    print(f" {name} -> {needed_food_quantity}g")

print("Areas with hungry animals:")
for area in areas:
    count = 0
    for animal in animals:
        if animals[animal][1] == area:
            count += 1
    if count > 0:
        print(f"{area}: {count}")

# Example input:
"""
Add: Adam-4500-ByTheCreek
Add: Maya-7600-WaterfallArea
Add: Maya-1230-WaterfallArea
Feed: Jamie-2000
EndDay

"""

# Example input:
"""
Add: Jamie-600-WaterfallArea
Add: Maya-6570-WaterfallArea
Add: Adam-4500-ByTheCreek
Add: Bobbie-6570-WaterfallArea
Feed: Jamie-2000
Feed: Adam-2000
Feed: Adam-2500
EndDay

"""