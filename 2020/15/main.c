#include <stdio.h>
#include <stdint.h>

#define E 30000000

void main(void) {
	int64_t input[] = {20,9,11,0,1,2};

	int64_t* before_to_last_spoken = malloc(E * sizeof(int64_t));
	for (int j = 0; j < E; j++) before_to_last_spoken[j] = -1;

	int64_t* last_spoken = malloc(E * sizeof(int64_t));
	for (int j = 0; j < E; j++) last_spoken[j] = -1;

	int64_t i = sizeof(input) / sizeof(*input);
	for (int j = 0; j < i; j++) last_spoken[input[j]] = j;

	int64_t part1 = 0;

	int64_t previous = input[i - 1];
	int64_t current = input[i];

	for (; i < E; i++) {
		current = before_to_last_spoken[previous] < 0 ? 0 : last_spoken[previous] - before_to_last_spoken[previous];
		part1 |= i + 1 == 2020 ? current : 0;

		before_to_last_spoken[current] = last_spoken[current], last_spoken[current] = i;
		previous = current;
	}

	printf("part 1: %lu\n", part1);
	printf("part 2: %lu\n", current);

	// part 2 golfed... kinda

	int64_t* u = input;
	int64_t* b = before_to_last_spoken;
	for (int j = 0; j < E; j++) b[j] = -1;
	int64_t* l = last_spoken;
	for (int j = 0; j < E; j++) l[j] = -1;
	i = sizeof(input) / sizeof(*input);
	for (int j = 0; j < i; j++) l[u[j]] = j;
	int64_t c;

	for(int p=(c=u[i],u[i-1]);i<E;c=b[p]<0?0:l[p]-b[p],b[c]=l[c],l[c]=i++,p=c);

	printf("part 2: %lu\n", c);
}