from functools import reduce
from operator import and_

class R:
	def __init__(self, single_char, multiple, data):
		self.single_char = single_char
		self.multiple = multiple
		self.data = data

i = [x.split('\n') for x in open("example-input").read().split("\n\n")]
rules = {}

for r in i[0]:
	r = r.split(': ')

	single_char = r[1][0] == '"'
	data = r[1][1]

	if not single_char:
		multiple = r[1].find('|') != -1
		data = r[1].replace(' |', "").split(' ')

	rules[r[0]] = R(single_char, multiple, data)

def match_rule(s, n, m = False):
	r = rules[n]

	if r.single_char:
		if not s:
			return False

		ret = s[0] == r.data
		s.pop(0)
		return ret
	
	else:
		special = m and n in ("8", "11")

		if r.multiple or special:
			a = b = None

			s1 = s.copy()
			s2 = s.copy()

			if special:
				if n == "8": # basically this rule is saying "match rule 42 at least once"
					ret = False
					while match_rule(s, "42", m): ret = True
					return ret
				
				elif n == "11": # this rule is saying "match rule 42 and then rule 31 an equal number of times"
					c = None
					j = 1

					while 1:
						c = s.copy()
						o = True

						for x in range(j): o &= match_rule(c, "42")
						for x in range(j): o &= match_rule(c, "31")

						if not o:
							break

						j += 1
					
					if j > 1:
						s.clear()
						s.extend(c)
					
					return j > 1

			elif len(r.data) == 4:
				a = match_rule(s1, r.data[0], m) & match_rule(s1, r.data[1], m)
				b = match_rule(s2, r.data[2], m) & match_rule(s2, r.data[3], m)
			
			else:
				a = match_rule(s1, r.data[0], m)
				b = match_rule(s2, r.data[1], m)
			
			if a or b:
				s.clear()
				s.extend(s1 if a else s2)
				return True
			
			else:
				return False
		
		else:
			return reduce(and_, (match_rule(s, x, m) for x in r.data))

result = 0

for s in i[1]:
	l = list(s)
	m = match_rule(l, "0")
	result += m * (not l)

print("part 1:", result)

result = 0

for s in i[1]:
	l = list(s)
	m = match_rule(l, "0", True)
	result += m * (not l)

print("part 2:", result)