from itertools import chain
from itertools import accumulate
from functools import reduce
from collections import Counter

f = [x for x in map(str.strip, open(0).read().strip().split('\n'))]

OPEN = "{([<"
CLOSE = "})]>"

POINTS = {
	")": 1,
	"]": 2,
	"}": 3,
	">": 4
}

completion = []

points = 0
scores = []

for l in f:
	stack = []

	wrong = False
	for x in l:
		if x in OPEN:
			stack.append(x)
		
		if x in CLOSE:
			if OPEN.index(stack.pop()) != CLOSE.index(x):
				points += POINTS[x]
				break
	
	else:
		score = 0

		while stack:
			p = stack.pop()

			score *= 5
			score += POINTS[CLOSE[OPEN.index(p)]]
		
		scores.append(score)

scores = sorted(scores)
print(scores[len(scores) // 2])