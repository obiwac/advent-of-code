f = open(0).read().strip().split("\n")

for base in (2, 3):
	ts = 0

	for z, l in enumerate(f):
		# print(f"{z}/{len(f)}")

		lv, rv = l.split(":")
		lv = int(lv)
		*a, = map(int, rv.strip().split())

		works = False

		for i in range(3 ** (len(a) - 1)):
			ops = [0] * (len(a) - 1)

			for j in range(len(a) - 1):
				ops[j] = i // (base ** j) % base

			s = a[0]

			for i, o in enumerate(ops):
				if o == 0:
					s += a[i + 1]

				elif o == 1:
					s *= a[i + 1]

				elif o == 2:
					s = int(str(s) + str(a[i + 1]))

			works |= s == lv

		if works:
			ts += lv

	print(ts)
