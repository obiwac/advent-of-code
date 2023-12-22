*f, = map(str, open(0).read().strip().split('\n'))
bricks = []

for b in f:
	c1, c2 = map(lambda x: [*map(int, x.split(","))], b.split("~"))
	bricks.append([c1, c2])

bricks.sort(key=lambda x: min(x[0][2], x[1][2]))
supporting = {}

for i in range(len(bricks)):
	new_min_height = min(bricks[i][0][2], bricks[i][1][2])

	while 1:
		if new_min_height == 1:
			break

		stop = False

		for j in range(i):
			max_height = max(bricks[j][0][2], bricks[j][1][2])

			bottom_left_1 = [bricks[i][0][0], bricks[i][0][1]]
			top_right_1 = [bricks[i][1][0], bricks[i][1][1]]

			bottom_left_2 = [bricks[j][0][0], bricks[j][0][1]]
			top_right_2 = [bricks[j][1][0], bricks[j][1][1]]

			overlap = not (top_right_1[0] < bottom_left_2[0] or bottom_left_1[0] > top_right_2[0] or top_right_1[1] < bottom_left_2[1] or bottom_left_1[1] > top_right_2[1])

			if overlap and new_min_height - 1 <= max_height:
				stop = True

				if i not in supporting:
					supporting[i] = []

				supporting[i].append(j)

		if stop:
			break

		new_min_height -= 1

	dz = bricks[i][1][2] - bricks[i][0][2]

	bricks[i][0][2] = new_min_height
	bricks[i][1][2] = new_min_height + dz

can_disintegrate = [True] * len(bricks)

for i, brick in enumerate(bricks):
	if i in supporting and len(supporting[i]) == 1: # supported by only one brick, can't disintegrate
		j = supporting[i][0]
		can_disintegrate[j] = False

print(can_disintegrate.count(True))
