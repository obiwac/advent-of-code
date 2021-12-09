from functools import reduce
from itertools import chain
from operator import mul, or_

i = open(0).read()

o = (lambda p,q,f:reduce(mul,sorted(chain(*[[len((lambda r,*a:r(r,*a))(lambda r,f,x,y:{(x,y)}|reduce(or_,[({(x,y)}|r(r,f,z,w)if z in q(f)and w in q(f[x])and f[x][y]<f[z][w]<9else set())for z,w in p(x,y)]),f,x,y))for y in q(f[x])if any(f[x][y]<f[z][w]for z,w in p(x,y)if z in q(f)and w in q(f[x]))]for x in q(f)]))[-3:]))(lambda x,y:((x+1,y),(x-1,y),(x,y+1),(x,y-1)),lambda x:range(len(x)),[[*map(int,x)]for x in i.split('\n')])

print(o)
