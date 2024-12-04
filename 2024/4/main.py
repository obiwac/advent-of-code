import re

def flip(x):
	return ["".join(reversed(l)) for l in x]

*f, = map(str.strip, open(0).readlines())
options = [f, flip(f)]

*transposed, = map("".join, zip(*f))
options += [transposed, flip(transposed)]

for option in options[:2]:
	diags = []

	for i in range(-len(f), len(f)):
		diag = ""

		for j in range(len(f)):
			if j + i < 0 or j + i >= len(f):
				continue

			diag += option[j + i][j]

		diags.append(diag)

	options.extend([diags, flip(diags)])

# Part 1.

s = 0

for option in options:
	s += sum(len(re.findall("XMAS", l)) for l in option)

print(s)

# Part 2.

s = 0

for option in options[:4]:
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
