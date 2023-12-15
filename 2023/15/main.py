*f, = map(str, open(0).read().strip().split('\n'))

def hash(s):
	h = 0

	for c in s:
		h += ord(c)
		h *= 17
		h %= 256

	return h

ops = f[0].split(",")
print(sum(map(hash, ops)))
