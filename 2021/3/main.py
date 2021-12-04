from numpy import array
from functools import reduce
# part 1

r=(lambda d:(lambda g:g*(~g&((1<<12)-1)))(reduce(lambda a,b:2*a+b,d.sum(0)>d.shape[0]/2)))(array([[*map(int,x)]for x in open("input").read().split('\n')]))
print(r)

# 2

f = [x.strip() for x in open("input").readlines()]

gamma = ""
epislon = ""

a = list(f)
b = list(f)

for i in range(len(f[0])):
	zeros = 0
	ones = 0

	for x in a:
		zeros += x[i] == '0'
		ones += x[i] == '1'

	gamma += '1' if ones >= zeros else '0'
	epislon += '1' if ones < zeros else '0'

	if len(a) == 1:
		break

	for x in list(a):
		if x[i] != gamma[i]:
			a.remove(x)

epislon = ""

for i in range(len(f[0])):
	zeros = 0
	ones = 0

	for x in b:
		zeros += x[i] == '0'
		ones += x[i] == '1'

	epislon += '0' if zeros <= ones else '1' # get least common

	if len(b) == 1:
		break

	for x in list(b):
		if x[i] != epislon[i]:
			b.remove(x)

print(int(a[0], 2) * int(b[0], 2))
