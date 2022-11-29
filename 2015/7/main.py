f = open(0).readlines()

wires = {}

def tok(s):
	try:
		return int(s)

	except:
		return wires.get(s, 0)

for l in f:
	l = l.strip().split()

	if l[1] == '->': wires[l[2]] = tok(l[0])
	elif l[0] == 'NOT': wires[l[3]] = tok(l[1]) ^ 0b1111111111111111
	elif l[1] == 'AND' and l[0] in wires and l[2] in wires: wires[l[4]] = tok(l[0]) & tok(l[2])
	elif l[1] == 'OR' and l[0] in wires and l[2] in wires: wires[l[4]] = tok(l[0]) | tok(l[2])
	elif l[1] == 'LSHIFT' and l[0] in wires and l[2] in wires: wires[l[4]] = tok(l[0]) << tok(l[2])
	elif l[1] == 'RSHIFT' and l[0] in wires and l[2] in wires: wires[l[4]] = tok(l[0]) >> tok(l[2])

print(wires)
print(wires.get('a', 0))
