games = open(0).readlines()
s = 0

for game in games:
	print(game)
	a, b = game.split(":")
	_id = int(a.split()[1])

	rounds = b.split("; ")

	impossible = False

	for _round in rounds:
		things = _round.split(", ")

		red = 12
		green = 13
		blue = 14

		for thing in things:
			n, colour = thing.split()
			n = int(n)

			if colour == "red":
				red -= n

			elif colour == "green":
				green -= n

			elif colour == "blue":
				blue -= n

		if red < 0 or green < 0 or blue < 0:
			impossible = True
			break

	if impossible:
		continue

	s += _id

print(s)
