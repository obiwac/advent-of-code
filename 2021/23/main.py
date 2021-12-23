from itertools import chain
from itertools import accumulate
from functools import reduce
from collections import Counter
from operator import mul

# f = ["CD", "AC", "BA", "DB"]

class Amphipod:
	def __init__(self, t):
		self.t = t

buf = []
top = [Amphipod("B"), Amphipod("C"), Amphipod("B"), Amphipod("D")]
bot = [Amphipod("A"), Amphipod("D"), Amphipod("C"), Amphipod("A")]

def move()

while "".join(sorted(top)) != "ABCD" or "".join(sorted(bot)) != "ABCD":
	for t in top:

print(sorted(top))