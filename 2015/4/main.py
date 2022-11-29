# f = open(0).readlines()[0].strip()
# 
# import hashlib
# 
# for i in range(1000000000):
# 	digest = hashlib.md5(f"{f}{i}".encode()).hexdigest()
# 
# 	if digest[:5] == '00000':
# 		break
# 
# print(i)

f = open(0).readlines()[0].strip()

import hashlib

for i in range(1000000000):
	digest = hashlib.md5(f"{f}{i}".encode()).hexdigest()

	if digest[:5] == '00000':
		break

print(i)
