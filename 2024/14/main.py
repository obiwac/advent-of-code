W = 101
H = 103
ITER = 100

f = open("input").read().strip().split("\n")
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

map = [[0 for i in range(W)] for j in range(H)]
c = []

for i, (px, py, _, _) in enumerate(r):
	c.append([px, py])

for k in range(1, 1000000):
	seen = set()

	for i, (px, py, vx, vy) in enumerate(r):
		c[i][0] = (c[i][0] + vx) % W
		c[i][1] = (c[i][1] + vy) % H

		seen.add((c[i][0], c[i][1]))

	if len(seen) == len(f):
		print("Found in ", k)
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

exit()

for k in range(1000000):
	#map = [[0 for i in range(W)] for j in range(H)]

	for px, py, vx, vy in r:
		x = (px + vx * ITER) % W
		y = (py + vy * ITER) % H

		cx = px
		cy = py

		seen = set()

		for _ in range(k):
			#if map[cy][cx] > 0:
			#	map[cy][cx] -= 1

			cx = (cx + vx) % W
			cy = (cx + vy) % H

			seen.add((cx, cy))

			#map[cy][cx] += 1

		if len(seen) == len(f):
			print("Found in ", k)
			break

		if x < W // 2 and y < H // 2:
			q[0] += 1

		elif x > W // 2 and y < H // 2:
			q[1] += 1
		
		elif x < W // 2 and y > H // 2:
			q[2] += 1
		
		elif x > W // 2 and y > H // 2:
			q[3] += 1

		# if map in maps:
		# 	print("Loop in ", k)
		# 	break

		# maps.append(map)

		# for i in range(H):
		# 	for j in range(W):
		# 		if map[i][j] == 0:
		# 			print(" ", end="")
		# 		else:
		# 			print(map[i][j], end="")
		# 	print()

print(q)
print(q[0] * q[1] * q[2] * q[3])
