# f = open(0).readlines()
# s = 0
# 
# for box in f:
# 	l, w, h = map(int, box.strip().split('x'))
# 	sides = [l * w, w * h, h * l]
# 	s += 2 * sum(sides) + min(sides)
# 
# print(s)

f = open(0).readlines()
s = 0

for box in f:
	l, w, h = map(int, box.strip().split('x'))
	sides = [2 * (l + w), 2 * (w + h), 2 * (h + l)]
	s += min(sides) + l * w * h

print(s)
