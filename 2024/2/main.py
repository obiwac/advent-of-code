f = open(0).readlines()

def check_safety(x):
	sorted_ = sorted(x)

	if sorted_ != x and sorted_[::-1] != x:
		return False

	for i in range(len(x) - 1):
		if not (1 <= abs(x[i + 1] - x[i]) <= 3):
			return False

	return True

# Part 1.

s = 0

for l in f:
	*y, = map(int, l.split())
	s += check_safety(y)

print(s)

# Part 2.

s = 0

for l in f:
	*y, = map(int, l.split())

	if check_safety(y):
		s += 1
		continue

	for i in range(len(y)):
		o = list(y)
		del o[i]

		if check_safety(o):
			s += 1
			break

print(s)
