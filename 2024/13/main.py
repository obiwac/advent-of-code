machines = open(0).read().strip().split("\n\n")

for p in (1, 2):
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

		px += (p == 2) * 10000000000000
		py += (p == 2) * 10000000000000

		b = (py - ay * px / ax) / (by - ay * bx / ax)
		a = (px - bx * b) / ax

		eps = 1e-3

		if abs(round(a) - a) < eps and abs(round(b) - b) < eps:
			s += int(a * 3 + b)

	print(s)
