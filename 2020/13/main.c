#include <stdio.h>
#include <string.h>
#include <stdint.h>
#include <sys/param.h>

void main(void) {
	FILE* f = fopen("input", "r");

	// part 1

	unsigned min_timestamp;
	fscanf(f, "%u", &min_timestamp);

	unsigned best_timestamp_delta = -1u;
	unsigned best_bus_id;

	for (; !feof(f);) {
		unsigned bus_id;
		fscanf(f, "%u%*[x,]", &bus_id);

		unsigned timestamp_delta = bus_id - min_timestamp % bus_id;

		if (timestamp_delta < best_timestamp_delta) {
			best_timestamp_delta = timestamp_delta;
			best_bus_id = bus_id;
		}
	}

	printf("part 1: %u\n", best_timestamp_delta * best_bus_id);

	// part 2

	rewind(f);
	uint64_t prev_multiple;
	fscanf(f, "%lu %lu", &prev_multiple, &prev_multiple);

	uint64_t timestamp_delta = 0;
	uint64_t increment = prev_multiple;
	prev_multiple = 0;

	for (; !feof(f);) {
		char s[99];
		fscanf(f, "%[x,]s", s);

		timestamp_delta += (strlen(s) + 1) / 2;
		
		uint64_t bus_id;
		fscanf(f, "%lu", &bus_id);

		uint64_t timestamp = prev_multiple;
		for (; (timestamp + timestamp_delta) % bus_id; timestamp += increment);

		prev_multiple = timestamp;
		increment *= bus_id;
	}

	printf("part 2: %lu\n", prev_multiple);

	fclose(f);
}