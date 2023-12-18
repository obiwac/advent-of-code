from functools import reduce

raw_workflows, ratings = open(0).read().strip().split('\n\n')
workflows = {}

INSTR_NORMAL = 0
INSTR_END = 1

class Instruction:
	def __init__(self, kind, next, condition = None):
		self.kind = kind
		self.condition = condition
		self.next = next

for workflow in raw_workflows.split("\n"):
	name, rest = workflow.split("{")
	instructions = []

	for instruction in rest[:-1].split(","):
		if ":" not in instruction:
			instructions.append(Instruction(INSTR_END, instruction))
			continue

		condition, next = instruction.split(":")
		instructions.append(Instruction(INSTR_NORMAL, next, condition))

	workflows[name] = instructions

# part 1

s = 0

for raw_rating in ratings.split("\n"):
	rating = {}

	for r in raw_rating[1: -1].split(","):
		k, v = r.split("=")
		rating[k] = int(v)

	workflow = workflows["in"]
	accepted = False

	while 1:
		stop = False

		for instr in workflow:
			go_ahead = instr.kind == INSTR_END

			if instr.kind == INSTR_NORMAL:
				condition = str(instr.condition)

				for k, v in rating.items():
					condition = condition.replace(k, str(v))

				go_ahead = eval(condition)

			if go_ahead:
				if instr.next == "A":
					accepted = True
					stop = True
					break

				if instr.next == "R":
					stop = True
					break

				workflow = workflows[instr.next]
				break

		if stop:
			break

	if accepted:
		s += sum(rating.values())

print(s)

# part 2 - I'm sure there's a better way without having to build a whole tree :)

class Tree:
	def __init__(self, name, accepted, rejected, condition, leaf_accepted = None):
		self.name = name
		self.accepted = accepted
		self.rejected = rejected
		self.condition = condition
		self.parent = None
		self.leaf_accepted = leaf_accepted

	def __repr__(self):
		if self.leaf_accepted == True:
			return "ACCEPT"

		if self.leaf_accepted == False:
			return "REJECT"

		return f"{self.name}({self.accepted}, {self.rejected}, {self.condition})"

accepted = []
rejected = []

def recurse(name):
	global accepted

	if name == "A":
		leaf = Tree(None, None, None, None, True)
		accepted.append(leaf)
		return leaf

	if name == "R":
		leaf = Tree(None, None, None, None, False)
		rejected.append(leaf)
		return leaf

	suite = None

	for instruction in workflows[name][::-1]:
		if instruction.kind == INSTR_END:
			assert suite is None
			suite = recurse(instruction.next)

		if instruction.kind == INSTR_NORMAL:
			assert suite is not None
			suite = Tree(name, recurse(instruction.next), suite, instruction.condition)

	return suite

tree = recurse("in")

# set parents

def dfs(tree):
	if tree.accepted is not None:
		tree.accepted.parent = tree
		dfs(tree.accepted)

	if tree.rejected is not None:
		tree.rejected.parent = tree
		dfs(tree.rejected)

dfs(tree)

s = 0

for accept in accepted:
	allowed = {k: [True for _ in range(4000)] for k in "xmas"}
	conditions = []

	while accept.parent is not None:
		flip = accept != accept.parent.rejected

		accept = accept.parent
		condition = accept.condition

		part = condition[0]
		op = condition[1]
		threshold = int(condition[2:])

		if flip and op == ">": op = "<="
		elif flip and op == "<": op = ">="

		conditions.append((part, op, threshold))

	for part, op, threshold in conditions:
		rng = {
			"<": range(threshold - 1),
			">": range(threshold, 4000),
			"<=": range(threshold),
			">=": range(threshold - 1, 4000)
		}[op]

		for i in rng:
			allowed[part][i] = False

	for k in allowed:
		allowed[k] = sum(allowed[k])

	s += reduce(lambda x, y: x * y, allowed.values())

print(s)
