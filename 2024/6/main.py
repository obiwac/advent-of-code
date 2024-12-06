f = open(0).read().split("\n")
*f, = map(list, f)

initial_guard = [0, 0]
initial_guard_dir = [-1, 0]
path = set()
obstacles = set()

for i in range(len(f)):
	for j in range(len(f[i])):
		if f[i][j] == "#":
			obstacles.add((i, j))

		if f[i][j] == "^":
			path.add((i, j))
			initial_guard = [i, j]

print(initial_guard)

def in_loop(new_obstacle):
	guard = list(initial_guard)
	guard_dir = list(initial_guard_dir)
	states = set({(*guard, *guard_dir)})
	path = set()

	while True:
		prev_guard = list(guard)

		guard[0] += guard_dir[0]
		guard[1] += guard_dir[1]

		if tuple(guard) in obstacles or tuple(guard) == new_obstacle:
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

		state = (*guard, *guard_dir,)

		if state in states:
			return True

		states.add(state)
		path.add(tuple(guard))

	return False

s = 0

for i in range(len(f)):
	for j in range(len(f[i])):
		if f[i][j] == ".":
			if in_loop((i, j)):
				s += 1
				print("Loop at", i, j)

print(s)

"""
done = 0

for i in range(len(f)):
	for j in range(len(f[i])):
		if (i, j) in obstacles:
			print("#", end="")

		elif [i, j] == initial_guard:
			print("^", end="")

		elif (i, j) in path:
			done += 1
			print("X", end="")

		else:
			print(".", end="")
	
	print()

print(len(path), done)
"""
