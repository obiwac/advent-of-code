# f = open(0).readlines()[0]
# visited = set()
# 
# curr = [0, 0]
# 
# for d in f:
# 	visited.add(tuple(curr))
# 
# 	if d == '>': curr[0] += 1
# 	if d == '<': curr[0] -= 1
# 	if d == '^': curr[1] += 1
# 	if d == 'v': curr[1] -= 1
# 
# print(len(visited))

f = open(0).readlines()[0]
visited = set({(0, 0)})

santa = [0, 0]
robo = [0, 0]

for i, d in enumerate(f):
	l = santa if i & 1 else robo

	if d == '>': l[0] += 1
	if d == '<': l[0] -= 1
	if d == '^': l[1] += 1
	if d == 'v': l[1] -= 1

	visited.add(tuple(l))

print(len(visited))
