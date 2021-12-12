from itertools import chain
from itertools import accumulate
from functools import reduce
from collections import Counter
from operator import mul

_f = [x.split('-') for x in map(str.strip, open(0).read().strip().split('\n'))]
f = {}

for c in _f:
	if c[0] not in f:
		f[c[0]] = []

	f[c[0]].append(c[1])

	if c[1] not in f:
		f[c[1]] = []

	f[c[1]].append(c[0])

# print(f)

paths = []

def recurse(f, path, c, m, h):
	global paths

	if "end" in path:
		return

	for branch in f[c]:
		if branch == "start": # TODO necessary?
			continue

		if branch.islower() and path.count(branch) > m - 1:
			continue

		if branch in f:
			recurse(f, path + [branch], branch, 1, h)
			built = path + [branch]
			
			if "end" in built:
				paths.append(built)
			
			if not h:
				recurse(f, path + [branch], branch, 2, True)
				built = path + [branch]
				
				if "end" in built:
					paths.append(built)

searching = True

recurse(f, [], "start", 1, False)

print(len(set(map(str, paths))))
