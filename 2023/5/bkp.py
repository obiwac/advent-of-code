*f, = open(0).read().strip().split('\n')

*seeds, = map(int, f[0].split(":")[1].split())
maps = {}
inv_maps = {}

i = 1
state = ""

while 1:
	if f[i].startswith("seed-to-soil"):
		state = "seed_to_soil"

	if f[i].startswith("soil-to-fertilizer"):
		state = "soil_to_fertilizer"

	if f[i].startswith("fertilizer-to-water"):
		state = "fertilizer_to_water"

	if f[i].startswith("water-to-light"):
		state = "water_to_light"
	
	if f[i].startswith("light-to-temperature"):
		state = "light_to_temperature"
	
	if f[i].startswith("temperature-to-humidity"):
		state = "temperature_to_humidity"
	
	if f[i].startswith("humidity-to-location"):
		state = "humidity_to_location"

	if state not in maps:
		maps[state] = {}

	try:
		dest_start, src_start, r = map(int, f[i].split())
		maps[state][(src_start, src_start + r)] = dest_start

	except:
		pass

	i += 1

	if i >= len(f):
		break

s = float("inf")

def get(state, v):
	for k, u in maps[state].items():
		if v >= k[0] and v < k[1]:
			return u + (v - k[0])

	return v

def get_invert(state, v):
	for k, u in maps[state].items():
		if v >= u and v < u + (k[1] - k[0]):
			return k[0] + (v - u)

	return v

for seed in seeds:
	soil = get("seed_to_soil", seed)
	fertilizer = get("soil_to_fertilizer", soil)
	water = get("fertilizer_to_water", fertilizer)
	light = get("water_to_light", water)
	temperature = get("light_to_temperature", light)
	humidity = get("temperature_to_humidity", temperature)
	location = get("humidity_to_location", humidity)

	s = min(s, location)

print(s)

# find first location in seeds

location = 17700000

while 1:
	humidity = get_invert("humidity_to_location", location)
	temperature = get_invert("temperature_to_humidity", humidity)
	light = get_invert("light_to_temperature", temperature)
	water = get_invert("water_to_light", light)
	fertilizer = get_invert("fertilizer_to_water", water)
	soil = get_invert("soil_to_fertilizer", fertilizer)
	seed = get_invert("seed_to_soil", soil)

	# check seed

	for i in range(0, len(seeds), 2):
		if seed >= seeds[i] and seed < seeds[i] + seeds[i + 1]:
			print(location)
			exit()

	location += 1

	if location % 100000 == 0:
		print(location)

__import__("time").sleep(0.1)
