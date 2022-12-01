f = open(0).read().split('\n\n')

m = []

for elf in f:
	a = 0

	for d in elf.split('\n'):
		if d:
			a += int(d)

	m.append(a)

print(max(m))
print(sum(sorted(m)[-3:]))
