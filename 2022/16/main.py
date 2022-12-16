import math
from itertools import chain
from itertools import accumulate
from functools import reduce
from collections import Counter
from collections import defaultdict
from collections import deque
from copy import deepcopy

import heapq

f = open(0).read().strip().split('\n')
valves = {}

for v in f:
	bits = v.split()
	name = bits[1]
	rate = int(bits[4][5: -1])
	*goes_to, = map(lambda x: x.strip(','), bits[9: len(bits)])
	valves[name] = [rate, goes_to, 0, [], False]

# part 1

opened = set()
visited = {}
candidates = set()

def dfs(curr, minute, rate):
	# do we have time left?

	if minute == 30:
		candidates.add(rate)
		return

	# check we haven't yet encountered this condition

	if (curr, minute) in visited and visited[(curr, minute)] >= rate:
		return

	visited[(curr, minute)] = rate

	# try going down every path

	goes_to = valves[curr][1]
	new = sum(v[0] for k, v in valves.items() if k in opened)

	for g in goes_to:
		dfs(g, minute + 1, rate + new)

	# see what happens if we open the current valve

	if curr in opened:
		return

	opened.add(curr)
	dfs(curr, minute + 1, rate + sum(v[0] for k, v in valves.items() if k in opened))
	opened.remove(curr)

SOURCE = "AA"
dfs(SOURCE, 1, 0)
print(max(candidates))

# part 2

opened = set()
visited = {}
candidates = set()

def dfs2(cur1, cur2, minute, rate):
	# do we have time left?

	if minute == 26:
		candidates.add(rate)
		return

	# check we haven't yet encountered this condition

	if (cur1, cur2, minute) in visited and visited[(cur1, cur2, minute)] >= rate:
		return

	visited[(cur1, cur2, minute)] = rate

	if valves[cur1][0] and not valves[cur1][4]:
		valves[cur1][4] = True

		goes_to = valves[cur2][1]
		new = sum(v[0] for k, v in valves.items() if v[4])

		for g in goes_to:
			dfs2(cur1, g, minute + 1, rate + new)
		
		if valves[cur2][0] and not valves[cur2][4]:
			valves[cur2][4] = True
			dfs2(cur1, cur2, minute + 1, rate + sum(v[0] for k, v in valves.items() if v[4]))
			valves[cur2][4] = False

		valves[cur1][4] = False

	goes_to = valves[cur1][1]

	for g in goes_to:
		goes_to = valves[cur2][1]
		new = sum(v[0] for k, v in valves.items() if v[4])

		for c in goes_to:
			dfs2(g, c, minute + 1, rate + new)

		if not valves[cur2][0] or valves[cur2][4]:
			continue

		valves[cur2][4] = True
		dfs2(g, cur2, minute + 1, rate + sum(v[0] for k, v in valves.items() if v[4]))
		valves[cur2][4] = False

SOURCE = "AA"
dfs2(SOURCE, SOURCE, 1, 0)
print(max(candidates))

# sad that this didn't work out 😥

exit(0)

def best(source):
	adjusted = deepcopy(valves)

	# bfs

	adjusted[source][0] = 0
	queue = deque()
	queue.append(source)
	visited = set((source))

	while queue:
		curr = queue[0]
		queue.popleft()
		goes_to = adjusted[curr][1]

		for g in goes_to:
			if g in visited:
				continue

			adjusted[g][0] += adjusted[curr][0] # add parent's rate as compensation
			adjusted[g][2] = adjusted[curr][2] + 1
			adjusted[g][0] /= adjusted[g][2]

			adjusted[g][3] = adjusted[curr][3] + [curr]

			queue.append(g)
			visited.add(g)

	best = (source, 0, [])
	best_cost = 0

	for k, v in adjusted.items():
		cost, _, layer, trail = v

		if cost > best_cost:
			best_cost = cost
			best = (k, layer, trail)
	
	return best

orig = deepcopy(valves)
valve = SOURCE
target = None
trail = []
layer = 0
pressure = 0
opened = set()

print("START")

for i in range(30):
	for o in opened:
		pressure += orig[o][0]

	# find target

	if target is None:
		target, layer, trail = best(valve)
		layer -= 1

	# got to target

	elif layer:
		print(i + 1, "MOVE", target)
		layer -= 1

	# found target

	else:
		print(i + 1, "OPEN " + target)
		valve = target
		valves[valve][0] = 0
		opened.add(valve)
		target = None

	print(target, trail)

print(pressure)
__import__("time").sleep(0.5)
