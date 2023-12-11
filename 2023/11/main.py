from copy import deepcopy

*f, = map(list, open(0).read().strip().split('\n'))
nf = deepcopy(f) # no expansion

of = f
f = []

for row in of:
	if all(x == "." for x in row):
		f.append(row)

	f.append(row)

*f, = zip(*f)

of = f
f = []

for row in of:
	if all(x == "." for x in row):
		f.append(row)

	f.append(row)

*f, = zip(*f)

def dist_sum(f):
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

	return s

no_expanded_dist = dist_sum(nf)
expanded_dist = dist_sum(f)

print(expanded_dist)

delta = expanded_dist - no_expanded_dist
print(no_expanded_dist + delta * 999999)
