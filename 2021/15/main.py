import heapq

o = [[*map(lambda y: int(y), x)] for x in map(str.strip, open(0).read().strip().split('\n'))]
f = o

for r in range(5):
	for l in o:
		row = []

		for t in range(5):
			row.extend(map(lambda x: (x - 1 + t + r) % 9 + 1, l))

		f.append(row)

unvisited = []
dists = [[9999] * len(f[0]) for _ in f]

def visit(x, y, risk):
	if not x in range(len(f[0])) or not y in range(len(f)):
		return
	
	if dists[y][x] <= risk + f[y][x]:
		return

	dist = risk + f[y][x]
	heapq.heappush(unvisited, (dist, (x, y)))

	dists[y][x] = dist

visit(0, 0, -f[0][0])

while unvisited:
	risk, (x, y) = heapq.heappop(unvisited)

	for p in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
		visit(*p, risk)

print(dists[-1][-1])
