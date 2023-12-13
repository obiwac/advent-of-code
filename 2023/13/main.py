*f, = map(lambda x: x.split("\n"), open(0).read().strip().split('\n\n'))
s = 0

for i, p in enumerate(f):
	*q, = map(str, p)
	r = -1

	for x, l in enumerate(q):
		if x == 0: continue

		a = "|".join(q[:x][::-1])
		b = "|".join(q[x:])

		if a.startswith(b) or b.startswith(a):
			r = x * 100
			break

	if r == -1:
		*q, = map("".join, zip(*q))

		for x, l in enumerate(q):
			if x == 0: continue

			a = "|".join(q[:x][::-1])
			b = "|".join(q[x:])

			if a.startswith(b) or b.startswith(a):
				r = x
				break

	s += r

print(s)
