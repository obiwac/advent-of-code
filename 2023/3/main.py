import re

*f, = map(str.strip, open(0).readlines())
s = 0

gears = {}

for y, l in enumerate(f):
	o = str(l)
	x = 0

	while 1:
		m = re.search(r'\d+', o)

		if m == None:
			break

		span = m.span()
		num = int(o[span[0]: span[1]])

		o = o[span[1]:]
		
		# check surrounding symbols

		start = span[0] + x
		end = span[1] + x

		# bottom edge
		
		def try_index(i, j):
			if i < 0 or j < 0 or i >= len(f) or j >= len(f[i]):
				return '.'

			c = f[j][i]
			return c

		is_comp = False

		for i in range(start - 1, end + 1):
			if try_index(i, y + 1) != '.':
				is_comp = True

		for i in range(start - 1, end + 1):
			if try_index(i, y - 1) != '.':
				is_comp = True

		if try_index(start - 1, y) != '.':
			is_comp = True

		if try_index(end, y) != '.':
			is_comp = True

		if is_comp:
			s += num

		x += span[1]

print(s)
