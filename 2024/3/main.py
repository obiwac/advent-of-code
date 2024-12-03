f = open(0).readlines()

s = 0

for l in f:
	for i in range(len(l)):
		v = l[i:].split(",")

		if len(v) < 2:
			continue

		if v[0][:4] != "mul(":
			continue

		try:
			a = int(v[0][4:])

		except ValueError:
			continue

		j = v[1].find(")")

		if j == -1:
			continue

		try:
			b = int(v[1][:j])

		except ValueError:
			continue

		s += a * b

print(s)
