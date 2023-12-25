import math
from itertools import chain
from itertools import accumulate
from functools import reduce
from collections import Counter
from collections import defaultdict
from copy import deepcopy

import numpy as np
import heapq

f = open(0).read().strip().split('\n\n')

candidates2 = set()
visited = {}

# state: ore, clay, obsidian, geodes, ore robots, clay robots, obsidian robots, geode robots

def dfs(params, state = (0, 0, 0, 0, 1, 0, 0, 0), minute = 0):
	ore_robot_cost, clay_robot_cost, obs_robot_cost_ore, obs_robot_cost_clay, geode_robot_cost_ore, geode_robot_cost_obs = params
	geodes = state[3]

	if minute == 10:
		print(state)
		candidates2.add(geodes)
		return

	if (state, minute) in visited and visited[(state, minute)] >= geodes:
		return

	visited[(state, minute)] = geodes

	# buy

	*prev, = state
	*state, = state

	if state[0] >= geode_robot_cost_ore and state[2] >= geode_robot_cost_obs:
		state[0] -= geode_robot_cost_ore
		state[2] -= geode_robot_cost_obs

		state[7] += 1

	need_more_obs = state[2] / geode_robot_cost_obs < state[0] / geode_robot_cost_ore

	if need_more_obs and state[0] >= obs_robot_cost_ore and state[1] >= obs_robot_cost_clay:
		state[0] -= obs_robot_cost_ore
		state[2] -= obs_robot_cost_clay

		state[6] += 1

	need_more_clay = state[1] / obs_robot_cost_clay < state[0] / obs_robot_cost_ore

	if need_more_clay and state[0] >= clay_robot_cost:
		state[0] -= clay_robot_cost
		state[5] += 1

	can_ore = state[0] // ore_robot_cost
	
	for i in range(can_ore + 1):
		*new, = state

		new[4] += i
		new[i] -= i * ore_robot_cost

		new[0] += prev[4]
		new[1] += prev[5]
		new[2] += prev[6]
		new[3] += prev[7]

		dfs(params, tuple(new), minute + 1)

	return # OLD

	# check how much we can buy

	*prev, = state

	# check spending states

	can_ore = state[0] // ore_robot_cost

	for i in range(can_ore + 1):
		new_ore_robots = prev[4] + i
		new_ores = prev[0] - i * ore_robot_cost
		can_clay = new_ores // clay_robot_cost

		for j in range(can_clay + 1):
			*new, = prev

			# ore robot cost

			new[4] = new_ore_robots
			new[0] = new_ores

			# clay robot cost

			new[5] += j
			new[0] -= j * clay_robot_cost

			# obs & geode robot costs
			# TODO do we also need to iterate over all possibilities?

			can_obs = min(new[0] // obs_robot_cost_ore, new[1] // obs_robot_cost_clay)
			new[6] += can_obs
			new[0] -= can_obs * obs_robot_cost_ore
			new[1] -= can_obs * obs_robot_cost_clay
			
			can_geode = min(new[0] // geode_robot_cost_ore, new[2] // geode_robot_cost_obs)
			new[7] += can_geode
			new[0] -= can_geode * geode_robot_cost_ore
			new[2] -= can_geode * geode_robot_cost_obs

			# update counts with previous state

			new[0] += state[4]
			new[1] += state[5]
			new[2] += state[6]
			new[3] += state[7]

			# if minute > 5:
			# 	print(minute, new)
			# 	return

			dfs(params, tuple(new), minute + 1)

qualities = []

for g in f:
	g = g.split('\n')
	n = int(g[0][len("Blueprint "): -1])
	*g, = map(lambda x: x.strip().split(), g[1:])

	a = int(g[0][4])
	b = int(g[1][4])
	c, d = int(g[2][4]), int(g[2][7])
	e, f = int(g[3][4]), int(g[3][7])

	# ore = 0
	# clay = 0
	# obs = 0
	# geode = 0

	# ore_rob = 1
	# clay_rob = 0
	# obs_rob = 0
	# geode_rob = 0

	# for m in range(24):
	# 	if ore >= e and obs >= f:
	# 		ore -= e
	# 		obs -= f

	# 		geode_rob += 1

	# 	need_more_obs = obs / e < ore / f

	# 	if need_more_obs and ore >= c and clay >= d:
	# 		ore -= c
	# 		clay -= d

	# 		obs_rob += 1

	# 	need_more_clay = clay / d < ore / c

	# 	if need_more_clay and ore >= b:
	# 		ore -= b
	# 		clay_rob += 1

	# 	if ore >= a:
	# 		ore -= a
	# 		ore_rob += 1

	# 	ore += ore_rob
	# 	clay += clay_rob
	# 	obs += obs_rob
	# 	geode += geode_rob

	# print(n, geode)
	# qualities.append(n * geode)

	candidates2 = set()
	visited = {}

	dfs((a, b, c, d, e, f))
	print(n, max(candidates2))
	qualities.append(n * max(candidates2))

print(sum(qualities))
