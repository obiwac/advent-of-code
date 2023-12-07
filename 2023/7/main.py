from functools import cmp_to_key
from collections import Counter

*f, = map(str.split, open(0).read().strip().split('\n'))
h = "AKQJT98765432"

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

def cmp(a_, b_):
	a = a_[0]
	b = b_[0]

	a_type = rank(a)
	b_type = rank(b)

	if a_type != b_type:
		return a_type - b_type

	for i in range(5):
		if h.index(a[i]) != h.index(b[i]):
			return h.index(b[i]) - h.index(a[i])

	return 0

print(rank("AAAAA"))
print(rank("AA8AA"))
print(rank("23332"))
print(rank("TTT98"))
print(rank("23432"))
print(rank("A23A4"))
print(rank("23456"))

print(cmp(["33332"], ["2AAAA"]))
print(cmp(["77888"], ["77788"]))

f.sort(key=cmp_to_key(cmp))
s = 0

for i in range(len(f)):
	s += int(f[i][1]) * (i + 1)

print(s)
