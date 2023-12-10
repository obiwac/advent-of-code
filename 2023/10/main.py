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

NONE = -1
IN = 0
OUT = 1

status = [[NONE] * len(f[0]) for _ in range(len(f))]

for y, row in enumerate(f):
	for x, col in enumerate(row):
		if col != ".":
			continue

		if status[y][x] != NONE:
			continue

		q = [(x, y)]
		status[y][x] = IN
		done = [(x, y)]
		is_out = False

		while q:
			x, y = q.pop(0)

			for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, 1), (-1, -1), (1, -1)):
				nx = x + dx
				ny = y + dy

				if ny >= len(f) or ny < 0 or nx >= len(f[0]) or nx < 0:
					is_out = True
					continue

				if f[ny][nx] != ".":
					continue

				if status[ny][nx] == NONE:
					status[ny][nx] = IN
					done.append((nx, ny))
					q.append((nx, ny))

		if is_out:
			for x, y in done:
				status[y][x] = OUT

for y, row in enumerate(f):
	for x, col in enumerate(row):
		print(f[y][x] if status[y][x] == NONE else ("I" if status[y][x] == IN else "O"), end="")

	print()

print(sum(status, []).count(IN))
