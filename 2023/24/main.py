from decimal import Decimal, getcontext
getcontext().prec = 50

*f, = map(str, open(0).read().strip().split('\n'))

lines = []

for l in f:
	pos, vel = l.split(" @ ")

	*pos, = map(Decimal, pos.split(", "))
	*vel, = map(Decimal, vel.split(", "))

	lines.append((pos, vel))

m = Decimal("20000000000000000")

def line_intersection(line1, line2):
	xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
	ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

	def det(a, b):
		return a[0] * b[1] - a[1] * b[0]

	div = det(xdiff, ydiff)
	if div == 0:
		return None

	d = (det(*line1), det(*line2))
	x = det(d, xdiff) / div
	y = det(d, ydiff) / div

	if (xdiff[0] > 0 and x > line1[0][0]) or (xdiff[0] < 0 and x < line1[0][0]):
		return None

	if (ydiff[0] > 0 and y > line1[0][1]) or (ydiff[0] < 0 and y < line1[0][1]):
		return None

	if (xdiff[1] > 0 and x > line2[0][0]) or (xdiff[1] < 0 and x < line2[0][0]):
		return None

	if (ydiff[1] > 0 and y > line2[0][1]) or (ydiff[1] < 0 and y < line2[0][1]):
		return None

	return x, y

s = 0

for i in range(len(lines)):
	pa, va = lines[i]
	pax1, pay1 = pa[0], pa[1]
	pax2, pay2 = pa[0] + m * va[0], pa[1] + m * va[1]
	line1 = ((pax1, pay1), (pax2, pay2))

	for j in range(i + 1, len(lines)):
		pb, vb = lines[j]
		pbx1, pby1 = pb[0], pb[1]
		pbx2, pby2 = pb[0] + m * vb[0], pb[1] + m * vb[1]
		line2 = ((pbx1, pby1), (pbx2, pby2))

		r = line_intersection(line1, line2)

		if r is None:
			continue

		x, y = r

		mi, ma = 200000000000000, 400000000000000
		# mi, ma = 7, 27

		if x >= mi and y >= mi and x <= ma and y <= ma:
			print(pa, pb)
			s += 1

print(s)