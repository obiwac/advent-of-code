from itertools import accumulate as accum
from itertools import chain
from functools import reduce

f = [int(x) for x in map(str.strip, open(0).read().split(','))]
f = [f.count(k)for k in range(10)]

def r(r,d,f):
	return r(r,d+1,[*map(lambda i:(f[i],f[i]+f[0],f[0])[1+(7,9).index(i)if i in(7,9)else 0],range(10))][1:]+[0])if d!=257else f

print(sum([r(r,0,f)[x]for x in range(8)]))
