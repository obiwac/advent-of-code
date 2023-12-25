import math
from itertools import chain
from itertools import accumulate
from functools import reduce
from collections import Counter
from collections import defaultdict
from copy import deepcopy

import numpy as np
import heapq

board, path = open(0).read().split('\n\n')
board = board.split('\n')
*out, = map(list, board)
m = max(map(len, board)) + 2

board = [" " * m] + [*map(lambda b: f" {b}{' ' * (m - len(b) - 1)}", board)] + [" " * m]
*transpose, = map("".join, zip(*board))

RIGHT = 0
DOWN = 1
LEFT = 2
UP = 3

y, x, facing = 1, len(board[1].rstrip()) - len(board[1].strip()), RIGHT

def find(letter):
	x = path.find(letter)
	return 999999999 if x < 0 else x

path = path.strip()

while path:
	d = min(find('L'), find('R'), find('U'), find('D'))

	if d == 0:
		break
	
	n = int(path[:d])
	path = path[d:]

	# go forward by n

	for _ in range(n):
		old = (y, x)
		out[y - 1][x - 1] = '>v<^'[facing]

		if facing == RIGHT: x += 1
		if facing == DOWN: y += 1
		if facing == LEFT: x -= 1
		if facing == UP: y -= 1

		if board[y][x] == '.':
			continue

		if board[y][x] == '#':
			y, x = old
			break

		# wrap

		# if facing == RIGHT: x = len(board[y].rstrip()) - len(board[y].strip())
		# if facing == DOWN: y = len(transpose[x].rstrip()) - len(transpose[x].strip())
		# if facing == LEFT: x = len(board[y].rstrip()) - 1
		# if facing == UP: y = len(transpose[x].rstrip()) - 1

		if facing == UP and y == 100: y, x, facing = x + 50, 51, RIGHT
		if facing == LEFT and x == 50 and y >= 51 and y <= 100: y, x, facing = 101, y - 50, DOWN

		if facing == DOWN and y == 51: y, x, facing = x - 50, 100, LEFT
		if facing == RIGHT and x == 101 and y >= 51 and y <= 100: y, x, facing = 50, y + 50, UP

		if facing == DOWN and y == 151: y, x, facing = x + 100, 50, LEFT
		if facing == RIGHT and x == 51 and y >= 151 and y <= 200: y, x, facing = 150, y - 100, UP

		if facing == RIGHT and x == 151: y, x, facing = y + 100, 100, LEFT
		if facing == RIGHT and x == 101 and y >= 101 and y <= 150: y, x, facing = y - 100, 150, LEFT

		if facing == LEFT and x == 0 and y >= 101 and y <= 150: y, x, facing = y - 100, 51, RIGHT
		if facing == LEFT and x == 50 and y >= 1 and y <= 50: y, x, facing = y + 100, 1, RIGHT

		if facing == UP and y == 0 and x >= 51 and x <= 100: y, x, facing = x + 100, 1, RIGHT
		if facing == LEFT and x == 0 and y >= 151 and x <= 200: y, x, facing = 1, y - 100, DOWN

		if facing == UP and y == 0 and x >= 101 and x <= 150: y, x = 200, x - 100
		if facing == DOWN and y == 201: y, x = 1, x + 100

		print(*old, y, x, facing)

		if board[y][x] == '#':
			y, x = old
			break

		if board[y][x] == ' ':
			print("IMPOSSIBLE")

	# change orientation, if possible

	try:
		o = path[0]

	except:
		break

	path = path[1:]

	if o == "R": facing = (facing + 1) % 4
	if o == "L": facing = (facing - 1) % 4

out[y - 1][x - 1] = '@'

for o in out:
	print("".join(o))

print(y, x, facing, 1000 * y + 4 * x + facing)
