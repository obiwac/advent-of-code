W = 101
H = 103
ITER = 100

f = open(0).read().strip().split("\n")
q = [0, 0, 0, 0]
r = []

for l in f:
	p, v = l.split()
	px, py = p.split(",")
	vx, vy = v.split(",")
	px = int(px[2:])
	vx = int(vx[2:])
	py = int(py)
	vy = int(vy)
	r.append((px, py, vx, vy))

# Part 1.

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

print(q[0] * q[1] * q[2] * q[3])

# Part 2.

c = []
k = 0

for i, (px, py, _, _) in enumerate(r):
	c.append([px, py])

for k in range(1, 1000000):
	seen = set()

	for i, (px, py, vx, vy) in enumerate(r):
		c[i][0] = (c[i][0] + vx) % W
		c[i][1] = (c[i][1] + vy) % H

		seen.add((c[i][0], c[i][1]))

	if len(seen) == len(f):
		break

for i in range(H):
	for j in range(W):
		for x, y in c:
			if x == j and y == i:
				print("#", end="")
				break

		else:
			print(".", end="")

	print()

print(k)
