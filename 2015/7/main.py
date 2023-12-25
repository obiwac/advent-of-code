f = open(0).readlines()

wires = {}

def tok(s):
	try:
		return int(s)

	except:
		return wires.get(s, 0)

OP_SET = 0
OP_NOT = 1
OP_AND = 2
OP_OR  = 3
OP_LSH = 4
OP_RSH = 5

class Wire:
	def __init__(self, op, left, right = None):
		self.op = op

		self.left = tok(left)
		self.right = tok(right)

	def eval(self):
		if self.op == OP_SET: return self.left if type(self.left) == int else self.left.eval()
		if self.op == OP_NOT: return self.left.eval() ^ 0b1111111111111111
		if self.op == OP_AND: return self.left.eval() & self.right.eval()
		if self.op == OP_OR: return self.left.eval() | self.right.eval()
		if self.op == OP_LSH: return self.left.eval() << self.right.eval()
		if self.op == OP_RSH: return self.left.eval() >> self.right.eval()

		return self.val

for l in f:
	l = l.strip().split()

	if l[1] == '->': wires[l[2]] = Wire(OP_SET, l[0])
	elif l[0] == 'NOT': wires[l[3]] = Wire(OP_NOT, l[1])
	elif l[1] == 'AND': wires[l[4]] = Wire(OP_AND, l[0], l[2])
	elif l[1] == 'OR': wires[l[4]] = Wire(OP_OR, l[0], l[2])
	elif l[1] == 'LSHIFT': wires[l[4]] = Wire(OP_LSH, l[0], l[2])
	elif l[1] == 'RSHIFT': wires[l[4]] = Wire(OP_RSH, l[0], l[2])

print(wires.get('a', 0).eval())

