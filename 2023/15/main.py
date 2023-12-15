from typing import OrderedDict

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

boxes = [OrderedDict() for _ in range(256)]

for o in ops:
	if "-" in o:
		h = hash(o[:-1])
		try: del boxes[h][o[:-1]]
		except: pass
	
	elif "=" in o:
		k, v = o.split("=")
		h = hash(k)
		boxes[h][k] = v

s = 0

for i, b in enumerate(boxes):
	for j, k in enumerate(b):
		s += (i + 1) * (j + 1) * int(b[k])

print(s)
