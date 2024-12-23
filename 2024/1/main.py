f = open(0).readlines()

# Part 1.

x = []
y = []

for l in f:
	a, b = map(int, l.split())
	x.append(a)
	y.append(b)

x.sort()
y.sort()

s = sum(abs(x[i] - y[i]) for i in range(len(x)))
print(s)

# Part 2.

from collections import Counter

y = Counter(y)
s = 0

for z in x:
	if z in y:
		s += y[z] * z

print(s)
