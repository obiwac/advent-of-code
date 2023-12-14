*f, = map(list, open(0).read().strip().split('\n'))

def tilt(f):
	for y, l in enumerate(f):
		for x, c in enumerate(l):
			if c != 'O':
				continue

			f[y][x] = "."

			v = False
			for yy in range(y - 1, -1, -1):
				if f[yy][x] in "#O":
					f[yy + 1][x] = "O"
					v = True
					break
			if not v: f[0][x] = "O"

	return f

def cycle(f):
	# north

	f = tilt(f)

	# west

	*f, = map(list, zip(*f))
	f = tilt(f)
	*f, = map(list, zip(*f))

	# south

	f = f[::-1]
	f = tilt(f)
	f = f[::-1]

	# east

	f = list(map(list, zip(*f)))[::-1]
	f = tilt(f)
	f = list(map(list, zip(*f[::-1])))

	return f

hashes = []
scores = []

I = 1000000000
start = 0

for i in range(I):
	f = cycle(f)
	h = hash("".join(map("".join, f)))

	if h in hashes:
		start = hashes.index(h)
		break

	s = 0

	for y, l in enumerate(f):
		score = len(f) - y
		# print("".join(l))
		s += "".join(l).count("O") * score

	hashes.append(h)
	scores.append(s)

print(scores[start + (I - 1 - start) % (len(scores) - start)])
