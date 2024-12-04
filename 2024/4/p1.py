import re

f = open(0).readlines()
*transposed, = map("".join, zip(*f))

s = 0

for l in f:
	s += len(re.findall("MAS", l))
	s += len(re.findall("SAM", l))

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
