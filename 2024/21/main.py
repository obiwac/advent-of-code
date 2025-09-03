from functools import cache

codes = open("input").read().strip().split("\n")

num_keypad = ["789", "456", "123", "#0A"]
dir_keypad = ["#^A", "<v>"]

def find(keypad, c):
	ci, cj = -1, -1

	for i in range(len(keypad)):
		if c in keypad[i]:
			ci, cj = i, keypad[i].index(c)
			break

	assert ci != -1 and cj != -1
	return ci, cj

def get_seq(keypad, code):
	ci, cj = find(keypad, "A")
	seqs = [""]

	for k, c in enumerate(code):
		target_i, target_j = find(keypad, c)

		@cache
		def dfs(i, j, target_i, target_j, seq):
			if i == target_i and j == target_j:
				return [seq + "A"]

			seqs = []

			if j > target_j:
				seqs.extend(dfs(i, j - 1, target_i, target_j, seq + "<"))
			elif j < target_j:
				seqs.extend(dfs(i, j + 1, target_i, target_j, seq + ">"))

			if i < target_i:
				seqs.extend(dfs(i + 1, j, target_i, target_j, seq + "v"))
			elif i > target_i:
				seqs.extend(dfs(i - 1, j, target_i, target_j, seq + "^"))

			return seqs

		nseq = []
		for seq in seqs:
			if k > 0:
				i, j = find(keypad, code[k - 1])
			else:
				i, j = ci, cj
			nseq.extend(dfs(i, j, target_i, target_j, seq))
		seqs = nseq

	return seqs

s = 0

for code in codes:
	robot1 = get_seq(num_keypad, code)
	robot2 = []
	for r in robot1:
		robot2.extend(get_seq(dir_keypad, r))
	rm2 = min(robot2, key=lambda x: len(x))
	robot2 = list(filter(lambda x: len(x) == len(rm2), robot2))
	print(len(robot2))
	me = []
	for r in robot2:
		print(r)
		me.extend(get_seq(dir_keypad, r))
	rm = min(me, key=lambda x: len(x))

	print(rm, len(rm), int(code[:-1]))
	s += len(rm) * int(code[:-1])

print(s)
