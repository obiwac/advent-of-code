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
