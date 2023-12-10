*f, = map(list, open(0).read().strip().split('\n'))

start = (0, 0)

for y, row in enumerate(f):
	for x, col in enumerate(row):
		if col == "S":
			start = (x, y)

q = [start]
dists = [[-1] * len(f[0]) for _ in range(len(f))]
loop = []

NORTH = "S|LJ"
SOUTH = "S|7F"
EAST = "S-LF"
WEST = "S-7J"

while q:
	x, y = q.pop(0)
	loop.append((x, y))

	for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
		nx = x + dx
		ny = y + dy

		if ny >= len(f) or ny < 0 or nx >= len(f[0]) or nx < 0:
			continue

		if dists[ny][nx] != -1:
			continue

		cur = f[y][x]
		n = f[ny][nx]

		if dx == 1 and cur in EAST and n in WEST:
			q.append((nx, ny))
			dists[ny][nx] = dists[y][x] + 1

		if dx == -1 and cur in WEST and n in EAST:
			q.append((nx, ny))
			dists[ny][nx] = dists[y][x] + 1

		if dy == 1 and cur in SOUTH and n in NORTH:
			q.append((nx, ny))
			dists[ny][nx] = dists[y][x] + 1

		if dy == -1 and cur in NORTH and n in SOUTH:
			q.append((nx, ny))
			dists[ny][nx] = dists[y][x] + 1

# for d in dists:
# 	print("".join(map(lambda x: str(x) if x >= 0 else ".", d)))

print(max(sum(dists, [])) + 1)
