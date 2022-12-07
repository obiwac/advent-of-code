import os

f = open(0).read().strip().split('\n')[1:]
s = 'mkdir -p r/r;(cd r/r;'

for l in f:
	if l[0] == '$':
		s += l[1:].replace('cd ', 'mkdir -p ') + ';'
		s += l[1:] + ';'

	b = l.split()

	if b[0].isnumeric():
		s += f'truncate -s{b[0]} {b[1]};'

s += ');find r -type d -exec du -sb {} +|cut -f1'
print(sum(filter(lambda x: x <= 100000, map(int, os.popen(s).read().strip().split('\n')))))
