from functools import reduce
from itertools import chain
from operator import mul, or_

f = [[*map(int, x)] for x in map(str.strip, open(0).read().strip().split('\n'))]

o = (lambda q:reduce(mul,sorted(chain(*[[len((lambda r,*a:r(r,*a))(lambda r,f,x,y:{(x,y)}|reduce(or_,[({(x,y)}|r(r,f,z,w)if z in range(len(f))and w in range(len(f[x]))and f[x][y]<f[z][w]<9else set())for z,w in q(x,y)]),f,x,y))for y in range(len(f[x]))if any(f[x][y]<f[z][w]for z,w in q(x,y)if z in range(len(f))and w in range(len(f[x])))]for x in range(len(f))]))[-3:]))(lambda x,y:((x+1,y),(x-1,y),(x,y+1),(x,y-1)))

print(o)
