import sys
sys.setrecursionlimit(10000)

*f, = map(list, open(0).read().strip().split('\n'))
w, h = len(f[0]), len(f)

slopes = "v>^<"
dirs =[(0, 1), (1, 0), (0, -1), (-1, 0)] 
s = (1, 0)

d = {}
paths = []

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
			if f[ny][nx] == '.':
				candidates.append(r(nx, ny, i, path + ((x, y),)))

			if f[ny][nx] in slopes:
				# can't go up a slope

				if slopes.index(f[ny][nx]) == (i + 2) % 4:
					continue

				# otherwise, go hella down

				slope_di = slopes.index(f[ny][nx])
				slope_dx, slope_dy = dirs[slope_di]
				slope_nx = nx + slope_dx
				slope_ny = ny + slope_dy
				candidates.append(r(slope_nx, slope_ny, slope_di, path + ((x, y), (nx, ny))))

	d[state] = max(candidates)
	return d[state]

print(r(*s))
