from collections import Counter

*f, = map(list, open(0).read().strip().split("\n"))
walls_orig = set()
start = None
end = None

for i in range(len(f)):
	for j in range(len(f[i])):
		if f[i][j] == "#":
			walls_orig.add((i, j))
		elif f[i][j] == "S":
			start = (i, j)
		elif f[i][j] == "E":
			end = (i, j)

def fastest(walls, cs = 0, ce = 0):
	assert start is not None and end is not None

	q = [start]
	dist = [[float("inf")] * len(f[0]) for _ in range(len(f))]
	dist[start[1]][start[0]] = 0
	prev = [[(-1, -1)] * len(f[0]) for _ in range(len(f))]
	cheat = set()

	while q:
		cx, cy = q.pop(0)

		for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
			nx, ny = cx + dx, cy + dy

			if 0 <= nx < len(f) and 0 <= ny < len(f):
				cheat_mode = cs <= dist[cy][cx] + 1 <= ce

				if not cheat_mode and (nx, ny) in walls:
					continue

				if cheat_mode and (nx, ny) in walls:
					cheat.add((nx, ny))

				if dist[cy][cx] + 1 < dist[ny][nx]:
					dist[ny][nx] = dist[cy][cx] + 1
					prev[ny][nx] = (cx, cy)
					q.append((nx, ny))

	if dist[end[1]][end[0]] == float("inf"):
		return float("inf")

	# Reconstruct path

	path = list()
	cx, cy = end

	while (cx, cy) != start:
		cx, cy = prev[cy][cx]
		path.append((cx, cy))

	path.reverse()

	delta = 84 - dist[end[1]][end[0]]
	if delta == 72:
		print("======", cs, ce, 84 - dist[end[1]][end[0]])

		for i in range(len(f[0])):
			for j in range(len(f)):
				if (i, j) in cheat and 0:
					print("Z", end = "")
				elif (i, j) == start:
					print("S", end = "")
				elif (i, j) == end:
					print("E", end = "")
				elif (i, j) in path:
					print("C" if (i, j) in cheat else "X", end = "")
				elif (i, j) in walls:
					print("#", end = "")
				else:
					print(".", end = "")

			print()

	return dist[end[1]][end[0]]

orig_time = fastest(walls_orig)
print("example", orig_time - fastest(walls_orig, 0, 20))

s = 0
deltas = list()

for i in range(1, int(orig_time)):
	delta = orig_time - fastest(walls_orig, i, i + 20)

	if delta >= 50:
		deltas.append(delta)

	if delta >= 100:
		s += 1

print(s)
print(Counter(deltas))

"""
orig_time = fastest(walls_orig)

for i, wall in enumerate(walls_orig):
	print(i, len(walls_orig))
	walls = walls_orig - {wall}
	if orig_time - fastest(walls) >= 100:
		s += 1

"""
