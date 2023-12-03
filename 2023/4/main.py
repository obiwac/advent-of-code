*f, = map(str.strip, open(0).readlines())
s = 0

for card in f:
	_, numbers = card.split(":")
	winning, got = numbers.split("|")

	*winning, = map(int, winning.split())
	*got, = map(int, got.split())

	a = 0

	for g in got:
		if g in winning:
			if not a: a = 1
			else: a *= 2

	s += a

print(s)
