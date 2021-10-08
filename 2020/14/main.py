import numpy as np
import pandas as pd
import itertools

data = np.loadtxt('input',dtype=str,delimiter=' = ')

memory = {}

for i in data:
	if i[0] == 'mask':
		mask = np.array(list(i[1]))
	else:
		binnum = np.array(list(bin(int(i[1]))[2:].zfill(36)))
		new_num = np.array([i for i in mask])
		new_num[np.where(new_num == 'X')] = binnum[np.where(new_num == 'X')]
		memory[i[0][4:-1]] = int(''.join(list(new_num)),2)

#print(sum(memory.values()))

memory = {}

k = 0

for i in data:
	#if k > 15: exit()

	if i[0] == 'mask':
		mask = np.array(list(i[1]))
		num_X = np.count_nonzero(mask == 'X')
		perms = ["".join(seq) for seq in itertools.product("01", repeat=num_X)]
	else:
		binnum = np.array(list(bin(int(i[0][4:-1]))[2:].zfill(36)))
		binnum[np.where(mask == '1')] = '1'
		binnum[np.where(mask == 'X')] = 'X'
		for j in perms:
			new_num = np.array([i for i in binnum])
			new_num[np.where(new_num == 'X')] = np.array(list(j))

			# if int(''.join(list(new_num)), 2) in memory:
			# 	print(f"writing {int(i[1])} at address {sum(memory.values())} ...")
			# 	k += 1
			# 	if k > 2315: exit()
			memory[int(''.join(list(new_num)), 2)] = int(i[1])
			#print(''.join(list(new_num)))
			#print(int(''.join(list(new_num)), 2))
			print(f"writing {int(i[1])} at address {len(memory.keys())} ...")
		#print(int(i[1]))

#print(sum(memory.values()))