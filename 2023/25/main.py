import graphviz

# can use xdot to view the graph

dot = graphviz.Graph(comment="Wires")
*f, = map(str, open(0).read().strip().split('\n'))

adj = {}
wires = []

no = [
		frozenset(["bbp", "dvr"]),
		frozenset(["tzj", "gtj"]),
		frozenset(["jzv", "qvq"]),
		# frozenset(["hfx", "pzl"]),
		# frozenset(["bvb", "cmg"]),
		# frozenset(["nvd", "jqt"]),
]

for l in f:
	a, b = l.split(": ")
	b = b.split()

	for c in b:
		if frozenset((c, a)) in no:
			continue

		if a not in adj:
			adj[a] = []

		adj[a].append(c)

		if c not in adj:
			adj[c] = []

		adj[c].append(a)

	dot.node(a, a)

	for c in b:
		dot.edge(a, c, tooltip=f"{a} -> {c}")

# left BFS

visited = set()
q = [[*adj.keys()][0]]

while q:
	cur = q.pop(0)

	for n in adj[cur]:
		if n not in visited:
			visited.add(n)
			q.append(n)

print(len(visited))

print(len(adj) - len(visited))

# for i in range(len(wires)):
# 	for j in range(i + 1, len(wires)):
# 		for k in range(j + 1, len(wires)):
# 			a, b = wires[i]
# 			c, d = wires[j]
# 			e, f = wires[k]
# 
# 	print(i)

# dot.render('out.gv', view=True)

# bbp -> dvr
# tzj -> gti
# jzv -> qvq
