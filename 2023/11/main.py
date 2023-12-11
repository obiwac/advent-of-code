*f, = map(list, open(0).read().strip().split('\n'))

of = f
f = []

for row in of:
	f.append(row)

*f, = zip(*f)

of = f
f = []

for row in of:
	f.append(row)

*f, = zip(*f)

galaxies = {}
counter = 1

for y, row in enumerate(f):
	for x, col in enumerate(row):
		if col != "#":
			continue

		galaxies[counter] = (x, y)
		counter += 1

s = 0

for a in range(1, counter):
	for b in range(a + 1, counter):
		ax, ay = galaxies[a]
		bx, by = galaxies[b]

		dist = abs(bx - ax) + abs(by - ay)
		s += dist

print(s)
