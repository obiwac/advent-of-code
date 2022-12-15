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

y = 2000000
impossible = 0
x = -maxx
maxx += 1
print(minx, maxx)

while 1:
	for b in beacons:
		x1, y1, x2, y2 = b
		if x2 == x and y2 == y: continue
		d1 = dist(x2, y2, x1, y1)
		d2 = dist(x, y, x1, y1)
		if d2 <= d1: # equals or nah?
			impossible += 1
			break
	x += 1
	if not x % 10000: print(x)
	if x > maxx:
		break

print(impossible)
