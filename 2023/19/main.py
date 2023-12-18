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
