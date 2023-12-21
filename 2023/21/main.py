import math

*f, = map(list, open(0).read().strip().split('\n'))
w, h = len(f[0]), len(f)

starting_point = (0, 0)

for i in range(len(f)):
	for j in range(len(f[i])):
		if f[i][j] == 'S':
			starting_point = (j, i)

full_poss = [0, 0]

grid_poss = [
	[[False] * w for _ in range(h)],
	[[False] * w for _ in range(h)],
]

# TODO is this right?

def in_prison(x, y):
	try:
		return f[y - 1][x] == "#" and f[y + 1][x] == "#" and f[y][x - 1] == "#" and f[y][x + 1] == "#"

	except:
		return False

for y in range(len(f)):
	shift = -1 if y % 2 else 0

	for x in range(-shift, len(f[y]) + shift, 2):
		if f[y][x] in 'S.' and not in_prison(x, y):
			full_poss[0] += 1
			grid_poss[0][y][x] = True

	shift = 0 if y % 2 else -1

	for x in range(-shift, len(f[y]) + shift, 2):
		if f[y][x] in 'S.' and not in_prison(x, y):
			full_poss[1] += 1
			grid_poss[1][y][x] = True

# steps = 26501365
steps = 5000
choose_i = steps % 2
chosen_grid_poss = grid_poss[choose_i]

# right_full_squares = max(0, (steps - (w - starting_point[0] - 1) - w) // w)
# left_full_squares = max(0, (steps - starting_point[0] - w) // w)
# down_full_squares = max(0, (steps - (h - starting_point[1] - 1) - h) // h)
# up_full_squares = max(0, (steps - starting_point[1] - h) // h)
# 
# # +1 cuz count middle square
# 
# horz_full_squares = left_full_squares + right_full_squares + 1
# vert_full_squares = up_full_squares + down_full_squares + 1

radius_full_squares = max(0, (steps - starting_point[0] - w) // w)
diam_full_squares = 2 * radius_full_squares + 1
 
s = math.ceil(diam_full_squares * diam_full_squares / 2) // 2 * full_poss[choose_i]
s += (math.ceil(diam_full_squares * diam_full_squares / 2) // 2 + 1) * full_poss[not choose_i]

# edge fillers
# since # steps is a multiple of our grid size, we just have one edge filler to deal with

primary_edge = [0, 0]
v = 1

for y in range(h):
	for x in range(w):
		dx = w - starting_point[0] + radius_full_squares * w + x - w
		dy = h - starting_point[1] + y

		dist = abs(dx + dy)

		if v: print("X" if dist <= steps else " ", end="")

		if True: # dist <= steps:
			for i in range(2):
				primary_edge[i] += grid_poss[i][y][x]
				primary_edge[i] += grid_poss[i][h - y - 1][x]
				primary_edge[i] += grid_poss[i][y][w - x - 1]
				primary_edge[i] += grid_poss[i][h - y - 1][w - x - 1]

	if v: print()

s += primary_edge[not choose_i] * (radius_full_squares // 2)
s += primary_edge[choose_i] * (radius_full_squares // 2 + 1)

# corners

corners = [0, 0]

for y in range(h):
	for x in range(w):
		if v: print("X" if abs((x - w // 2) + y) > h // 2 else " ", end="")

		if abs((x - w // 2) + y) > h // 2:
			continue

		for i in range(2):
			corners[i] += grid_poss[i][y][x]
			corners[i] += grid_poss[i][h - y - 1][x]
			corners[i] += grid_poss[i][y][w - x - 1]
			corners[i] += grid_poss[i][h - y - 1][w - x - 1]

	if v: print()

s += corners[choose_i]

# how many full squares?

print(s)
