from collections import Counter
from itertools import chain

f = [[[int(z.strip()) for z in y.split(',')] for y in x.split('->')] for x in map(str.strip, open(0).readlines())]

print(sum([x>1for x in Counter(chain(*[(lambda x,y,z,w:(lambda r,*a:r(r,*a))(lambda r,c,x,y,z,w,a,b:r(r,c+[(x,y)],x+a,y+b,z,w,a,b)if x!=z or y!=w else[(x,y)]+c,[],x,y,z,w,(z>x)-(z<x),(w>y)-(w<y)))(*chain(*l))for l in f])).values()]))