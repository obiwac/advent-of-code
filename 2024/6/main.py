f = open(0).read().split("\n")
*f, = map(list, f)

guard = [0, 0]
guard_dir = [-1, 0]
path = set()
obstacles = set()

for i in range(len(f)):
	for j in range(len(f[i])):
		if f[i][j] == "#":
			obstacles.add((i, j))

		if f[i][j] == "^":
			path.add((i, j))
			guard = [i, j]

print(guard)

while True:
	prev_guard = list(guard)

	guard[0] += guard_dir[0]
	guard[1] += guard_dir[1]

	if tuple(guard) in obstacles:
		guard = prev_guard

		if guard_dir == [-1, 0]:
			guard_dir = [0, 1]

		elif guard_dir == [1, 0]:
			guard_dir = [0, -1]

		elif guard_dir == [0, -1]:
			guard_dir = [-1, 0]

		elif guard_dir == [0, 1]:
			guard_dir = [1, 0]

		else:
			assert False

		continue

	if guard[0] < 0 or guard[0] > len(f) - 1 or guard[1] < 0 or guard[1] > len(f[0]) - 1:
		break

	path.add(tuple(guard))

done = 0

for i in range(len(f)):
	for j in range(len(f[i])):
		if (i, j) in obstacles:
			print("#", end="")

		elif [i, j] == guard:
			print("^", end="")

		elif (i, j) in path:
			done += 1
			print("X", end="")

		else:
			print(".", end="")
	
	print()

print(done)
