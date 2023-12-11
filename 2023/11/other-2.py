*f, = map(list, open(0).read().strip().split('\n'))
size = 999999

pockets_y = []

for i, row in enumerate(f):
	if all(x == "." for x in row):
		pockets_y.append(i)

pockets_x = []

for i, col in enumerate(zip(*f)):
	if all(x == "." for x in col):
		pockets_x.append(i)

galaxies = {}
counter = 1

for y, row in enumerate(f):
	for x, col in enumerate(row):
		if col != "#":
			continue

		nx = x
		ny = y

		for px in pockets_x:
			if x >= px:
				nx += size

		for py in pockets_y:
			if y >= py:
				ny += size

		galaxies[counter] = (nx, ny)
		counter += 1

s = 0

for a in range(1, counter):
	for b in range(a + 1, counter):
		ax, ay = galaxies[a]
		bx, by = galaxies[b]

		dist = abs(bx - ax) + abs(by - ay)
		s += dist

print(s)
