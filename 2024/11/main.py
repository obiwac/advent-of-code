from functools import cache

f = open(0).read().strip().split("\n")
*a, = map(int, f[0].split())

@cache
def g(x, o, i = 0):
	if i == o:
		return 1

	if x == 0:
		return g(1, o, i + 1)

	elif len(str(x)) % 2 == 0:
		l = int(str(x)[:len(str(x)) // 2])
		r = int(str(x)[len(str(x)) // 2:])

		return g(l, o, i + 1) + g(r, o, i + 1)

	return g(x * 2024, o, i + 1)

print(sum(g(x, 25) for x in a))
print(sum(g(x, 75) for x in a))
