import re

*f, = map(str.strip, open(0).readlines())
*transposed, = map("".join, zip(*f))

s = 0

options = [f, ["".join(reversed(l)) for l in f]]
options += [transposed, ["".join(reversed(l)) for l in transposed]]

for oc, option in enumerate(options):
	for i, l in enumerate(option[:-2]):
		for match in re.finditer("(?=(M.S))", l):
			if option[i + 1][match.start() + 1] != "A":
				continue

			if option[i + 2][match.start()] != "M":
				continue

			if option[i + 2][match.start() + 2] != "S":
				continue

			s += 1

print(s)
exit()

for l in transposed:
	s += len(re.findall("XMAS", l))
	s += len(re.findall("SAMX", l))

diag1 = []

for i in range(-len(f), len(f)):
	diag = ""

	for j in range(len(f)):
		if j + i < 0 or j + i >= len(f):
			continue

		diag += f[j + i][j]

	diag1.append(diag)

diag2 = []

for i in range(-len(f), len(f)):
	diag = ""

	for j in range(len(f)):
		if j + i < 0 or j + i >= len(f):
			continue

		diag += list(reversed(f[j + i].strip()))[j]

	diag2.append(diag)

print(diag1)
print(diag2)

for l in diag1:
	s += len(re.findall("XMAS", l))
	s += len(re.findall("SAMX", l))

for l in diag2:
	s += len(re.findall("XMAS", l))
	s += len(re.findall("SAMX", l))

print(s)
