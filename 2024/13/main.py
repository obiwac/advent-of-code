machines = open(0).read().strip().split("\n\n")
s = 0

for machine in machines:
	a, b, prize = machine.split("\n")

	ax, ay = a.split()[2:]
	ax = int(ax[2: -1])
	ay = int(ay[2:])

	bx, by = b.split()[2:]
	bx = int(bx[2: -1])
	by = int(by[2:])

	px, py = prize.split()[1:]
	px = int(px[2: -1])
	py = int(py[2:])

	m = float("inf")

	for i in range(100):
		for j in range(100):
			if i * ax + j * bx == px and i * ay + j * by == py:
				cost = 3 * i + 1 * j

				if cost < m:
					m = cost

	if m < float("inf"):
		s += m

print(s)
