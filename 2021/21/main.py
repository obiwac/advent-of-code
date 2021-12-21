s = [4, 8] # starting position
rolls = 0

def roll():
	global rolls
	rolls += 1
	return (rolls - 1) % 100 + 1

def play(i):
	s[i] += roll()
	s[i] = (s[i] - 1) % 10 + 1

p = [0, 0] # points

while p[0] < 1000 and p[1] < 1000:
	for i in range(len(s)):
		for _ in range(3):
			play(i)
		
		p[i] += s[i]
		
		if p[i] >= 1000:
			break

print(rolls * min(p))

r = {} # possible states

def universe(s, p):
	h = hash((*s, *p))

	if h in r: # have we already encountered a state?
		return r[h]

	w = [0, 0] # wins in subsequent universes

	for d in range(27): # 3 * 3 * 3 universes generated after turn
		steps = d // 3 // 3 + d // 3 % 3 + d % 3 + 3
		pos = (s[0] + steps) % 10 + 1

		if p[0] + pos >= 21: # win?
			w[0] += 1
			continue

		*_p, = reversed(universe([s[1], pos - 1], [p[1], p[0] + pos]))
		
		w[0] += _p[0]
		w[1] += _p[1]

	r[h] = w
	return w

print(max(universe([4 - 1, 5 - 1], [0, 0])))