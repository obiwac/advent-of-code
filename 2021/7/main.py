from itertools import accumulate as accum
from itertools import chain
from functools import reduce

f = [int(x) for x in map(str.strip, open(0).read().split(','))]

# golfed x_X

print(min(sum(abs(i-j)*(abs(i-j)+1)/2for j in f)for i in range(max(f))))

# original solution

a = min(f)
b = max(f)

costs = []

for i in range(a, b + 1):
	cost = 0

	for j in f:
		n = abs(j - i)
		cost += n * (n + 1) / 2

	costs.append(cost)

print(min(costs))
