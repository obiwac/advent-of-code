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

for y in range(len(f)):
	shift = -1 if y % 2 else 0

	for x in range(-shift, len(f[y]) + shift, 2):
		if f[y][x] in 'S.':
			full_poss[0] += 1
			grid_poss[0][y][x] = True

	shift = 0 if y % 2 else -1

	for x in range(-shift, len(f[y]) + shift, 2):
		if f[y][x] in 'S.':
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
 
s = math.ceil(diam_full_squares * diam_full_squares / 2) * full_poss[choose_i]

# edge fillers

"""
xx.......
xxx......
xxxx.....
###xx....
###xxx...
###xxxx..
######xx.
######xxx
######xxxx
#########xx
#########xxx
#########xx
######xxxx
######xxx
######xx
"""

primary_edge = 0
secondary_edge = 4 * w * h / 4

# for y in range(h):
# 	for x in range(w):
# 		dx = w - starting_point[0] + right_full_squares * w + x - w
# 		dy = h - starting_point[1] + h + y
# 
# 		dist = abs(dx + dy)
# 
# 		if dist < steps:
# 			primary_edge += chosen_grid_poss[y][x]
# 			primary_edge += chosen_grid_poss[h - y - 1][x]
# 			primary_edge += chosen_grid_poss[y][w - x - 1]
# 			primary_edge += chosen_grid_poss[h - y - 1][w - x - 1]
# 
# for y in range(h):
# 	for x in range(w):
# 		dx = w - starting_point[0] + right_full_squares * w + x - w
# 		dy = h - starting_point[1] + y
# 
# 		dist = abs(dx + dy)
# 
# 		if dist < steps:
# 			secondary_edge += chosen_grid_poss[y][x]
# 			secondary_edge += chosen_grid_poss[h - y - 1][x]
# 			secondary_edge += chosen_grid_poss[y][w - x - 1]
# 			secondary_edge += chosen_grid_poss[h - y - 1][w - x - 1]

# s += primary_edge * radius_full_squares
# s += secondary_edge * radius_full_squares

# how many full squares?

print(s)
