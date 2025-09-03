f = open(0).read().strip().split("\n")

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

for c in cliques:
	print(c)
print(len((*filter(lambda c: len(c) == 3 and any(v[0] == "t" for v in c), cliques),)))
print(",".join(sorted(list(max(cliques, key=len)))))
