*f, = open(0).read().strip().split('\n')

instructions = f[0]
nodes_raw = f[2:]

nodes = {}

for node_raw in nodes_raw:
	name, _, left, right = node_raw.split()
	left = left[1: -1]
	right = right[:-1]

	nodes[name] = (left, right)

starts = [name for name in nodes if name[-1] == "A"]
dists = []

for start in starts:
	cur = start
	dist = 0

	while cur[-1] != "Z":
		if instructions[dist % len(instructions)] == "L":
			cur = nodes[cur][0]

		else:
			cur = nodes[cur][1]

		dist += 1

	dists.append(dist)

# least common multiple of all elements in dists

import math

def lcm(a, b):
	return a * b // math.gcd(a, b)

l = dists[0]

for d in dists[1:]:
	l = lcm(l, d)

print(dists, l)
