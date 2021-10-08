from math import log2, floor, prod

i = open("input").read().split("\n\n")

ranges = [[[int(z) for z in y.split('-')] for y in x.replace("or ","").split(': ')[1].split(' ')] for x in i[0].split('\n')]
print(ranges)

error_rate = 0
tickets = [[int(y) for y in x.split(',')] for x in i[2].split('\n')[1:]]
valid_tickets = []

def check_range(field, r):
	return field in range(r[0][0], r[0][1] + 1) or field in range(r[1][0], r[1][1] + 1)

for j, fields in enumerate(tickets):
	old_error_rate = error_rate

	for field in fields:
		error_rate += field
		
		for r in ranges:
			if check_range(field, r):
				error_rate -= field
				break

	if error_rate == old_error_rate:
		valid_tickets.append(fields)

print(f"part 1: {error_rate}")

candidates_per_range = {}

for k, r in enumerate(ranges):
	curr_mask = (1 << len(ranges)) - 1

	for fields in valid_tickets:
		mask = 0
		print(fields[0])

		for j, field in enumerate(fields):
			mask |= check_range(field, r) << j
		
		curr_mask &= mask
	
	candidates_per_range[k] = [bin(curr_mask).count('1'), curr_mask] # floor(log2(curr_mask))

	print(f"candidate: r = {k}, b = {bin(curr_mask).count('1')}, m = {curr_mask}")
	if k == 17: exit()

verdict = {}

sorted_keys = [y for x, y in sorted(zip(candidates_per_range.values(), candidates_per_range.keys()))]

for k in sorted_keys:
	#print("candidate", k, candidates_per_range[k][1])

	mask = candidates_per_range[k][1]

	try: verdict[k] = floor(log2(mask))
	except ValueError: pass
	
	for j in candidates_per_range.keys():
		candidates_per_range[j][1] ^= mask

print(verdict)

my_tickets = [int(y) for y in i[1].split('\n')[1].split(',')]
print(prod((my_tickets[verdict[x]] for x in range(6))))