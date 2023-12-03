*f, = map(str.strip, open(0).readlines())
s = 0
card_counts = []

for card in f:
	_, numbers = card.split(":")
	winning, got = numbers.split("|")

	*winning, = map(int, winning.split())
	*got, = map(int, got.split())

	a = 0
	card_count = 0

	for g in got:
		if g in winning:
			if not a: a = 1
			else: a *= 2

			card_count += 1

	card_counts.append(card_count)
	s += a

instances = [1] * len(card_counts)

for i, card_count in enumerate(card_counts):
	for j in range(card_count):
		instances[i + 1 + j] += 1 * instances[i]

print(s)
print(sum(instances))
