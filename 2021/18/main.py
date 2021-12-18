import math
import ast
from functools import reduce
from copy import deepcopy

f = [ast.literal_eval(x) for x in map(str.strip, open(0).read().strip().split('\n'))]

def propagate(i, x, trail, gp):
	l = len(trail)

	for j in range(l - 1, -1, -1): # got backwards up the trail 
		y = trail[j]

		if gp[j] == i:
			continue
		
		p = y
		y = y[i]

		if type(y) == int: # if we find an int, great, add explosion value and stop here
			p[i] += x[i]
			return
		
		# find the first number down the trail, add explosion value & stop when found

		while 1:
			p = y
			y = y[i ^ 1]

			if type(y) == int:
				p[i ^ 1] += x[i]
				return

def proc_expl(x, trail, gp, nest):
	if type(x) != list:
		return False
	
	if nest >= 4:
		for i in range(2):
			propagate(i, x, trail, gp)

		trail[-1][gp[-1]] = 0
	
	return any(proc_expl(x[i], trail + [x], gp + [i], nest + 1) for i in range(2))

def proc_split(x, trail, gp, nest):
	if type(x) == int and x >= 10:
		trail[-1][gp[-1]] = [x // 2, math.ceil(x / 2)]
		return True
	
	if type(x) == list:
		return any(proc_split(x[i], trail + [x], gp + [i], 0) for i in range(2))
	
	return False

def add(x, y):
	x = deepcopy([x, y])

	# reduce

	while 1:
		if not any(f(x, [], [], 0) for f in (proc_expl, proc_split)):
			return x

def mag(x):
	r = 0

	for i, y in enumerate(x):
		r += (mag(y) if type(y) == list else y) * (3, 2)[i]

	return r

print(mag(reduce(add, f)))

vals = []

for i in f:
	for j in f:
		vals.append(mag(add(i, j)))

print(max(vals))