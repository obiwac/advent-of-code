f = open(0).readlines()

s = 0
do = True

for l in f:
	for i in range(len(l)):
		if l[i:i + 4] == "do()":
			do = True
			continue

		if l[i:i + 7] == "don't()":
			do = False
			continue

		if not do:
			continue

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
