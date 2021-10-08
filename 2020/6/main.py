answers = open("input").readlines()
answers.append('\n')

# part 1

_sum = 0
questions = set()

for answer in answers:
	if answer == '\n':
		_sum += len(questions)
		questions = set()
		continue
	
	for question in answer.replace('\n', ""):
		questions.add(question)

print(f"part 1: {_sum}")

# part 2

_sum = 0
people = 0
questions = dict()

for answer in answers:
	if answer == '\n':
		for question in questions:
			if questions[question] == people:
				_sum += 1

		questions = dict()
		people = 0

		continue
	
	for question in answer.replace('\n', ""):
		if not question in questions: questions[question] = 0
		questions[question] += 1
	
	people += 1

print(f"part 2: {_sum}")

# part 1 better

i = open("input").read()

result = sum(map(lambda answer: len(set(answer.replace('\n', ""))), open("input").read().split("\n\n")))
print(f"part 1: {result}")

# part 2 better

from functools import reduce
from operator import and_

result = sum(map(lambda a: bin(reduce(and_, map(lambda p: sum(map(lambda q: 1 << (ord(q) - 0x61), set(p.replace('\n', "")))), a.split('\n')))).count('1'), open("input").read().split("\n\n")))
print(f"part 2: {result}")

# part 1 even better

r=1-sum(1-len(set(a))for a in i.split('\n'*2))
print(f"part 1: {r}")

# part 2 even better

r=sum(len(reduce(and_,(set(p)for p in a.split('\n'))))for a in i.split('\n'*2))
print(f"part 2: {r}")