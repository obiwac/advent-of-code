f = open(0).readlines()

*times, = map(int, f[0].split()[1:])
*dists, = map(int, f[1].split()[1:])

s = 1

for time, dist in zip(times, dists):
	ways = 0

	for press_time in range(time + 1):
		speed = press_time
		remaining_time = time - press_time

		if speed * remaining_time > dist:
			ways += 1

	s *= ways

print(s)
