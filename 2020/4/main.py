required_keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

lines = open("input")

passports = []
current_passport = {"required_keys": 0}

for line in lines:
	if line == '\n':
		passports.append(current_passport)
		current_passport = {"required_keys": 0}
	
	else:
		fields = line.split(' ')

		for field in fields:
			key, value = field.split(':')
			
			current_passport[key] = value.replace('\n', "")
			current_passport["required_keys"] += key in required_keys

passports.append(current_passport)
passports_with_valid_keys = []

for passport in passports:
	if passport["required_keys"] == len(required_keys):
		passports_with_valid_keys.append(passport)

print(f"part 1: {len(passports_with_valid_keys)}")

# part 2

passports_with_valid_values = []
eye_colours = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

for passport in passports_with_valid_keys:
	try: int(passport["byr"])
	except ValueError: continue
	if not int(passport["byr"]) in range(1920, 2002 + 1): continue

	try: int(passport["iyr"])
	except ValueError: continue
	if not int(passport["iyr"]) in range(2010, 2020 + 1): continue

	try: int(passport["eyr"])
	except ValueError: continue
	if not int(passport["eyr"]) in range(2020, 2030 + 1): continue

	height = passport["hgt"]
	height_unit = height[-2: len(height)]

	try: height = int(height[0: -2])
	except ValueError: continue

	if height_unit == "cm":
		if not height in range(150, 193 + 1): continue
		
	elif height_unit == "in":
		if not height in range(59, 76 + 1): continue

	else:
		continue

	if passport["hcl"][0] != '#': continue
	if len(passport["hcl"]) != 7: continue

	try: int(passport["hcl"][1: len(passport["hcl"])], 16)
	except ValueError: continue

	if not passport["ecl"] in eye_colours:
		continue

	if len(passport["pid"]) != 9: continue
	try: int(passport["pid"])
	except ValueError: continue

	passports_with_valid_values.append(passport)

print(f"part 2: {len(passports_with_valid_values)}")