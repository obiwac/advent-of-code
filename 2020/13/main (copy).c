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

	unsigned bus_ids[99];
	unsigned timestamp_deltas[99];
	unsigned bus_count = 1;

	fscanf(f, "%u %u", bus_ids, bus_ids);

	for (; !feof(f);) {
		char s[99];
		fscanf(f, "%[x,]s", s);

		timestamp_deltas[bus_count] = (strlen(s) + 1) / 2;
		fscanf(f, "%u", bus_ids + bus_count++);
	}

	unsigned prev_multiple = bus_ids[bus_count - 1];

	for (int i = bus_count - 2; i >= 0; i--) {
		unsigned bus_id = bus_ids[i];
		unsigned timestamp_delta = timestamp_deltas[i + 1];

		printf("%u\n", timestamp_delta);

		unsigned max = MAX(prev_multiple, bus_id);
		for (; (max + timestamp_delta) % prev_multiple || max % bus_id; max++);

		printf("%u %u = %u\n", prev_multiple, bus_id, max);
		
		prev_multiple = max;
	}

	printf("part 2: %u\n", prev_multiple);

	fclose(f);
}