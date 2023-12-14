*f, = map(list, open(0).read().strip().split('\n'))

for y, l in enumerate(f):
	for x, c in enumerate(l):
		if c != 'O':
			continue

		f[y][x] = "."

		v = False
		for yy in range(y - 1, -1, -1):
			if f[yy][x] in "#O":
				f[yy + 1][x] = "O"
				v = True
				break
		if not v: f[0][x] = "O"

s = 0

for y, l in enumerate(f):
	score = len(f) - y
	# print("".join(l))
	s += "".join(l).count("O") * score

print(s)
