f = open(0).readlines()

s1 = 0
s2 = 0
do = True

for l in f:
	for i in range(len(l)):
		if l[i:i + 4] == "do()":
			do = True
			continue

		if l[i:i + 7] == "don't()":
			do = False
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

		s1 += a * b

		if not do:
			s2 += a * b

print(s1)
print(s2)
