f = open(0).read().split('\n')

def dist(x1, y1, x2, y2):
	return abs(x1 - x2) + abs(y1 - y2)

beacons = []
minx = 0
maxx = 0

for s in f:
	bits = s.split()

	if not bits:
		continue

	x1, y1 = int(bits[2][2:-1]), int(bits[3][2:-1])
	x2, y2 = int(bits[8][2:-1]), int(bits[9][2:])

	beacons.append((x1, y1, x2, y2))
	minx = min(minx, x1, x2)
	maxx = max(maxx, x1, x2)

MAX = 4000000 # 20

for y in range(MAX + 1):
	intervals = []

	for b in beacons:
		x1, y1, x2, y2 = b
		d = dist(x1, y1, x2, y2)
		i = max(0, 1 + ((d - abs(y1 - y)) * 2))
		if not i: continue
		a, b = x1 - i // 2, x1 + i // 2
		intervals.append((a, b))

	# get union of all our intervals

	b = []

	for begin, end in sorted(intervals):
		if b and b[-1][1] >= begin - 1: b[-1][1] = max(b[-1][1], end)
		else: b.append([begin, end])

	if not y % 10000: print(b, y)

	# go though union and (imperfectly) find any gaps

	for a, b in b:
		if a > 0 and a < MAX: # technically we should also check if there's not a beacon to the right, but that's a lot of work for a quite literal edgecase
			x = a - 1
			print(x, y)
			break # found
	else:continue
	break

print(x * 4000000 + y)
