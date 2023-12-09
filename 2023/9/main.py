*f, = open(0).read().strip().split('\n')

# part 1

s = 0

for l in f:
	*a, = map(int, l.split())
	chain = [a]

	while a != [0] * len(a):
		b = []
		
		for i in range(1, len(a)):
			b.append(a[i] - a[i - 1])

		chain.append(b)
		a = b

	chain[-1].append(0)

	for c in range(len(chain) - 2, -1, -1):
		chain[c].append(chain[c][-1] + chain[c + 1][-1])

	s += chain[0][-1]

print(s)

# part 2

s = 0

for l in f:
	*a, = map(int, l.split())
	*a, = reversed(a) # this is all that changes!
	chain = [a]

	while a != [0] * len(a):
		b = []
		
		for i in range(1, len(a)):
			b.append(a[i] - a[i - 1])

		chain.append(b)
		a = b

	chain[-1].append(0)

	for c in range(len(chain) - 2, -1, -1):
		chain[c].append(chain[c][-1] + chain[c + 1][-1])

	s += chain[0][-1]

print(s)
