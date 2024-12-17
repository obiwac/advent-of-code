registers_raw, program_raw = open(0).read().strip().split("\n\n")
registers = {}

for l in registers_raw.split("\n"):
	_, name, val = l.split()
	name = name[:-1]
	val = int(val)
	registers[name] = val

*program, = map(int, program_raw.split()[1].split(","))

ip = 0
out = []

while ip < len(program):
	opcode = program[ip]
	ip += 1

	if opcode == 0:
		operand = program[ip]
		ip += 1

		if operand > 3 and operand < 7:
			operand = registers[{4: "A", 5: "B", 6: "C"}[operand]]

		registers["A"] = int(registers["A"] / (2 ** operand))

	elif opcode == 1:
		operand = program[ip]
		ip += 1
		registers["B"] = registers["B"] ^ operand

	elif opcode == 2:
		operand = program[ip]
		ip += 1

		if operand > 3 and operand < 7:
			operand = registers[{4: "A", 5: "B", 6: "C"}[operand]]

		registers["B"] = operand % 8

	elif opcode == 3:
		operand = program[ip]
		ip += 1

		if registers["A"] != 0:
			ip = operand

	elif opcode == 4:
		ip += 1
		registers["B"] = registers["B"] ^ registers["C"]

	elif opcode == 5:
		operand = program[ip]
		ip += 1

		if operand > 3 and operand < 7:
			operand = registers[{4: "A", 5: "B", 6: "C"}[operand]]


		out.append(operand % 8)

	elif opcode == 6:
		operand = program[ip]
		ip += 1

		if operand > 3 and operand < 7:
			operand = registers[{4: "A", 5: "B", 6: "C"}[operand]]

		registers["B"] = int(registers["A"] / (2 ** operand))

	elif opcode == 7:
		operand = program[ip]
		ip += 1

		if operand > 3 and operand < 7:
			operand = registers[{4: "A", 5: "B", 6: "C"}[operand]]

		registers["C"] = int(registers["A"] / (2 ** operand))

print(",".join(map(str, out)))
