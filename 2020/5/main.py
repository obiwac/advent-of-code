boarding_passes = open("input").readlines()

# part 1

def get_y(string):
	y = 0

	for i in range(len(string)):
		bit = string[i] == 'B'
		y |= bit << (7 - i - 1)
	
	return y

def get_x(string):
	x = 0

	for i in range(len(string)):
		bit = string[i] == 'R'
		x |= bit << (3 - i - 1)
	
	return x

def get_xy(string):
	return (get_x(string[7: 10]), get_y(string[0: 7]))

def get_sid(string):
	x, y = get_xy(string)
	return y * 8 + x

boarding_pass_sids = []

for boarding_pass in boarding_passes:
	boarding_pass_sids.append(get_sid(boarding_pass))

lowest_sid = min(boarding_pass_sids)
highest_sid = max(boarding_pass_sids)

print(f"part 1: {highest_sid}")

# part 2

my_sid = None

line = 0
for sid in range(lowest_sid, highest_sid + 1):
	if not sid in boarding_pass_sids:
		if sid - 1 in boarding_pass_sids and sid + 1 in boarding_pass_sids:
			line += 1
			my_sid = sid
			break

print(f"part 2: {my_sid} {line} {sum(boarding_pass_sids)}")

# part 1 (better)

def get_sid(string):
	binary = string.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1')
	return int(binary, 2)

boarding_pass_sids = [get_sid(boarding_pass) for boarding_pass in boarding_passes]
print(f"part 1: {max(boarding_pass_sids)} {sum(range(lowest_sid, highest_sid + 1))}")

print(boarding_pass_sids)