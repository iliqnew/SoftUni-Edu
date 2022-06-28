a = [i for i in range(1, 11+1)]
b = [i for i in range(1, 11+1)]

card_sequence = input().split()

terminated = False
for card in card_sequence:
    team, number = card.split("-")
    if team == "A":
        if int(number) in a:
            a.remove(int(number))
    elif team == "B":
        if int(number) in b:
            b.remove(int(number))
    if len(a) < 7 or len(b) < 7:
        terminated = True
        break

print(f"Team A - {len(a)}; Team B - {len(b)}")
if terminated:
    print("Game was terminated")