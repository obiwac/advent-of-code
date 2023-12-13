*f, = map(lambda x: x.split("\n"), open(0).read().strip().split('\n\n'))
s = 0
no_smudge_s = 0

for i, p in enumerate(f):
	*q, = map(str, p)
	no_smudge = -1

	for x, l in enumerate(q):
		if x == 0: continue

		a = "|".join(q[:x][::-1])
		b = "|".join(q[x:])

		if a.startswith(b) or b.startswith(a):
			no_smudge = x * 100
			break

	if no_smudge == -1:
		*q, = map("".join, zip(*q))

		for x, l in enumerate(q):
			if x == 0: continue

			a = "|".join(q[:x][::-1])
			b = "|".join(q[x:])

			if a.startswith(b) or b.startswith(a):
				no_smudge = x
				break

	no_smudge_s += no_smudge

	for yy in range(len(p)):
		to_break = False

		for xx in range(len(p[yy])):
			*q, = map(list, p)
			q[yy][xx] = "#" if q[yy][xx] == "." else "."
			*q, = map("".join, q)

			pr = []

			for x, l in enumerate(q):
				if x == 0: continue

				a = "|".join(q[:x][::-1])
				b = "|".join(q[x:])

				if a.startswith(b) or b.startswith(a):
					pr.append(x * 100)

			*q, = map("".join, zip(*q))

			for x, l in enumerate(q):
				if x == 0: continue

				a = "|".join(q[:x][::-1])
				b = "|".join(q[x:])

				if a.startswith(b) or b.startswith(a):
					pr.append(x)

			r = -1

			for rr in pr:
				if rr != no_smudge:
					r = rr

			if r != -1:
				s += r
				to_break = True
				break

		if to_break: break

print(no_smudge_s)
print(s)
