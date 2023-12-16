*f, = map(str, open(0).read().strip().split('\n'))

def do(start):
	beams = [start]
	had = [[set() for _ in range(len(f[0]))] for _ in range(len(f))]
	energized = set()

	while beams:
		for beam in list(beams):
			x, y = beam[0], beam[1]
			dx, dy = beam[2], beam[3]
			nx, ny = x + dx, y + dy

			if not (x < 0 or x >= len(f[0]) or y < 0 or y >= len(f)):
				if (dx, dy) in had[y][x]:
					beams.pop(beams.index(beam))
					continue

				had[y][x].add((dx, dy))
				energized.add((x, y))

			if nx < 0 or nx >= len(f[0]) or ny < 0 or ny >= len(f):
				beams.pop(beams.index(beam))
				continue

			if f[ny][nx] == ".":
				beam[0], beam[1] = nx, ny
				continue

			if f[ny][nx] == "-" and dx != 0:
				beam[0], beam[1] = nx, ny
				continue

			if f[ny][nx] == "|" and dy != 0:
				beam[0], beam[1] = nx, ny
				continue

			if f[ny][nx] == "/":
				beam[0], beam[1] = nx, ny

				if dx == 1: beam[2], beam[3] = 0, -1
				if dx == -1: beam[2], beam[3] = 0, 1
				if dy == 1: beam[2], beam[3] = -1, 0
				if dy == -1: beam[2], beam[3] = 1, 0

				continue

			if f[ny][nx] == "\\":
				beam[0], beam[1] = nx, ny

				if dx == 1: beam[2], beam[3] = 0, 1
				if dx == -1: beam[2], beam[3] = 0, -1
				if dy == 1: beam[2], beam[3] = 1, 0
				if dy == -1: beam[2], beam[3] = -1, 0

				continue

			if f[ny][nx] == "-" and dx == 0:
				beam[0], beam[1] = nx, ny
				beam[2], beam[3] = 1, 0
				beams.append([nx, ny, -1, 0])
				continue

			if f[ny][nx] == "|" and dy == 0:
				beam[0], beam[1] = nx, ny
				beam[2], beam[3] = 0, 1
				beams.append([nx, ny, 0, -1])
				continue

			raise Exception("shouldn't happen")

	return len(energized)

"""
for y in range(len(f)):
	for x in range(len(f[0])):
		if f[y][x] != ".":
			print(f[y][x], end="")
			continue

		if len(had[y][x]) == 1:
			dx, dy = list(had[y][x])[0]

			if dx == 1: print(">", end="")
			if dx == -1: print("<", end="")
			if dy == 1: print("v", end="")
			if dy == -1: print("^", end="")

			continue

		if len(had[y][x]) > 1:
			print(len(had[y][x]), end="")
			continue

		if (x, y) in energized:
			print("#", end="")
			continue

		print(f[y][x], end="")

	print()
"""

print(do([-1, 0, 1, 0]))

s = 0

for y in range(len(f)):
	s = max(s, do([-1, y, 1, 0]))
	s = max(s, do([len(f), y, -1, 0]))

for x in range(len(f[0])):
	s = max(s, do([x, -1, 0, 1]))
	s = max(s, do([x, len(f[0]), 0, -1]))

print(s)
