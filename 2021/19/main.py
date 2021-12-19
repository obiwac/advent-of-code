import numpy as np
import glm
import math
from itertools import chain, accumulate, permutations
from functools import reduce
from collections import Counter, defaultdict
from operator import mul

print("Generating rotation quaternions ...")

rotation_quaterions = set()

for i in range(4):
	for j in range(4):
		for k in range(4):
			quaterion = glm.quat(glm.vec3(math.tau / 4 * i, math.tau / 4 * j, math.tau / 4 * k))
			rotation_quaterions.add(quaterion)

class Scanner:
	def __init__(self):
		self.absolute = False
		self.pos = glm.vec3(0)
		self.relative = []

print("Parsing input ...")

f = [x for x in map(str.strip, open(0).read().strip().split('\n'))]
scanners = []
c = None

for l in f:
	if not l:
		continue

	if l[:3] == '-' * 3:
		c = int(l.split(' ')[2])
		scanners.append(Scanner())

	else:
		scanners[-1].relative.append(glm.vec3(*map(int, l.split(','))))

scanners[0].absolute = True

def overlap(a, b):
	# assumes a is in the correct orientation and b needs a bit of help

	for quaterion in rotation_quaterions:
		with_rotation = []

		for beacon in b.relative:
			with_rotation.append(glm.vec3(*(round(x) for x in beacon * quaterion)))
	
		for i in with_rotation:
			for j in a.relative:
				# if i - delta == j, it then follows that 12 other points should be equal

				delta = j - i
				count = 0
				overlap = [] # necessary?
				
				for k in with_rotation:
					for l in a.relative:
						if l == k + delta:
							count += 1
							overlap.append(l)

				if count >= 12:
					# we do that so that we can say "X relative to any other scanner is equivalent to X relative to the 0th scanner"

					b.pos += delta
					b.relative = with_rotation
					b.absolute = True

					for i, x in enumerate(b.relative):
						b.relative[i] = x + delta

					return delta
	
	return False

print("Absolutely positioning all scanners ...")

while not all(x.absolute for x in scanners):
	for j in scanners:
		if j.absolute:
			continue

		for i in scanners:
			if i == j or not i.absolute:
				continue
			
			delta = overlap(i, j)

			if delta:
				print(f"{sum(x.absolute for x in scanners) - 1}/{len(scanners)}")
				i = j
				break

# part 1

beacons = set()

for scanner in scanners:
	beacons = beacons.union(scanner.relative)

print("Beacon count:", len(beacons))

# part 2

dists = []

for x in scanners:
	for y in scanners:
		dists.append(sum(map(abs, x.pos - y.pos)))

print("Max Manhattan distance:", int(max(dists)))