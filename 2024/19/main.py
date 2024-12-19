from functools import cache

patterns, designs = open(0).read().strip().split("\n\n")

patterns = patterns.split(", ")
designs = designs.split("\n")

poss = 0
s = 0

@cache
def dfs(design):
	if len(design) == 0:
		return 1

	count = 0

	for pattern in patterns:
		if design.startswith(pattern):
			count += dfs(design[len(pattern):])

	return count

for design in designs:
	d = dfs(design)

	s += d
	poss += d > 0

print(poss)
print(s)
