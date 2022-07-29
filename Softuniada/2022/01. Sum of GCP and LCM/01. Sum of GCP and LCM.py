def nod(n: int, m: int) -> int:
	return max({i for i in range(n, 0, -1) if n % i == 0} & {i for i in range(m, 0, -1) if m % i == 0})

def nok(n: int, m: int) -> int:
	for i in range(1, n * m + 1):
		if i % n == i % m == 0:
			return i

n = int(input())
m = int(input())

print(nod(n,m) + nok(n,m))