f = open(0).read().strip().split("\n")

edges = set()
verts = set()

for l in f:
	a, b = l.split("-")
	edges.add((a, b))
	verts.add(a)
	verts.add(b)

triples = set()

for u, v in edges:
	for w in verts:
		if (u, w) in edges and (w, v) in edges:
			if u[0] == "t" or v[0] == "t" or w[0] == "t":
				triples.add(frozenset((u, v, w)))
		if (v, w) in edges and (w, u) in edges:
			if u[0] == "t" or v[0] == "t" or w[0] == "t":
				triples.add(frozenset((u, v, w)))

print(len(triples))
