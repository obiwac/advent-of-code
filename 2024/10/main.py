f = open(0).read().strip().split("\n")
m = []

for l in f:
	m.append(list(map(int, l)))

def dfs(i, j, prev, path):
	if i < 0 or i >= len(m) or j < 0 or j >= len(m[i]):
		return set()

	if m[i][j] != prev + 1:
		return set()

	if (i, j) in path:
		return set()

	if m[i][j] == 9:
		return {(i, j)}

	nines = set()
	npath = path + [(i, j)]

	nines |= dfs(i - 1, j, m[i][j], npath)
	nines |= dfs(i + 1, j, m[i][j], npath)
	nines |= dfs(i, j - 1, m[i][j], npath)
	nines |= dfs(i, j + 1, m[i][j], npath)

	return nines

s = 0

for i in range(len(m)):
	for j in range(len(m[i])):
		if m[i][j] == 0:
			score = dfs(i, j, -1, [])
			s += len(score)

print(s)
