f = [x for x in map(str.strip, open(0).read().strip().split('\n\n'))]

f[0] = [x == '#' for x in f[0]]
f[1] = [[y == '#' for y in x] for x in map(str.strip, f[1].split('\n'))]

algo = f[0]
fb = f[1]

# expand fb

EX = 70
IW = len(fb[0])

for i in range(len(fb)):
	fb[i] = [False] * EX + fb[i] + [False] * EX

W = len(fb[0])

fb = [[False] * W for _ in range(EX)] + fb + [[False] * W for _ in range(EX)]
H = len(fb)

CLEAN = lambda: [[0 for __ in range(W)] for _ in range(H)]

d = False

def enhance(fb):
	global d
	nf = CLEAN()

	for y in range(W):
		for x in range(H):
			# kernel
			
			num = 0

			for j in range(-1, 2):
				for i in range(-1, 2):
					val = d
					d = not d

					if x + i in range(W) and y + j in range(H):
						val = fb[y + j][x + i]
					
					num = num * 2 + val

			nf[y][x] = algo[num]
	
	return nf

def show(x):
	for l in x:
		for c in l:
			print(" █"[c], end = "")
		
		print()

for _ in range(50):
	print(_ / 50)
	fb = enhance(fb)

count = 0
M = 5

for x in range(M, W - M):
	for y in range(M, H - M):
		count += fb[y][x]

show(fb)
print(count)
print("Done")
