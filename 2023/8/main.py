*f, = open(0).read().strip().split('\n')

instructions = f[0]
nodes_raw = f[2:]

nodes = {}

for node_raw in nodes_raw:
	name, _, left, right = node_raw.split()
	left = left[1: -1]
	right = right[:-1]

	nodes[name] = (left, right)

cur = "AAA"
i = 0

while cur != "ZZZ":
	if instructions[i % len(instructions)] == "L":
		cur = nodes[cur][0]

	else:
		cur = nodes[cur][1]

	i += 1

print(i)
