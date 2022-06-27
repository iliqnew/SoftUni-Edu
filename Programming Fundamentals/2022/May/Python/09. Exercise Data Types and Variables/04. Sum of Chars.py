n = int(input())

s = 0
for i in range(n):
    letter = input()
    s += ord(letter)

print(f"The sum equals: {s}")