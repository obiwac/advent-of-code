*f, = map(str, open(0).read().strip().split('\n'))
d = {}

for i in f:
	in_, out = i.split(" -> ")
	kind = "broadcaster"
	
	if in_[0] == "%":
		in_ = in_[1:]
		kind = "flipflop"

	if in_[0] == "&":
		in_ = in_[1:]
		kind = "conjunction"

	# (kind, [ins], [out], flipflop_state, conjunction_mem)
	d[in_] = [kind, [], out.split(", "), False, {}]

to_add = []

for k, v in d.items():
	for o in v[2]:
		if o not in d:
			to_add.append(o)
			continue

		if d[o][0] == "conjunction":
			kind, ins, out, flipflop_state, mem = d[o]
			ins.append(k)
			mem[k] = False

for i in to_add:
	d[i] = ["idkfam", [], [], False, False]

low_count = 0
high_count = 0

for _ in range(1000):
	q = [("broadcaster", False, "button")]

	while q:
		name, is_high, prev = q.pop(0)
		kind, ins, out, flipflop_state, mem = d[name]

		is_high_name = "high" if is_high else "low"
		print(f"{prev} -{is_high_name}-> {name}")

		low_count += not is_high
		high_count += is_high

		if kind == "broadcaster":
			for o in out:
				if d[o][0] == "conjunction": d[o][4][name] = is_high
				q.append((o, is_high, name))

		if kind == "flipflop":
			if is_high:
				continue

			flipflop_state = not flipflop_state
			d[name][3] = flipflop_state

			for o in out:
				if d[o][0] == "conjunction": d[o][4][name] = flipflop_state
				q.append((o, flipflop_state, name))

		if kind == "conjunction":
			s = sum(mem.values())

			for o in out:
				if d[o][0] == "conjunction": d[o][4][name] = s != len(ins)
				q.append((o, s != len(ins), name))

print(low_count * high_count)
