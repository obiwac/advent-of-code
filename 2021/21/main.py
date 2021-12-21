from itertools import chain
from itertools import accumulate
from functools import reduce
from collections import Counter
from operator import mul

s = [4, 8] # starting position
rolls = 0

def roll():
	global rolls
	rolls += 1
	return (rolls - 1) % 100 + 1

def play(i):
	s[i] += roll()
	s[i] = (s[i] - 1) % 10 + 1

p = [0, 0] # points

while p[0] < 1000 and p[1] < 1000:
	for i in range(len(s)):
		for _ in range(3):
			play(i)
		
		p[i] += s[i]
		
		if p[i] >= 1000:
			break

print(rolls * min(p))

r = {} # possible states

# i tells us if it's A's turn or B's turn

def universe(s, p, i = 0):
	h = hash((*s, *p, i))

	if h in r: # have we already encountered a state?
		return r[h]

	w = [0, 0] # wins in subsequent universes

	for d in range(27): # 3 * 3 * 3 universes generated after turn
		steps = d // 3 // 3 + d // 3 % 3 + d % 3 + 3
		pos = (s[i] + steps) % 10 + 1

		_p = list(p)
		_s = list(s)

		_p[i] += pos

		if _p[i] >= 21: # win?
			w[i] += 1
			continue

		_s[i] = pos - 1
		_p = universe(_s, _p, i ^ 1)
		
		w[0] += _p[0]
		w[1] += _p[1]

	r[h] = w
	return w

print(max(universe([4 - 1, 5 - 1], [0, 0])))