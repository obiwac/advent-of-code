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
	while True:
		if file[1] == 0 or leftmost_free_space >= len(free_spaces) or free_spaces[leftmost_free_space][1] > file[2]:
			break

		if file[1] < free_spaces[leftmost_free_space][0]:
			break

		d = min(file[1], free_spaces[leftmost_free_space][0])
		file[1] -= d
		free_spaces[leftmost_free_space][0] -= d
		blocks.append((free_spaces[leftmost_free_space][1], d, file[0]))
		free_spaces[leftmost_free_space][1] += d

		if free_spaces[leftmost_free_space][0] == 0:
			leftmost_free_space += 1

	if file[1] > 0:
		blocks.append([file[2], file[1], file[0]])

# compacted = [0] * 100
# 
# for b in blocks:
# 	compacted[b[0]:b[0] + b[1]] = [b[2]] * b[1]
# 
# print("".join(map(str, compacted)))

s = 0

for start, size, id in blocks:
	end = start + size
	s += id * (end * (end - 1) // 2 - start * (start - 1) // 2)

print(s)
