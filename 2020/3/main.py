lines = open("input").readlines()

# part 1: completed in just under a minute

trees = 0
x = 0

for line in lines:
	if line[x % 31] == '#':
		trees += 1
	
	x += 3

print(f"part 1: {trees}")

# part 2: completed in about 2 min 30 sec

def test_slope(dx, dy):
	trees = 0
	
	x = 0
	y = 0

	while y < len(lines):
		if lines[y][x % 31] == '#':
			trees += 1

		x += dx
		y += dy
	
	return trees

print(f"part 2: {test_slope(1, 1) * test_slope(3, 1) * test_slope(5, 1) * test_slope(7, 1) * test_slope(1, 2)}")
