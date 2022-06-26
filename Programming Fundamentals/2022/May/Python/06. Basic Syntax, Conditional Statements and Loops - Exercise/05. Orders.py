import random

n = int(input())

total = 0
for i in range(n):
    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())
    if not (0.01 <= price_per_capsule <= 100):
        continue
    if not (1 <= days <= 31):
        continue
    if not (1 <= capsules_per_day <= 2000):
        continue
    total_price = price_per_capsule * days * capsules_per_day
    print(f"The price for the coffee is: ${total_price:.2f}")
    total += total_price

print(f"Total: ${total:.2f}")
