i = open("input").read().split('\n')

# part 1

class N:
	def __init__(s, x): s.x = x
	__sub__ = lambda s, a: N(s.x * a.x)
	__add__ = lambda s, a: N(s.x + a.x)

s = 0

for l in i:
	for n in range(10):
		n = str(n)
		l = l.replace(n, f"N({n})")

	s += eval(l.replace("*", "-")).x

print("part 1:", s)

# part 2

class M:
	def __init__(s, x): s.x = x
	__mul__ = lambda s, a: M(s.x + a.x)
	__add__ = lambda s, a: M(s.x * a.x)

s = 0

for l in i:
	for n in range(10):
		n = str(n)
		l = l.replace(n, f"M({n})")

	s += eval(l.translate({43:42,42:43})).x

print("part 2:", s)