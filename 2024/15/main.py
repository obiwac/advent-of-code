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

		elif m[i][j] == "O":
			boxes.add((j * 2, i))

		elif m[i][j] == "@":
			x, y = j * 2, i

for move in l:
	print()

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
	cx, cy = ox, oy

	while (cx, cy) in boxes:
		cx += dx
		cy += dy

	if (cx, cy) in walls:
		continue # Do nothing if we can't move.

	if (ox, oy) in boxes:
		boxes.remove((ox, oy))
		boxes.add((cx, cy))

	x, y = ox, oy

s = 0

for bx, by in boxes:
	s += bx + by * 100

print(s)
