f = open(0).readlines()

# part 1

vals = []

for l in f:
	digits = []

	for c in l:
		# check if c is a number

		if c.isdigit():
			digits.append(int(c))

	vals.append(digits[0] * 10 + digits[-1])

print(sum(vals))
