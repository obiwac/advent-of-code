f = open(0).read().strip()

s = ""
files = []
free_spaces = []
abs_i = 0

for i in range(len(f)):
	x = int(f[i])

	if i % 2 == 0:
		id = i // 2
		files.append([id, x, abs_i])
		abs_i += x

	else:
		free_spaces.append([x, abs_i])
		abs_i += x

leftmost_free_space = 0
blocks = []

for file in files[::-1]:
	for i in range(leftmost_free_space, len(free_spaces)):
		if file[1] == 0 or free_spaces[i][1] > file[2]:
			break

		if file[1] > free_spaces[i][0]:
			continue

		d = min(file[1], free_spaces[i][0])
		file[1] -= d
		free_spaces[i][0] -= d
		blocks.append((free_spaces[i][1], d, file[0]))
		free_spaces[i][1] += d

		if free_spaces[i][0] == 0:
			leftmost_free_space += 0

	if file[1] > 0:
		blocks.append([file[2], file[1], file[0]])

s = 0

for start, size, id in blocks:
	end = start + size
	s += id * (end * (end - 1) // 2 - start * (start - 1) // 2)

print(s)
