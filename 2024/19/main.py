from functools import cache

patterns, designs = open(0).read().strip().split("\n\n")

patterns = patterns.split(", ")
designs = designs.split("\n")

poss = 0
s = 0

@cache
def is_poss(design):
	if len(design) == 0:
		return True

	for pattern in patterns:
		if design.startswith(pattern):
			if is_poss(design[len(pattern):]) == True:
				return True

	return False

@cache
def design_count(design):
	if len(design) == 0:
		return 1

	count = 0

	for pattern in patterns:
		if design.startswith(pattern):
			count += design_count(design[len(pattern):])

	return count

for design in designs:
	print(design)

	if is_poss(design):
		poss += 1
		s += design_count(design)

print(poss)
print(s)
