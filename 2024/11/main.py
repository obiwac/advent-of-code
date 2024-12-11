f = open(0).read().strip().split("\n")
*a, = map(int, f[0].split())

for _ in range(25):
	na = []

	for i, x in enumerate(a):
		if x == 0:
			na.append(1)

		elif len(str(x)) % 2 == 0:
			na.append(int(str(x)[:len(str(x)) // 2]))
			na.append(int(str(x)[len(str(x)) // 2:]))

		else:
			na.append(x * 2024)

	a = na

print(len(a))
