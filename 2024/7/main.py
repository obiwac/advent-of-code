f = open(0).read().strip().split("\n")
ts = 0

for l in f:
	lv, rv = l.split(":")
	lv = int(lv)
	*a, = map(int, rv.strip().split())

	works = False

	for i in range(3 ** (len(a) - 1)):
		ops = bin(i)[2:].zfill(len(a) - 1).replace("1", "*").replace("0", "+")
		s = a[0]

		for i, o in enumerate(ops):
			if o == "+":
				s += a[i + 1]

			elif o == "*":
				s *= a[i + 1]

		works |= s == lv

	if works:
		ts += lv

print(ts)
