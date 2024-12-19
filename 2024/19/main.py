from functools import cache

patterns, designs = open(0).read().strip().split("\n\n")

patterns = patterns.split(", ")
designs = designs.split("\n")

poss = 0

@cache
def is_poss(design):
	if len(design) == 0:
		return True

	for pattern in patterns:
		if design.startswith(pattern):
			if is_poss(design[len(pattern):]) == True:
				return True

	return False

for design in designs:
	print(design)
	poss += is_poss(design)

print(poss)
