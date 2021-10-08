from math import pi, cos, sin

i=open("input").read()

# part 1

x,y,d=0,0,0
for n,m in((x[0],int(x[1:]))for x in i.split('\n')):
	o="ENWSFRL"
	a=d if n=='F' else o.index(n)*pi/2
	if n in o[5:]:
		d+=m*((n=='L')*2-1)*pi/180
		m=0
	x+=m*cos(a)
	y+=m*sin(a)

print(f"part 1: {abs(x)+abs(y)}")

# part 1 golfed

from operator import mul

def test(n,d):
	#print("test", n, sum(d))
	return sum(d)

#r=(lambda:(d:=0,sum(map(lambda z:abs(sum(z)),zip(map(lambda t:map(lambda c:(d:=d+t[1]*((t[0]=='L')*2-1)*pi/180)*0 if t[0]in"LR"else c*t[1],map(lambda a:(cos(a),sin(a)),[d if'F'==t[0]else"ENWS".index(t[0])*pi/2])),((x[0],int(x[1:]))for x in i.split('\n')))))))[-1])()
r=((  #sum(map(lambda z:abs(sum(z)),
	list((lambda ____:(d:=[],
	zip(*map(lambda t:
		(((0,d.append(t[1]*((t[0]=='L')*2-1)*pi/180),test(1,d))[0]if t[0]in"LR"else c*t[1])
		for c in(lambda a:(cos(a),sin(a)))(test(2,d)if'F'==t[0]else"ENWSRL".index(t[0])*pi/2)),
	((x[0],int(x[1:]))for x in i.split('\n'))))))([])[1])

	))

"""
The problem I'm facing here is that Python's peephole optimizer is executing all the sum(d) calls before d.append has a chance to be called
"""

#print(f"part 1: {r}")

# part 2

from cmath import rect, polar

x, y = 0, 0
wx, wy = 10, 1 # these are relative positions to the ship (x, y)

for n,m in((x[0],int(x[1:]))for x in i.split('\n')):
	if n in 'LR':
		modulus, argument = polar(complex(wx, wy))
		z = rect(modulus, argument + m * ((n == 'L') * 2 - 1) * pi / 180)
		
		wx = z.real
		wy = z.imag

	elif n in 'ENWS':
		a = o.index(n) * pi / 2

		wx += m * cos(a)
		wy += m * sin(a)
	
	else:
		x += wx * m
		y += wy * m

print(f"part 2: {round(abs(x) + abs(y))}")