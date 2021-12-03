f = [(s.split()[0][0], int(s.split()[1])) for s in open("input").readlines()]

# part 1

x = 0
y = 0

for act, n in f:
	if act == 'forward': x += n
	if act == 'backward': x -= n

	if act == 'up': y -= n
	if act == 'down': y += n

from functools import reduce
from operator import mul

print(x, y, x * y)
print(reduce(mul, [sum([(a == s[0]) * n - (a == s[1]) * n for a, n in f]) for s in ['fb', 'du']]))

# part 2

x = 0
y = 0
aim = 0

for act, n in f:
	if act == 'forward':
		x += n
		y += n * aim
	if act == 'backward':
		x -= n
		y -= n * aim

	if act == 'up': aim -= n
	if act == 'down': aim += n

print(x * y)
print(sum([(a == 'f') * n - (a == 'b') * n for a, n in f]))