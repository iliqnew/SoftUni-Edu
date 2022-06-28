cards = input().split()
shuffles = int(input())

for i in range(shuffles):
    new_cards = []
    l1 = cards[:len(cards)//2]
    l2 = cards[len(cards)//2:]
    for j in range(len(l1)):
        new_cards.append(l1.pop(0))
        new_cards.append(l2.pop(0))
    cards = new_cards

print(cards)