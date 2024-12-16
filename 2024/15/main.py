m, l = open(0).read().strip().split("\n\n")
*m, = map(list, m.split("\n"))
l = l.replace("\n", "")

walls = set()
boxes = set()
x, y = 0, 0

for i in range(len(m)):
	for j in range(len(m[i])):
		if m[i][j] == "#":
			walls.add((j * 2, i))
			walls.add((j * 2 + 1, i))

		elif m[i][j] == "O":
			boxes.add((j * 2, i))

		elif m[i][j] == "@":
			x, y = j * 2, i

PRINT_MAP = False

for mi, move in enumerate(l):
	if PRINT_MAP:
		for i in range(len(m)):
			skip = False

			for j in range(len(m[i]) * 2):
				if skip:
					skip = False
					continue

				if (j, i) in boxes:
					print("[]", end="")
					skip = True

				elif (j, i) in walls:
					print("##", end="")
					skip = True

				elif (j, i) == (x, y):
					print("@", end="")

				else:
					print(".", end="")

			print()

	t = {
		"<": (-1, 0),
		">": (1, 0),
		"^": (0, -1),
		"v": (0, 1),
	}

	dx, dy = t[move]
	ox, oy = x + dx, y + dy

	if (ox, oy) in walls:
		continue

	cx, cy = ox + (dx if dx == -1 else 0), oy

	to_move = set()
	layer = set()
	hit_wall = False

	for _ in range(1000):
		if dx and (cx, cy) not in boxes:
			break

		if dx:
			to_move.add((cx, cy))

		if dy:
			nl = set()

			for bx, by in layer:
				if (bx - 1, by + dy) in boxes:
					nl.add((bx - 1, by + dy))
					assert (bx, by + dy) not in boxes

				if (bx + 1, by + dy) in boxes:
					nl.add((bx + 1, by + dy))
					assert (bx, by + dy) not in boxes

				if (bx, by + dy) in boxes:
					nl.add((bx, by + dy))

				if (bx, by + dy) in walls or (bx + 1, by + dy) in walls:
					hit_wall = True
					break

			if hit_wall:
				break

			if cy == oy and (ox, oy) in boxes:
				nl.add((ox, oy))

			if cy == oy and (ox - 1, oy) in boxes:
				nl.add((ox - 1, oy))

			if not nl:
				break

			layer = nl
			to_move.update(layer)

		cx += dx * 2
		cy += dy

	if hit_wall:
		continue

	if dx and (cx - (dx if dx == -1 else 0), cy) in walls:
		continue # Do nothing if we can't move.

	for bx, by in to_move:
		boxes.remove((bx, by))

	for bx, by in to_move:
		boxes.add((bx + dx, by + dy))

	x, y = ox, oy

s = 0

for bx, by in boxes:
	s += bx + by * 100

print(s)
