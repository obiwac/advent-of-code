*f, = map(list, open(0).read().strip().split('\n'))
w, h = len(f[0]), len(f)

starting_point = (0, 0)
full_poss = [0, 0]

for i in range(len(f)):
	for j in range(len(f[i])):
		if f[i][j] == 'S':
			starting_point = (j, i)

for y in range(len(f)):
	shift = -1 if y % 2 else 0

	for x in range(shift, len(f[y]) + shift, 2):
		if f[y][x] in 'S.':
			full_poss[0] += 1

		if f[y - 1][x - 1] in 'S.':
			full_poss[1] += 1

steps = 5000
right_full_squares = max(0, (steps - (w - starting_point[0]) - w) // w)
left_full_squares = max(0, (steps - starting_point[0] - w) // w)
down_full_squares = max(0, (steps - (h - starting_point[1]) - h) // h)
up_full_squares = max(0, (steps - starting_point[1] - h) // h)

# +1 cuz count middle square

horz_full_squares = left_full_squares + right_full_squares + 1
vert_full_squares = up_full_squares + down_full_squares + 1

print((horz_full_squares * vert_full_squares / 2) * full_poss[1])

# how many full squares?

print(full_poss)
