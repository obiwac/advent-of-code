from itertools import chain
from itertools import accumulate
from functools import reduce
from collections import Counter
from operator import mul

f = "".join(bin(int(x, 16))[2:].zfill(4) for x in open(0).read().strip())

s = 0
ptr = 0

def rd(i):
	global f, ptr
	res = f[ptr:i+ptr]
	ptr += i
	return res

def packet():
	global s, ptr

	version = int(rd(3), 2)
	s += version
	typeid = int(rd(3), 2)

	val = 0

	if typeid == 4: # literal value
		num = ""

		while int(rd(1), 2):
			num += rd(4)
		
		num += rd(4)
		val = int(num, 2)
	
	else: # operator
		lentypeid = int(rd(1), 2)

		op = {
			0: "sum",
			1: "prod",
			2: "min",
			3: "max",
			5: "gt",
			6: "lt",
			7: "eq",
		}[typeid]

		l = []

		if lentypeid:
			subpackets = int(rd(11), 2)

			for _ in range(subpackets):
				l.append(packet())
	
		else:
			length = int(rd(15), 2)

			while length:
				pp = ptr
				l.append(packet())
				length -= ptr - pp
		
		if op == "sum": l = sum(l)
		if op == "prod": l = reduce(lambda x, y: x * y, l)
		if op == "min": l = min(l)
		if op == "max": l = max(l)
		if op == "gt": l = l[0] > l[1]
		if op == "lt": l = l[0] < l[1]
		if op == "eq": l = l[0] == l[1]

		val = l
	
	return val

print(packet())
print(s)