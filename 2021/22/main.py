from itertools import chain
from itertools import accumulate
from functools import reduce
from collections import Counter, defaultdict
from operator import mul

f = [x.split(' ') for x in map(str.strip, open(0).read().strip().split('\n'))]
steps = []

def _min(x):
	if not x:
		return "empty"

	return min(x)

def _max(x):
	if not x:
		return "empty"

	return max(x)

class Step:
	def __init__(self, on, xr, yr, zr):
		self.on = on
		self.xr = xr
		self.yr = yr
		self.zr = zr
	
	def __repr__(self):
		return f"({_min(self.xr)}..{_max(self.xr)}, {_min(self.yr)}..{_max(self.yr)}, {_min(self.zr)}..{_max(self.zr)})"

def clamp(x):
	return x#min(max(x, -50), 50)

for l in f:
	ranges = l[1].split(',')

	for r in range(len(ranges)):
		x = [*map(int, ranges[r][2:].split('..'))]
		ranges[r] = range(clamp(x[0]), clamp(x[1]) + 1)

	steps.append(Step(l[0] == "on", *ranges))

def intersect(a, b):
	c = set(a) & set(b)

	if not c:
		return False

	return range(min(c), max(c) + 1)

def rr(a, b): # remove range
	c = set(a) - set(b)

	if not c:
		if set(a) & set(b):
			return range(0, 0)

		return False
	
	return range(min(c), max(c) + 1)

def intersect_steps(a, b):
	c = Step(False, intersect(a.xr, b.xr), intersect(a.yr, b.yr), intersect(a.zr, b.zr))

	if False in (c.xr, c.yr, c.zr):
		return False

	return c

def break_step(a, b): # break a by b
	pieces = []
	inter = intersect_steps(a, b)

	if not inter:
		return False
	
	xr = rr(a.xr, b.xr)
	yr = rr(a.yr, b.yr)
	zr = rr(a.zr, b.zr) # AAAGH

	if False in (xr, yr, zr):
		return False

	pieces.append(Step(0, xr, yr, zr))

	pieces.append(Step(0, xr, yr, inter.zr))
	pieces.append(Step(0, xr, inter.yr, zr))
	pieces.append(Step(0, inter.xr, yr, zr))

	pieces.append(Step(0, xr, inter.yr, inter.zr))
	pieces.append(Step(0, inter.xr, yr, inter.zr))
	pieces.append(Step(0, inter.xr, inter.yr, zr))

	return pieces

on_regions = []

for i, step in enumerate(steps):
	if step.on:
		# break all steps leading up to this one

		broken = []
		rem = []

		for j in on_regions:
			b = break_step(j, step)

			if b:
				for c in b:
					if range(0) in (c.xr, c.yr, c.zr):
						continue

					broken.append(c)
				
				rem.append(j)
		
		for r in rem:
			on_regions.remove(r)

		on_regions.extend(broken)
		on_regions.append(step)

	else:
		# break all steps leading up to this one

		broken = []
		rem = []

		for j in on_regions:
			b = break_step(j, step)

			if b:
				for c in b:
					if range(0) in (c.xr, c.yr, c.zr):
						continue

					broken.append(c)

				rem.append(j)
		
		for r in rem:
			on_regions.remove(r)
		
		on_regions.extend(broken)
	
	print(f"step {i} {len(on_regions)}")

count = 0

for r in on_regions:
	count += len(r.xr) * len(r.yr) * len(r.zr)

print(count)