divisor = int(input())
boundary = int(input())

max_value = False
for i in range(1, boundary + 1):
    if i % divisor == 0:
        max_value = i

print(max_value)