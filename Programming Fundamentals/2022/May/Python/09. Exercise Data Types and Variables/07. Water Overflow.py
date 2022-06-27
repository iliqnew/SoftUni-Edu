capacity = 255

n = int(input())
total = 0
for i in range(n):
    liters = int(input())
    if total+liters > capacity:
        print("Insufficient capacity!")
        continue
    total += liters
print(total)