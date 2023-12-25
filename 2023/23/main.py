import sys
sys.setrecursionlimit(10000)

*f, = map(list, open(0).read().strip().split('\n'))
w, h = len(f[0]), len(f)

slopes = "v>^<"
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)] 
s = (1, 0)

"""
q = [s]
visited = [[False] * w for _ in range(h)]
visited[0][1] = True
nodes = [s]

while q:
	x, y = q.pop()
	branches = 0

	for i, (dx, dy) in enumerate(dirs):
		nx, ny = x + dx, y + dy

		if 0 <= nx < w and 0 <= ny < h and not visited[ny][nx]:
			visited[ny][nx] = True

			if f[ny][nx] == '.' or f[ny][nx] in slopes:
				q.append((nx, ny))
				branches += 1

	if branches > 1:
		nodes.append((x, y))

graph = {}
visited = [[False] * w for _ in range(h)]

for x, y in nodes:
	q = [(x, y)]
	visited[y][x] = True
	graph[(x, y)] = []

	while q:
		x, y = q.pop()

		for i, (dx, dy) in enumerate(dirs):
			nx, ny = x + dx, y + dy

			if 0 <= nx < w and 0 <= ny < h and not visited[ny][nx]:
				visited[ny][nx] = True

				if f[ny][nx] == '.' or f[ny][nx] in slopes:
					q.append((nx, ny))
					graph[(x, y)].append((nx, ny))

"""
d = {}
paths = []
lowest_depth = float("inf")

def r(x, y, di = 0, path = ()):
	state = (x, y, di, len(path))

	if state in d:
		return d[state]

	if (x, y) == (w - 2, h - 1):
		return len(path)

	paths.append(path)
	candidates = [0]

	for i, (dx, dy) in enumerate(dirs):
		if i == (di + 2) % 4:
			continue

		nx, ny = x + dx, y + dy

		if 0 <= nx < w and 0 <= ny < h and not (nx, ny) in path:
			if f[ny][nx] == '.' or f[ny][nx] in slopes:
				candidates.append(r(nx, ny, i, path + ((x, y),)))

			elif f[ny][nx] in slopes:
				# can't go up a slope

				if slopes.index(f[ny][nx]) == (i + 2) % 4:
					continue

				# otherwise, go hella down

				slope_di = slopes.index(f[ny][nx])
				slope_dx, slope_dy = dirs[slope_di]
				slope_nx = nx + slope_dx
				slope_ny = ny + slope_dy
				candidates.append(r(slope_nx, slope_ny, slope_di, path + ((x, y), (nx, ny))))

	global lowest_depth

	if len(path) < lowest_depth:
		lowest_depth = len(path)
		print(lowest_depth)

	d[state] = max(candidates)
	return d[state]

print(r(*s))
