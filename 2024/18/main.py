*f, = map(lambda x: tuple(map(int, x.split(","))), open(0).read().strip().split("\n"))
f = set(f[:1024])

W, H = 71, 71

q = [(0, 0)]
dist = {(0, 0): 0}

while q:
	cx, cy = q.pop(0)

	for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
		nx, ny = cx + dx, cy + dy

		if 0 <= nx < W and 0 <= ny < H and (nx, ny) not in f:
			cost = dist[(cx, cy)] + 1

			if (nx, ny) in dist and cost >= dist[(nx, ny)]:
				continue

			dist[(nx, ny)] = cost
			q.append((nx, ny))

for i in range(H):
	for j in range(W):
		if (j, i) in f:
			print("#", end="")
		else:
			print(".", end="")
	print()

print(dist[(W - 1, H - 1)])
