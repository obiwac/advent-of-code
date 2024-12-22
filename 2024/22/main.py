f = open(0).read().strip().split("\n")
s = 0

for l in f:
	x = int(l)

	for i in range(2000):
		x = (x ^ (x << 6)) % 16777216
		x = (x ^ (x >> 5)) % 16777216
		x = (x ^ (x << 11)) % 16777216

	s += x

print(s)
