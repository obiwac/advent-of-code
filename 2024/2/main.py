f = open(0).readlines()

# Part 1.

s = 0

for l in f:
	*x, = map(int, l.split())
	sorted_ = sorted(x)

	if sorted_ != x and sorted_[::-1] != x:
		continue

	unsafe = False

	for i in range(len(x) - 1):
		if not (1 <= abs(x[i + 1] - x[i]) <= 3):
			unsafe = True
			break

	if not unsafe:
		s += 1

print(s)
