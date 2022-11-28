f = open(0).readlines()[0]

s = 0

for c in f:
	if c == '(':
		s += 1
	
	elif c == ')':
		s -= 1

print(s)
