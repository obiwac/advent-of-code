from collections import OrderedDict

i = [0, 3, 6]
turns = OrderedDict()

before_to_last_spoken = {}
last_spoken = {}

j = 0
while j < len(i):
	turns[j] = i[j]
	last_spoken[turns[j]] = j
	j += 1

while j < 10:
	v = list(turns.values())[-1]
	
	if v in before_to_last_spoken.keys():
		turns[j] = last_spoken[v] - before_to_last_spoken[v]
	
	else:
		turns[j] = 0
	
	if turns[j] in last_spoken.keys():
		before_to_last_spoken[turns[j]] = last_spoken[turns[j]]
	last_spoken[turns[j]] = j

	if 1 in last_spoken: print(j, turns[j], last_spoken[1])
	else: print(j, turns[j], -1)

	j += 1

print(f"part 1: {list(turns.values())[-1]}")