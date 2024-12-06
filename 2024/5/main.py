f = open(0).read().split("\n\n")

def gorder(set_):
	numbers = {}

	for o in f[0].split("\n"):
		a, b = map(int, o.split("|"))

		if a not in set_ or b not in set_:
			continue

		if a not in numbers:
			numbers[a] = {"before": [], "after": []}

		if b not in numbers:
			numbers[b] = {"before": [], "after": []}

		numbers[a]["before"].append(b)
		numbers[b]["after"].append(a)

	gorder = []

	while 1:
		for i in numbers:
			if numbers[i]["after"] == []:
				gorder.append(i)

				for j in numbers:
					if i in numbers[j]["after"]:
						numbers[j]["after"].remove(i)

				del numbers[i]
				break

		else:
			break

	return gorder

for p in (1, 2):
	s = 0

	for o in f[1].strip().split("\n"):
		*a, = map(int, o.split(","))

		translate = {}
		translate_b = {}

		for i, o in enumerate(gorder(a)):
			translate[o] = i
			translate_b[i] = o

		*translated, = map(lambda x: translate[x], a)
		*sort, = sorted(translated)

		if (p == 1 and sort != translated) or (p == 2 and sort == translated):
			continue

		*untranslated, = map(lambda x: translate_b[x], sort)

		s += untranslated[len(untranslated) // 2]

	print(s)
