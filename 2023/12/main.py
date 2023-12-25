f = open(0).read().strip().split('\n')

s = 0

for l in f:
	m, n = l.split()
	*n, = map(int, n.split(','))

	# n = n * 5
	# m = "?".join([m] * 5)

	"""
	exp = m.count("?")

	for i in range(2 ** exp):
		o = list(m)
		k = 0

		for j in range(len(m)):
			if m[j] == "?":
				o[j] = "#" if (i >> k) & 1 else "."
				k += 1

		# check it

		p = []

		for k, g in itertools.groupby(o):
			if k == "#": p.append(len(list(g)))

		if p == n:
			s += 1

	print(l)
	"""

	def where_hole(thing, other):
		holes = []
		contiguous = 0

		for i, c in enumerate(m):
			if c in thing:
				contiguous += 1

			if c in other and contiguous:
				holes.append([i - contiguous, i - 1])
				contiguous = 0

		if contiguous:
			holes.append([len(m) - contiguous, len(m) - 1])

		return holes

	holes = where_hole("?#", ".")
	damaged = where_hole("#", "?.")

	print(holes, damaged)

	must_mask = 0

	for a, b in damaged:
		for i in range(a, b + 1):
			must_mask |= 1 << i

	cache = {}

	def r(i, ni, hist = ()):
		state = (i, ni)

		if state in cache:
			return cache[state]

		if ni >= len(n):
			fill_mask = 0

			for a, c in zip(hist, n):
				b = a + c - 1

				for i in range(a, b + 1):
					fill_mask |= 1 << i

			cache[state] = fill_mask & must_mask == must_mask
			return cache[state]

		arr = 0

		for start, end in holes:
			for j in range(start, end - n[ni] + 2):
				if j < i: continue
				arr += r(j + n[ni] + 1, ni + 1, hist + (j,))

		cache[state] = arr
		return arr

	v = r(0, 0)
	print(v)
	s += v

print(s)
