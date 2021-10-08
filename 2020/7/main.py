lines = open("input").read().split('.\n')
bags = {}

for line in lines:
	sections = [sections_str.split(' ') for sections_str in line.split(', ')]
	parent_colour = f"{sections[0][0]} {sections[0][1]}"

	bag = []
	bags[parent_colour] = bag

	if sections[0][4] == "no":
		continue

	sections[0] = sections[0][4: len(sections[0])]

	for section in sections:
		count = int(section[0])
		colour = f"{section[1]} {section[2]}"

		bag.append({"count": count, "colour": colour})

# part 1

colours = set()

def recurse(colour):
	global colours
	back_propagate = False

	for child in bags[colour]:
		if child["colour"] == "shiny gold": back_propagate = True
		back_propagate = back_propagate or recurse(child["colour"])
	
	if back_propagate:
		colours.add(colour)

	return back_propagate

for colour in bags:
	recurse(colour)

print(f"part 1: {len(colours)}")

# part 2

count = 0

def recurse(colour):
	global count

	for child in bags[colour]:
		for i in range(child["count"]):
			recurse(child["colour"])
			count += 1

recurse("shiny gold")
print(f"part 2: {count}")