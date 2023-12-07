from functools import cmp_to_key
from collections import Counter

*f, = map(str.split, open(0).read().strip().split('\n'))
h = "AKQJT98765432"

p2 = 0

def rank(a):
	a_type = 0
	a_count = Counter(a)

	if len(set(a)) == 5: # high card (all different)
		a_type = 0

	elif len(set(a)) == 4: # one pair
		a_type = 1

	elif len(set(a)) == 3: # two pair or three of kind
		if list(a_count.values()).count(3) == 1: # three of kind
			a_type = 3

		else: # two pair
			a_type = 2

	elif len(set(a)) == 2: # four of kind or full house
		if list(a_count.values()).count(4) == 1: # four of kind
			a_type = 5

		else:
			a_type = 4 # full house

	elif len(set(a)) == 1: # five of kind
		a_type = 6

	return a_type

def rank2(a):
	js = a.count("J")

	if js == 0: # regular card
		return rank(a)

	if js == 5 or js == 4: # can make five of kind
		return 6

	j_indices = [i for i, x in enumerate(a) if x == "J"]
	c = len(h) - 1
	best = 0

	for i in range(c ** js):
		b = list(a)

		b1 = i // c // c
		b2 = i // c % c
		b3 = i % c

		b[j_indices[0]] = h[b3]
		if len(j_indices) > 1: b[j_indices[1]] = h[b2]
		if len(j_indices) > 2: b[j_indices[2]] = h[b1]

		best = max(best, rank(b))

	return best

def cmp(a_, b_):
	a = a_[0]
	b = b_[0]

	a_type = (rank2 if p2 else rank)(a)
	b_type = (rank2 if p2 else rank)(b)

	if a_type != b_type:
		return a_type - b_type

	for i in range(5):
		if h.index(a[i]) != h.index(b[i]):
			return h.index(b[i]) - h.index(a[i])

	return 0

# part 1

f.sort(key=cmp_to_key(cmp))
s = 0

for i in range(len(f)):
	s += int(f[i][1]) * (i + 1)

print(s)

# part 2

h = "AKQT98765432J"
p2 = 1

f.sort(key=cmp_to_key(cmp))
s = 0

for i in range(len(f)):
	s += int(f[i][1]) * (i + 1)

print(s)
