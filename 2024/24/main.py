from itertools import chain

reg, instr = open(0).read().strip().split("\n\n")
regs = {}

for r in reg.split("\n"): 
	name, val = r.split(": ")
	regs[name] = int(val)

instr = instr.split("\n")

def valof(regs, name):
	x = ""

	for r in reversed(sorted(regs.keys())):
		if r[0] == name:
			x += str(regs[r])

	return int(x, 2)

def setreg(name, val):
	for r in sorted(regs.keys()):
		if r[0] == name:
			regs[r] = val & 1
			val >>= 1

def run(instr, x, y):
	setreg("x", x)
	setreg("y", y)

	wregs = dict(regs)
	remaining = list(instr)

	while remaining:
		for r in remaining:
			a, op, b, _, out = r.split()

			if a not in wregs or b not in wregs:
				continue

			if op == "AND":
				wregs[out] = wregs[a] & wregs[b]

			elif op == "OR":
				wregs[out] = wregs[a] | wregs[b]
			
			elif op == "XOR":
				wregs[out] = wregs[a] ^ wregs[b]

			remaining.remove(r)
			break

		else:
			break

	return valof(wregs, "z")

def find_pairs(instr, x, y, z):
	pairs = []

	for i in range(len(instr)):
		for j in range(i + 1, len(instr)):
			ninstr = instr.copy()

			op1, out1 = ninstr[i].split(" -> ")
			op2, out2 = ninstr[j].split(" -> ")

			ninstr[i] = f"{op1} -> {out2}"
			ninstr[j] = f"{op2} -> {out1}"

			if run(ninstr, x, y) == z:
				print("Found pair", i, j)
				pairs.append((i, j))

	return pairs

# Find issues.

from issues import issues
from collections import Counter

counter = Counter(chain.from_iterable(issues))
print(len(counter))
exit()

j = 0

for i in range(45): # Registers seem to be 45 bits long
	bit = 1 << i

	if run(instr, 0, 0) != 0:
		print("0, 0 issue at", i, bit, run(instr, 0, 0))
		print(issues[j])
		j += 1

	if run(instr, bit, 0) != bit:
		print("1, 0 issue at", i, bit, run(instr, bit, 0))
		print(issues[j])
		j += 1

	if run(instr, 0, bit) != bit:
		print("1, 0 issue at", i, bit, run(instr, 0, bit))
		print(issues[j])
		j += 1

	if run(instr, bit, bit) != bit << 1:
		print("1, 1 issue at", i, bit, run(instr, bit, bit))
		print(issues[j])
		j += 1

exit()

print(issues)

import pickle

with open("issues.pickle", "wb") as f:
	pickle.dump(issues, f)
