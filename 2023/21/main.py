*f, = map(list, open(0).read().strip().split('\n'))

starting_point = (0, 0)

for i in range(len(f)):
	for j in range(len(f[i])):
		if f[i][j] == 'S':
			starting_point = (j, i)

q = [(starting_point, 0)]
right_dist = set()
pcurdist = -1

while q:
	cur, cur_dist = q.pop(0)

	if pcurdist != cur_dist:
		print(cur_dist, len(q), len(set(q)))
		q = list(set(q))
		pcurdist = cur_dist

	if cur_dist >= 64:
		continue

	for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
		x, y = cur[0] + dx, cur[1] + dy

		if 0 <= y < len(f) and 0 <= x < len(f[0]):
			if f[y][x] in ".S":
				q.append(((x, y), cur_dist + 1))

				if cur_dist + 1 == 64:
					right_dist.add((x, y))

for j in range(len(f)):
	for i in range(len(f[j])):
		if f[j][i] == "." or f[j][i] == "S": print("O" if (i, j) in right_dist else ".", end="")
		if f[j][i] == "#": print("#", end="")

	print()

print(len(right_dist))
