# f = open(0).readlines()
# 
# s = 0
# 
# for l in f:
# 	l = l.strip()
# 
# 	if len([*filter(lambda v: v in 'aeiou', l)]) < 3:
# 		continue
# 
# 	for i in range(len(l) - 1):
# 		if l[i] == l[i + 1]:
# 			break
# 	
# 	else:
# 		continue
# 
# 	if 'ab' in l or 'cd' in l or 'pq' in l or 'xy' in l:
# 		continue
# 
# 	s += 1
# 
# print(s)

import itertools
f = open(0).readlines()

s = 0

for l in f:
	l = l.strip()

	alphabet = "abcdefghijklmnopqrstuvwxyz"

	for c in itertools.product(alphabet, alphabet):
		if l.count(c[0] + c[1]) >= 2:
			break
	
	else:
		continue

	for i in range(len(l) - 2):
		if l[i] == l[i + 2]:
			break
	
	else:
		continue

	s += 1

print(s)
