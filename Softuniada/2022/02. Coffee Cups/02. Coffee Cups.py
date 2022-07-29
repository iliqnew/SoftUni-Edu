n = int(input())
name = input().upper()

w = 3 * n + 6
h = 3 * n + 1

# steam
for i in range(n):
    print(" " * n + "~ ~ ~")
# name
print("=" * (w - 1))
for i in range(n - 2):
    if i == n // 2 - 1:
        print("|" + "~" * n + name + "~" * n + "|" + " " * (n-1) + "|")
        continue
    print("|" + "~" * (2 * n + len(name)) + "|" + " " * (n-1) + "|")
print("=" * (w - 1))
# coffee
for i in range(n):
    print(" " * i + "\\" + "@" * (2 * (n - i) + len(name)) + "/")
# table top
print("-" * (w - 1))