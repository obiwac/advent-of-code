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

A = {}

for l in f:
	a, b = l.split("-")

	if a not in A:
		A[a] = set()

	if b not in A:
		A[b] = set()

	A[a].add(b)
	A[b].add(a)

cliques = set()

def bron_kerbosch(R, P, X): # From Wikipedia.
	if not P and not X:
		cliques.add(frozenset(R))

	for v in set(P):
		bron_kerbosch(R | {v}, P & A[v], X & A[v])
		P.remove(v)
		X.add(v)

bron_kerbosch(set(), set(A.keys()), set())
print(",".join(sorted(list(max(cliques, key=len)))))
