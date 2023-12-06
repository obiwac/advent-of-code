f = open(0).readlines()

*p1_times, = map(int, f[0].split()[1:])
*p1_dists, = map(int, f[1].split()[1:])

*p2_times, = map(int, ["".join(f[0].split()[1:])])
*p2_dists, = map(int, ["".join(f[1].split()[1:])])

for times, dists in ((p1_times, p1_dists), (p2_times, p2_dists)):
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
