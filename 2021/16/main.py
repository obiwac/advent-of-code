import math

f = "".join(bin(int(x, 16))[2:].zfill(4) for x in open(0).read().strip())

s = 0
ptr = 0

def rd(i):
	global ptr
	res = f[ptr:i+ptr]
	ptr += i
	return int(res, 2)

def packet():
	global s

	version = rd(3)
	s += version
	typeid = rd(3)

	if typeid == 4:
		num = 0

		while rd(1):
			num |= rd(4)
			num <<= 4
		
		return num | rd(4)
	
	lentypeid = rd(1)
	l = []

	if lentypeid:
		subpackets = rd(11)

		for _ in range(subpackets):
			l.append(packet())

	else:
		length = rd(15)

		while length:
			pp = ptr
			l.append(packet())
			length -= ptr - pp
	
	return {
		0: sum,
		1: math.prod,
		2: min,
		3: max,
		5: lambda l: l[0] > l[1],
		6: lambda l: l[0] < l[1],
		7: lambda l: l[0] == l[1],
	}[typeid](l)

print(packet())
print(s)