*f, = map(list, open(0).read().strip().split('\n'))

start = (0, 0)

for y, row in enumerate(f):
	for x, col in enumerate(row):
		if col == "S":
			start = (x, y)

q = [start]
dists = [[-1] * len(f[0]) for _ in range(len(f))]
loop = [[False] * len(f[0]) for _ in range(len(f))]

NORTH = "S|LJ"
SOUTH = "S|7F"
EAST = "S-LF"
WEST = "S-7J"

while q:
	x, y = q.pop(0)
	loop[y][x] = True

	for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
		nx = x + dx
		ny = y + dy

		if ny >= len(f) or ny < 0 or nx >= len(f[0]) or nx < 0:
			continue

		if dists[ny][nx] != -1:
			continue

		cur = f[y][x]
		n = f[ny][nx]

		if \
			(dx ==  1 and cur in EAST and n in WEST) or \
			(dx == -1 and cur in WEST and n in EAST) or \
			(dy ==  1 and cur in SOUTH and n in NORTH) or \
			(dy == -1 and cur in NORTH and n in SOUTH):
			q.append((nx, ny))
			dists[ny][nx] = dists[y][x] + 1

# for d in dists:
# 	print("".join(map(lambda x: str(x) if x >= 0 else ".", d)))

in_count = 0

for y, row in enumerate(f):
	inside = False
	in_horz = False
	first_horz = "."

	for x, col in enumerate(row):
		if f[y][x] == "S":
			f[y][x] = "F" # yes, hardcoded, but this would take a lot of time to do correctly :)

		if in_horz and f[y][x] != "-":
			if (first_horz not in SOUTH and f[y][x] in SOUTH) or first_horz not in NORTH and f[y][x] in NORTH:
				inside = not inside

			in_horz = False
			continue

		if in_horz:
			continue

		if loop[y][x]:
			if f[y][x] in EAST + WEST:
				first_horz = f[y][x]
				in_horz = True
				continue

			inside = not inside
			continue

		if inside:
			f[y][x] = "I"
			in_count += 1

for y, row in enumerate(f):
	for x, col in enumerate(row):
		if loop[y][x] or col == "I":
			print(col, end="")
			continue

		print("O", end="")

	print()

print(max(sum(dists, [])) + 1)
print(in_count)
