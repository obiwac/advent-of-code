W=98
H=93

i = open("input").read()
f = list(map(lambda r:list(map(".L#".index,r)),i.split('\n')))

# part 1

from copy import deepcopy
from math import *

p=f
c=[]
while 0:
	c=deepcopy(p)
	b=deepcopy(p)
	
	p.append([0]*(W+1))
	p[0].append(0)
	for y in range(H):
		p[y+1].append(0)
		for x in range(W):
			a=[p[y+i//3-1][x+i%3-1]for i in range(9)]
			if 1==p[y][x]and a.count(2)<1:c[y][x]=2
			elif 2==p[y][x]and a.count(2)>4:c[y][x]=1
	
	if b==c:break
	p=c

print(f"part 1: {str(c).count('2')}")

# part 2 

p=list(map(lambda r:list(map(".L#".index,r)),i.split('\n')))
c=[]
while 1:
	c=deepcopy(p)
	
	for y in range(H):
		for x in range(W):
			a=0

			for t in [z*tau/8 for z in range(8)]:
				i,j=x,y
				while 1:
					j+=round(sin(t))
					i+=round(cos(t))

					if not(j in range(H)and i in range(W)):break

					b=p[j][i]
					if m>1:print(j, i, t, round(sin(t)), round(cos(t)))
					if b:
						a+=b==2
						break
			
			if 1==p[y][x]and a<1:c[y][x]=2
			elif 2==p[y][x]and a>4:c[y][x]=1
	
	if p==c:break
	p=c

print(f"part 2: {str(c).count('2')}")