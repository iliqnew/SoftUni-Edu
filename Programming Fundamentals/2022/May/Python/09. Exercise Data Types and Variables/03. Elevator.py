n = int(input())
p = int(input())

print(n // p + int(bool(n % p > 0)) * 1)