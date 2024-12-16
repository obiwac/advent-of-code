from functools import cache

*f, = map(list, open(0).read().strip().split("\n"))

walls = set()
start = None
end = None

for i in range(len(f)):
	for j in range(len(f[i])):
		if f[i][j] == "#":
			walls.add((i, j))

		if f[i][j] == "E":
			end = (i, j)

		if f[i][j] == "S":
			start = (i, j)

assert start is not None
assert end is not None

DIRS = ((0, 1), (0, -1), (1, 0), (-1, 0))
q = [start + (2,)]
dist = [[[float("inf")] * len(f) for _ in range(len(f[0]))] for _ in range(4)]

for i in range(4):
	dist[i][start[0]][start[1]] = 0

while q:
	cx, cy, cd = q.pop(0)

	for d, (dx, dy) in enumerate(DIRS):
		nx, ny = cx + dx, cy + dy
		cost = 1 + (1000 if cd != d else 0)

		if 0 <= nx < len(f) and 0 <= ny < len(f[0]) and (nx, ny) not in walls and dist[cd][cx][cy] + cost < dist[d][nx][ny]:
			dist[d][nx][ny] = dist[cd][cx][cy] + cost
			q.append((nx, ny, d))

print(min(dist[i][end[0]][end[1]] for i in range(4)))

"""
states = {}

def dfs(cur, cost, path = []):
	if tuple(path) in states:
		return states[tuple(path)]

	cx, cy = cur
	candidates = []

	for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
		nx, ny = cx + dx, cy + dy
		pdx, pdy = path[-1][0] - cx, path[-1][1] - cy

		if pdx == -dx or pdy == -dy: # Disallow 180 deg turns.
			continue

		if 0 <= nx < len(f) and 0 <= ny < len(f[0]) and (nx, ny) not in walls and (nx, ny) not in path:
			nc = cost + 1

			if (dx, dy) != (pdx, pdy):
				nc += 1000

			if (nx, ny) == end:
				print(len(path) + 1)
				exit()

			candidates.append(dfs((nx, ny), nc, path + [(nx, ny)]))

	states[tuple(path)] = min(candidates, default=float("inf"))
	return states[tuple(path)]

print(dfs(start, 0))
"""
