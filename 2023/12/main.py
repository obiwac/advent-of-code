import itertools

f = open(0).read().strip().split('\n')

s = 0

for l in f:
	m, n = l.split()
	*n, = map(int, n.split(','))

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
	# (hole_size, start, end, damaged_before, damaged_after)

	holes = []
	contiguous = 0
	damaged_count = 0

	for i, c in enumerate(m):
		if c == "?":
			contiguous += 1

		if c in "#." and contiguous:
			holes.append([contiguous, i - contiguous, i, damaged_count, 0])
			if len(holes) >= 2: holes[-2][2] = damaged_count

			contiguous = 0
			damaged_count = 0

		if c == "#":
			damaged_count += 1

		if c == ".": damaged_count = 0

	if contiguous:
		holes.append([contiguous, len(m) - contiguous, len(m) - 1, damaged_count, 0])
		if len(holes) >= 2: holes[-2][2] = damaged_count

	def r(n_left, holes_left):
		# base case: nothing left!

		if not n_left or not holes_left:
			return

		# place first group, and then recurse into the rest

		hole_size, start, end, damaged_before, damaged_after = holes_left[0]
		full_size = hole_size + damaged_before + damaged_after
		to_place = n[0]

		if to_place >= full_size: # can't place anything
			return

		if to_place == full_size: # only one arrangement possible, move on
			return r(n[1:], holes_left[1:])

		if to_place >= damaged_before and to_place <= hole_size - 1 + damaged_before: # can place at the beginning
			...

		if to_place <= hole_size - 1 + damaged_after: # can place at the end

	r(n, holes)
	"""

print(s)
