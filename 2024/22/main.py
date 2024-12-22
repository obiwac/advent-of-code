f = open(0).read().strip().split("\n")
s = 0
totals = {}

for l in f:
	x = int(l)
	changes = []
	visited = set()

	for _ in range(2000):
		prev = x % 10
		x = (x ^ (x << 6)) & 0xFFFFFF
		x = (x ^ (x >> 5)) & 0xFFFFFF
		x = (x ^ (x << 11)) & 0xFFFFFF

		price = x % 10
		changes.append(price - prev)

		if len(changes) < 4:
			continue

		k = tuple(changes[-4:])

		if k in visited:
			continue

		visited.add(k)

		if k not in totals:
			totals[k] = price

		else:
			totals[k] += price

	s += x

print(s)
print(max(totals.values()))
