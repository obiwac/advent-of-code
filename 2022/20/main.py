import math
from itertools import chain
from itertools import accumulate
from functools import reduce
from collections import Counter
from collections import defaultdict
from copy import deepcopy

import heapq

*f, = map(int, open(0).read().strip().split('\n'))

class Node:
	def __init__(self, i, val, next = None, prev = None):
		self.i = i
		self.val = val
		self.next = next
		self.prev = prev

	def __repr__(self):
		return f"({self.i} {self.val})"

class Circular_list:
	def __init__(self):
		self.head = None
	
	def add(self, node):
		if self.head == None:
			self.head = node
			node.next = node
			node.prev = node
			return

		node.prev = self.head.prev
		node.next = self.head

		self.head.prev.next = node
		self.head.prev = node

	def shuffle(self):
		start = self.head
		todo = []

		while 1:
			todo.append(start)

			start = start.next
			if start == self.head: break

		# actually shuffle

		for t in todo:
			start = t
			m = t.val - t.val // len(f) * (len(f) - 1)

			if m > 0:
				for _ in range(m % len(f)):
					start = start.next

			if m < 0:
				for _ in range(-m % len(f) + 1):
					start = start.prev

			if start == t:
				continue

			# remove

			if t == self.head:
				self.head = t.next

			o = t.prev
			t.prev.next = t.next
			t.next.prev = o

			# insert

			t.prev = start
			t.next = start.next

			start.next.prev = t
			start.next = t

	def __repr__(self):
		start = self.head
		s = ""
		n = 0

		while 1:
			s += repr(start.val) + " "
			start = start.next
			n += 1

			if start == self.head:
				break

		return f"len({n}), {s}"
	
	def __len__(self):
		start = self.head
		n = 0

		while 1:
			start = start.next
			n += 1

			if start == self.head:
				break

		return n

c = Circular_list()
KEY = 1 # 811589153

# key = KEY % len(f)

for i, x in enumerate(f):
	c.add(Node(i, x * KEY))

print(len(c))

for _ in range(10 if KEY > 1 else 1): 
	c.shuffle()

print(c)
# print(t)
# print(t[1000 % len(f)] + t[2000 % len(f)] + t[3000 % len(f)])

start = c.head

while 1:
	start = start.next
	if start.val == 0: break

print(start)

s = 0
i = 0

while 1:
	if i in (1000, 2000, 3000):
		s += start.val

	if i > 3000:
		break

	i += 1
	start = start.next

print(s)

__import__("time").sleep(0.1)
