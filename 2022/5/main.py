import math
from itertools import chain
from itertools import accumulate
from functools import reduce
from collections import Counter
from collections import defaultdict

import numpy as np

f = open(0).read().split('\n\n')

# part 1

stacks_raw = f[0].split('\n')
stack_len = len(stacks_raw[-1].split())

stacks = [[] for _ in range(stack_len)]

for row in reversed(stacks_raw[:-1]):
	for i in range(stack_len):
		elem = row[i * 4: i * 4 + 4].strip()

		if elem:
			stacks[i].append(elem[1])

for step in f[1].strip().split('\n'):
	_, move, _, from_, _, to = step.split()

	move = int(move)
	from_ = int(from_)
	to = int(to)

	bit = stacks[from_ - 1][-move:]
	stacks[from_ - 1] = stacks[from_ - 1][:-move]
	stacks[to - 1].extend(reversed(bit))

s = ""

for stack in stacks:
	top = stack[-1]
	s += top

print(s)

# part 1

stacks_raw = f[0].split('\n')
stack_len = len(stacks_raw[-1].split())

stacks = [[] for _ in range(stack_len)]

for row in reversed(stacks_raw[:-1]):
	for i in range(stack_len):
		elem = row[i * 4: i * 4 + 4].strip()

		if elem:
			stacks[i].append(elem[1])

for step in f[1].strip().split('\n'):
	_, move, _, from_, _, to = step.split()

	move = int(move)
	from_ = int(from_)
	to = int(to)

	bit = stacks[from_ - 1][-move:]
	stacks[from_ - 1] = stacks[from_ - 1][:-move]
	stacks[to - 1].extend(bit)

s = ""

for stack in stacks:
	top = stack[-1]
	s += top

print(s)
