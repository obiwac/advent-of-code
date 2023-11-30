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

# part 2

vals = []

for l in f:
	digits = [0, 0]

	# find first digit (written in english or as a number)

	for i in range(len(l)):
		if l[i].isdigit():
			digits[0] = int(l[i])

		elif l[i:].startswith("one"): digits[0] = 1
		elif l[i:].startswith("two"): digits[0] = 2
		elif l[i:].startswith("three"): digits[0] = 3
		elif l[i:].startswith("four"): digits[0] = 4
		elif l[i:].startswith("five"): digits[0] = 5
		elif l[i:].startswith("six"): digits[0] = 6
		elif l[i:].startswith("seven"): digits[0] = 7
		elif l[i:].startswith("eight"): digits[0] = 8
		elif l[i:].startswith("nine"): digits[0] = 9

		else:
			continue

		break

	# same things, but starting from the end

	for i in range(len(l) - 1, -1, -1):
		if l[i].isdigit():
			digits[1] = int(l[i])

		elif l[:i].endswith("one"): digits[1] = 1
		elif l[:i].endswith("two"): digits[1] = 2
		elif l[:i].endswith("three"): digits[1] = 3
		elif l[:i].endswith("four"): digits[1] = 4
		elif l[:i].endswith("five"): digits[1] = 5
		elif l[:i].endswith("six"): digits[1] = 6
		elif l[:i].endswith("seven"): digits[1] = 7
		elif l[:i].endswith("eight"): digits[1] = 8
		elif l[:i].endswith("nine"): digits[1] = 9

		else:
			continue

		break

	vals.append(digits[0] * 10 + digits[-1])

print(sum(vals))
