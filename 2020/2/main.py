passwords = open("input").readlines()
valid1 = 0
valid2 = 0

for password in passwords:
	parts = password.split(' ')
	policy = parts[0].split('-')

	policymin = int(policy[0])
	policymax = int(policy[1])

	parts[1] = parts[1][0]

	# part 1

	n = 0
	for c in parts[2]:
		if c == parts[1]:
			n += 1
	
	if n >= policymin and n <= policymax:
		valid1 += 1
	
	# part 2

	if (parts[2][policymin - 1] == parts[1]) ^ (parts[2][policymax - 1] == parts[1]):
		valid2 += 1

print(valid1)
print(valid2)