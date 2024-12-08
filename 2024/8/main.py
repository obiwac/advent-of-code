f = open(0).read().strip().split("\n")
freqs = {}

for i in range(len(f)):
	for j in range(len(f[i])):
		if f[i][j] == ".":
			continue

		if f[i][j] not in freqs:
			freqs[f[i][j]] = []

		freqs[f[i][j]].append((i, j))

for p in (1, 2):
	antinodes = set()

	for freq in freqs:
		for i1 in range(len(freqs[freq])):
			for i2 in range(i1 + 1, len(freqs[freq])):
				pos1 = freqs[freq][i1]
				pos2 = freqs[freq][i2]

				dy = pos1[0] - pos2[0]
				dx = pos1[1] - pos2[1]

				def try_add(i, j):
					if i < 0 or i >= len(f) or j < 0 or j >= len(f[i]):
						return 1

					antinodes.add((i, j))
					return 0

				for acc_y, acc_x, m in (pos1 + (1,), pos2 + (-1,)):
					for z in range(100000):
						if p == 1 and z > 1:
							break;

						if (p != 1 or z != 0) and try_add(acc_y, acc_x):
							break

						acc_y += m * dy
						acc_x += m * dx

	for i in range(len(f)):
		for j in range(len(f[i])):
			if f[i][j] != ".":
				print(f[i][j], end="")
			elif (i, j) in antinodes:
				print("X", end="")
			else:
				print(f[i][j], end="")
		print()

	print(len(antinodes))
