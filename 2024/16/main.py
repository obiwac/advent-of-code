import random

*f, = map(list, open(0).read().strip().split("\n"))

walls = set()
start = None
end = None

for i in range(len(f)):
	for j in range(len(f[i])):
		if f[i][j] == "#":
			walls.add((i, j))

		if f[i][j] == "E":
			end = (i, j)

		if f[i][j] == "S":
			start = (i, j)

assert start is not None
assert end is not None
assert start != end

seats = set()
m_printed = False

for _ in range(20):
	DIRS = ((0, 1), (0, -1), (1, 0), (-1, 0))
	q = [start + (2,)]
	dist = [[[float("inf")] * len(f) for _ in range(len(f[0]))] for _ in range(4)]
	prev: list[list[list[None | tuple]]] = [[[None] * len(f) for _ in range(len(f[0]))] for _ in range(4)]

	for i in range(4):
		dist[i][start[0]][start[1]] = 0

	while q:
		cx, cy, cd = q.pop(0)
		enum = list(enumerate(DIRS))
		random.shuffle(enum)

		for d, (dx, dy) in enum:
			nx, ny = cx + dx, cy + dy
			cost = 1 + (1000 if cd != d else 0)

			if not (0 <= nx < len(f) and 0 <= ny < len(f[0])) or (nx, ny) in walls:
				continue

			if dist[cd][cx][cy] + cost > dist[d][nx][ny]:
				continue

			dist[d][nx][ny] = dist[cd][cx][cy] + cost
			prev[d][nx][ny] = (cx, cy, cd)

			q.append((nx, ny, d))

	m = float("inf")
	di = 0

	for i in range(4):
		d = dist[i][end[0]][end[1]]

		if d < m:
			m = d
			di = i

	assert m != float("inf")

	if not m_printed:
		m_printed = True
		print("Part 1:", m)

	u = end + (di,)

	while u:
		seats.add(u[:2])
		u = prev[u[2]][u[0]][u[1]]

	print("Part 2 candidate:", len(seats))

print("Part 2:", len(seats))
