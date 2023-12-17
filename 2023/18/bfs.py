*f, = map(str, open(0).read().strip().split('\n'))

m = {(0, 0): True}
x, y = 0, 0

DIRS = {
	"R": (1, 0),
	"L": (-1, 0),
	"U": (0, -1),
	"D": (0, 1),
}

for r in f:
	d, l, c = r.split()
	dx, dy = DIRS[d]

	for _ in range(int(l)):
		x += dx
		y += dy
		m[(x, y)] = True

q = [(1, 1)]
visited = set()

while q:
	cx, cy = q.pop(0)

	for dx, dy in DIRS.values():
		nx, ny = cx + dx, cy + dy

		if (nx, ny) in visited:
			continue

		if (nx, ny) not in m:
			q.append((nx, ny))
			visited.add((nx, ny))

print(len(visited) + len(m))
