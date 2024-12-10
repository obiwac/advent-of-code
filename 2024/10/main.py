f = open(0).read().strip().split("\n")
m = []

for l in f:
	m.append(list(map(int, l)))

def dfs(i, j, prev, path):
	if i < 0 or i >= len(m) or j < 0 or j >= len(m[i]):
		return set(), 0

	if m[i][j] != prev + 1:
		return set(), 0

	if (i, j) in path:
		return set(), 0

	if m[i][j] == 9:
		return {(i, j)}, 1

	nines = set()
	tot = 0
	npath = path + [(i, j)]

	nines, tot = (lambda x: (nines | x[0], tot + x[1]))(dfs(i - 1, j, m[i][j], npath))
	nines, tot = (lambda x: (nines | x[0], tot + x[1]))(dfs(i + 1, j, m[i][j], npath))
	nines, tot = (lambda x: (nines | x[0], tot + x[1]))(dfs(i, j - 1, m[i][j], npath))
	nines, tot = (lambda x: (nines | x[0], tot + x[1]))(dfs(i, j + 1, m[i][j], npath))

	return nines, tot

p1 = 0
p2 = 0

for i in range(len(m)):
	for j in range(len(m[i])):
		if m[i][j] == 0:
			score, rating = dfs(i, j, -1, [])
			p1 += len(score)
			p2 += rating

print(p1)
print(p2)
