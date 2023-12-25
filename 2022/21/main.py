import math
from itertools import chain
from itertools import accumulate
from functools import reduce
from collections import Counter
from collections import defaultdict
from copy import deepcopy

import numpy as np
import heapq

f = open(0).read().strip().split('\n')
monkeys = {}

for l in f:
	name, job = l.split(': ')
	monkeys[name] = job

def say(name):
	job = monkeys[name]

	if job.isnumeric():
		return int(job)

	bits = job.split()

	a = say(bits[0])
	b = say(bits[2])
	o = bits[1]

	if o == '+': return a + b
	if o == '-': return a - b
	if o == '*': return a * b
	if o == '/': return a / b

def has_dep(name, dep = "humn"):
	job = monkeys[name]

	if job.isnumeric():
		return False

	a, _, b = job.split()

	if dep in (a, b):
		return True

	return has_dep(a, dep) or has_dep(b, dep)

def equation(name):
	job = monkeys[name]

	if job.isnumeric():
		return int(job)

	a, op, b = job.split()

	if a != "humn": a = equation(a)
	if b != "humn": b = equation(b)

	return f"({a}{op}{b})"

def back(fit, want):
	print(fit, want)

print(int(say("root"))) # p1
a, _, b = monkeys["root"].split() # we want a & b to be equal

if has_dep(a):
	fit = a
	want = int(say(b))

elif has_dep(b):
	fit = b
	want = int(say(a))

from sympy.solvers import solve
from sympy import Symbol

print(solve(f"{equation(fit)}-{want}", Symbol("humn"))[0]) # p2
