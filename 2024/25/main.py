f = open(0).read().strip().split("\n\n")

locks = []
keys = []

for lock in f:
	rows = lock.split("\n")
	is_lock = rows[0] == "#" * len(rows[0])
	thing = [*map(lambda x: x.count("#") - 1, zip(*rows))]
	
	if is_lock:
		locks.append(thing)

	else:
		keys.append(thing)

s = 0

for key in keys:
	for lock in locks:
		for i in range(5):
			if key[i] + lock[i] > 5:
				break

		else:
			s += 1

print(s)
