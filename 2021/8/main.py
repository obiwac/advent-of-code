from itertools import accumulate
from itertools import chain
from functools import reduce
from collections import Counter

f = [[y.strip().split() for y in x.split('|') if y] for x in map(str.strip, open(0).readlines())]

count = 0

for line in f:
	_in, out = line

	s = ""

	zero_pos = []
	two_pos  = []
	five_pos = []
	six_pos  = []

	one_pos   = []
	four_pos  = []
	seven_pos = []
	eight_pos = []

	# one

	for x in _in:
		if len(x) == 2:
			one_pos.extend(set(x))

	for x in _in:
		if len(x) == 4:
			four_pos.extend(set(x))

	for x in _in:
		if len(x) == 3:
			seven_pos.extend(set(x))

	for x in _in:
		if len(x) == 7:
			eight_pos.extend(set(x))

	one_pos   = set(one_pos)
	four_pos  = set(four_pos)
	seven_pos = set(seven_pos)
	eight_pos = set(eight_pos)

	for x in out:
		if len(x) == 2: s += "1" # 1
		if len(x) == 4: s += "4" # 4
		if len(x) == 3: s += "7" # 7
		if len(x) == 7: s += "8" # 8

		if len(x) == 5:
			if len((eight_pos - seven_pos - four_pos) & set(x)) == 2: s += "2"
			elif len(one_pos & set(x)) == 2: s += "3"
			else: s += "5"
		
		if len(x) == 6:
			if len((eight_pos - four_pos) & set(x)) == 3 and len(seven_pos & set(x)) == 3: s += "0"
			elif len(one_pos & set(x)) == 2: s += "9"
			else: s += "6"
	
	count += int(s)
	print(out, s)

print(count)