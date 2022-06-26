price_ratings = [int(i) for i in input().split(", ")]
entry_point = int(input())
type_of_items = input()

entry_point_number = price_ratings[entry_point]
if type_of_items == "cheap":
    left = sum([i for i in price_ratings[:entry_point] if i < entry_point_number])
    right = sum([i for i in price_ratings[entry_point+1:] if i < entry_point_number])

elif type_of_items == "expensive":
    left = sum([i for i in price_ratings[:entry_point] if i >= entry_point_number])
    right = sum([i for i in price_ratings[entry_point+1:] if i >= entry_point_number])

if left >= right:
    print(f"Left - {left}")
else:
    print(f"Right - {right}")
