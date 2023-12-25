from itertools import chain
from itertools import accumulate
from functools import reduce
from collections import Counter
from operator import mul

instrs = [x.split(' ') for x in map(str.strip, open(0).read().strip().split('\n'))]

def test_model_num(model_num):
	regs = {
		'x': 0,
		'y': 0,
		'z': 0,
		'w': 0
	}

	def proc_operand(x):
		if x in regs.keys():
			return regs[x]
		
		return int(x)

	for opcode, *operands in instrs:
		if opcode == 'inp':
			regs[operands[0]] = int(model_num[0])
			model_num = model_num[1:]

		if opcode == 'brk':
			print("BREAKPOINT", regs)

		if opcode == 'add':
			regs[operands[0]] += proc_operand(operands[1])
		
		if opcode == 'mul':
			regs[operands[0]] *= proc_operand(operands[1])
		
		if opcode == 'div':
			regs[operands[0]] //= proc_operand(operands[1])
		
		if opcode == 'mod':
			regs[operands[0]] %= proc_operand(operands[1])
		
		if opcode == 'eql':
			regs[operands[0]] = int(regs[operands[0]] == proc_operand(operands[1]))

	return regs

PARAMS = [
	(1, 14, 12),
	(1, 11, 8),
	(1, 11, 7),
	(1, 14, 4),
	(26, -11, 4),
	(1, 12, 1),
	(26, -1, 10),
	(1, 10, 8),
	(26, -3, 12),
	(26, -4, 10),
	(26, -13, 15),
	(26, -8, 4),
	(1, 13, 10),
	(26, -11, 9),
]

def rev(model_num):
	z = 0

	for i, d in enumerate(model_num):
		w = int(d)
		x = z % 26 + PARAMS[i][1]
		z = int(z / PARAMS[i][0])

		if x != w:
			z = z * 26 + w + PARAMS[i][2]
	
	return z

# for p in range(14):
# 	for d in range(1, 10):
# 		num = list("9" * 14)
# 		num[p] = str(d)

# 		regs = test_model_num("".join(num))

# 		if regs['z'] == 0:
# 			print("STOP", num)
# 			exit()

# 		print(p, regs)


# x = z % 26 + 14
# if x != w: z = z * 26 + w + 12

# x = z % 26 + 11
# if x != w: z = z * 26 + w + 7

num = list("9" * 14)
# num[0] = 9
# num[1] = 1
# num[7] = 4
# num[2] = 2
num[4] = 2
num[6] = 9
num[8] = 1
num[9] = 9
num[10] = 3
num[11] = 9
num[13] = 8

D = [0, 1, 2, 3, 5, 7, 12]

v = int('9' * len(D))
# v = int('9' * 14)
m = "---"

import os

while v:
	s = str(v)

	if '0' in s:
		v -= 1
		# print(m)
		continue

	# num = s
	num[0] = s[0]
	num[1] = s[1]
	num[2] = s[2]
	num[3] = s[3]
	num[5] = s[4]
	num[7] = s[5]
	num[12] = s[6]

	m = "".join(map(str, num))

	# print(m)

	e = rev(m)

	if e == 0:
		print(m)
		os.system(f"echo {m} > /tmp/solutino")
		exit()

	v -= 1

m = "".join(map(str, num))
print(test_model_num(m))
print("====", m)

# for d in range(9):
# 	for p in range(10)

# v = int('9' * 14)

# while v:
# 	s = str(v)

# 	if '0' in s:
# 		v -= 1
# 		continue

# 	print("test", s)

# 	if test_model_num(s) == 0:
# 		print(s)
# 		exit()

# 	v -= 1