import math
from itertools import chain
from itertools import accumulate
from functools import reduce
from collections import Counter
from collections import defaultdict
from copy import deepcopy

import numpy as np

PART = 2

f = open(0).read().strip().split('\n\n')

monkeys = []
lcm = 1
new = 0

class Monkey:
	def __init__(self, id, s, op, divisor, true_cnd, false_cnd):
		self.id = id
		self.s = s

		self.op = op
		self.divisor = divisor
		self.true_cnd = true_cnd
		self.false_cnd = false_cnd

		self.inspected = 0
	
	def inspect(self, worry):
		old = worry
		exec("global new;" + self.op)
		worry = new % lcm if PART == 2 else new // 3

		if worry % self.divisor:
			monkeys[self.false_cnd].s.append(worry)

		else:
			monkeys[self.true_cnd].s.append(worry)

		self.inspected += 1
		self.s.remove(old)

# parse

for monkey in f:
	lines = monkey.strip().split('\n')
	_, n = lines[0].split()
	n = int(n.strip(':'))

	s = lines[1].strip().split()[2:]
	*s, = map(lambda x: int(x.strip(',')), s)

	op = lines[2].strip()[len("Operation: "):]
	divisor = int(lines[3].strip()[len("Test: divisible by "):])

	true_cnd = int(lines[4].strip()[len("If true: throw to monkey ")])
	false_cnd = int(lines[5].strip()[len("If false: throw to monkey ")])

	lcm *= divisor
	monkeys.append(Monkey(n, s, op, divisor, true_cnd, false_cnd))

# run

for i in range((20, 10000)[PART == 2]):
	for monkey in monkeys:
		for worry in list(monkey.s):
			monkey.inspect(worry)

	for monkey in monkeys:
		if not i % 1000:
			print(i, monkey.inspected)

# final answer

a, b = sorted(map(lambda x: x.inspected, monkeys))[-2:]
print(a, b)
print(a * b)
__import__("time").sleep(0.1)
