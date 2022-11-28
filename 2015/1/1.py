f = open(0).readlines()[0]

s = 0

for i, c in enumerate(f):
	if c == '(':
		s += 1
	
	elif c == ')':
		s -= 1

	if s < 0:
		print(i + 1)
		break
