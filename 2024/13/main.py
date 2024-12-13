from sympy import symbols, Eq, solve

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

	px += 10000000000000
	py += 10000000000000

	a, b = symbols(["a", "b"])

	system = [
		Eq(ax * a + bx * b, px),
		Eq(ay * a + by * b, py),
	]

	sol = solve(system, [a, b])
	eps = 1e-6

	if sol[a] % 1 < eps and sol[b] % 1 < eps:
		s += sol[a] * 3 + sol[b]

print(s)
