
lines = open(0).read().split('\n\n')
draws = map(int, lines[0].split(','))
boards = [[[[int(x), False] for x in map(str.strip, row.split(' ')) if x] for row in line.split('\n')] for line in lines[1:]]

winners = []
values = []

for draw in draws:
	for board in boards:
		# already won?

		if str(board) in map(str, winners):
			continue

		# contains winning number?

		for val in sum(board, []):
			val[1] |= val[0] == draw

		# won?

		o = len(winners)

		for row in board:
			winners += [board] * (sum(x[1] for x in row) == 5)
		
		if o < len(winners):
			values.append(draw)
			continue

		for col in zip(*board):
			winners += [board] * (sum(x[1] for x in col) == 5)
		
		if o < len(winners):
			values.append(draw)
	
	# enough winners?

	if len(winners) == len(boards):
		break

*winners, = map(lambda winner: sum([x for x, y in sum(winner, []) if not y]), winners)

print(values[0] * winners[0])
print(values[-1] * winners[-1])