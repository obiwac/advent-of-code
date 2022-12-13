from functools import cmp_to_key

f = open(0).read().strip().split('\n\n')

RIGHT = -1
WRONG = 1

def comp(left, right):
	if type(left) == type(right) == int:
		if left < right: return RIGHT
		if left > right: return WRONG
		return 0

	if type(left) == int: left = [left]
	if type(right) == int: right = [right]

	left = list(left)
	right = list(right)

	while 1:
		if not left and not right:
			break

		if not left: return RIGHT # left side ran out; right order
		if not right: return WRONG # right side ran out; wrong order

		a = left.pop(0)
		b = right.pop(0)

		r = comp(a, b)
		if r: return r
	
	return 0

s = 0

for i, g in enumerate(f):
	first, second = map(eval, g.split('\n'))
	if comp(first, second) == RIGHT:
		s += i + 1

print(s)

# part 2

f.append("[[2]]\n[[6]]")
f = sorted(map(eval, "\n".join(f).split('\n')), key = cmp_to_key(comp))

prod = 1

for i, g in enumerate(f):
	prod *= (repr(g) in ("[[2]]", "[[6]]")) * i + 1

print(prod)
