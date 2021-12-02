f = [(s.split()[0][0], int(s.split()[1])) for s in open("input").readlines()]

# part 1

x = 0
y = 0

for act, n in f:
	if act == 'forward': x += n
	if act == 'backward': x -= n

	if act == 'up': y -= n
	if act == 'down': y += n

# from functools import reduce
# from operator import mul

print(x, y, x * y)
# print(reduce(mul, [sum([(a == s[0]) * n - (a == s[1]) * n for a, n in f]) for s in ['fb', 'du']]))

# part 2

x = 0
y = 0
aim = 0

for act, n in f:
	if act == 'f':
		x += n
		y += n * aim
	if act == 'u': aim -= n
	if act == 'd': aim += n

print(x, y, x * y)

from itertools import accumulate

r=(lambda f:(lambda x:sum([(a=='f')*n*x[i]for i,(a,n)in enumerate(f)]))(list(accumulate([n*((a=='d')-(a=='u'))for a,n in f])))*sum([n*(a=='f')for a,n in f]))([(x[0],int(y))for x,y in map(str.split,open("input").readlines())])
print(r)




#[expr1, expr2][-1]

#=(lambda x, y: [y, 1 if x() == 1 else x()][0])(lambda y: , [])
print(r)


r=(lambda n: (lambda f, *a: f(f, *a))(lambda rec, n: 1 if n == 0 else n*rec(rec, n-1), n))(10)
print(r)
