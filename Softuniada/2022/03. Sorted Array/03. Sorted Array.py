l = int(input())
arr = [int(n) for n in input().split()]

for i in range(0, l - 1):
    if i % 2 == 0:
        arr[i], arr[i + 1] = sorted([arr[i], arr[i + 1]], reverse=True)
        continue
    arr[i], arr[i + 1] = sorted([arr[i], arr[i + 1]])

print(" ".join([str(n) for n in arr]))
