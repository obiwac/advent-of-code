from functools import cache

f = open(0).read().strip().split("\n")
*a, = map(int, f[0].split())

@cache
def g(x, i = 0):
	if i == 25:
		return 1

	if x == 0:
		return g(1, i + 1)

	elif len(str(x)) % 2 == 0:
		l = int(str(x)[:len(str(x)) // 2])
		r = int(str(x)[len(str(x)) // 2:])

		return g(l, i + 1) + g(r, i + 1)

	return g(x * 2024, i + 1)

print(sum(g(x) for x in a))
