# f = open(0).readlines()
# 
# s = [[False] * 1000 for _ in range(1000)]
# 
# for l in f:
# 	l = l.strip().split(' ')
# 
# 	if l[0] == 'turn':
# 		*coord1, = map(int, l[2].split(','))
# 		*coord2, = map(int, l[4].split(','))
# 
# 		rx = range(coord1[0], coord2[0] + 1)
# 		ry = range(coord1[1], coord2[1] + 1)
# 
# 		for y in ry:
# 			for x in rx:
# 				s[y][x] = l[1] == 'on'
# 	
# 	if l[0] == 'toggle':
# 		*coord1, = map(int, l[1].split(','))
# 		*coord2, = map(int, l[3].split(','))
# 
# 		rx = range(coord1[0], coord2[0] + 1)
# 		ry = range(coord1[1], coord2[1] + 1)
# 
# 		for y in ry:
# 			for x in rx:
# 				s[y][x] = not s[y][x]
# 
# print(sum(l.count(True) for l in s))

f = open(0).readlines()

s = [[0] * 1000 for _ in range(1000)]

for l in f:
	l = l.strip().split(' ')

	if l[0] == 'turn':
		*coord1, = map(int, l[2].split(','))
		*coord2, = map(int, l[4].split(','))

		rx = range(coord1[0], coord2[0] + 1)
		ry = range(coord1[1], coord2[1] + 1)

		for y in ry:
			for x in rx:
				if l[1] == 'on': s[y][x] += 1
				if l[1] == 'off': s[y][x] = max(s[y][x] - 1, 0)
	
	if l[0] == 'toggle':
		*coord1, = map(int, l[1].split(','))
		*coord2, = map(int, l[3].split(','))

		rx = range(coord1[0], coord2[0] + 1)
		ry = range(coord1[1], coord2[1] + 1)

		for y in ry:
			for x in rx:
				s[y][x] += 2

print(sum(sum(l) for l in s))
