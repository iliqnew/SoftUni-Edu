import re

n_of_inputs = int(input())
for i in range(n_of_inputs):
    boss = input()
    pattern = r"\|(?P<name>[A-Z]{4,})\|:#(?P<title>[a-zA-z]+ [a-zA-z]+)#"
    result = re.search(pattern, boss)
    if result:
        name = result.group('name')
        title = result.group('title')
        print(f"{name}, The {title}")
        print(f">> Strength: {len(name)}")
        print(f">> Armor: {len(title)}")
    else:
        print("Access denied!")

# Example input:
"""
3
|PETER|:#Lead architect#
|GEORGE|:#High Overseer#
|ALEX|:#Assistant Game Developer#

"""