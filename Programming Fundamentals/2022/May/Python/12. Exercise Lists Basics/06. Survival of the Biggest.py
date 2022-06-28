ints = [int(i) for i in input().split()]
n = int(input())

for i in range(n):
    ints.remove(min(ints))

print(str(ints)[1:-1])