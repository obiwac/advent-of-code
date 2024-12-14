W = 101
H = 103
ITER = 100

f = open(0).read().strip().split("\n")
q = [0, 0, 0, 0]

for l in f:
	p, v = l.split()
	px, py = p.split(",")
	vx, vy = v.split(",")
	px = int(px[2:])
	vx = int(vx[2:])
	py = int(py)
	vy = int(vy)

	x = (px + vx * ITER) % W
	y = (py + vy * ITER) % H

	if x < W // 2 and y < H // 2:
		q[0] += 1

	elif x > W // 2 and y < H // 2:
		q[1] += 1
	
	elif x < W // 2 and y > H // 2:
		q[2] += 1
	
	elif x > W // 2 and y > H // 2:
		q[3] += 1

print(q)
print(q[0] * q[1] * q[2] * q[3])
