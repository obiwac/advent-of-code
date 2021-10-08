#include <stdio.h>
#include <stdint.h>
#include <string.h>
#include <sys/param.h>

#define MAX_FIELDS 20
#define MAX_TICKETS 240

static uint32_t ranges[MAX_FIELDS][2][2];

static inline uint8_t check_range(uint32_t field, uint32_t range) {
	return (field >= ranges[range][0][0] && field <= ranges[range][0][1]) || \
	       (field >= ranges[range][1][0] && field <= ranges[range][1][1]);
}

static inline uint64_t rdtsc(void) {
	uint64_t cycles;
	asm("rdtsc" : "=A" (cycles));
	return cycles;
}

void main(void) {
	// FILE* f = stdin;
	FILE* f = fopen("input", "r");

	// parse ranges

	uint32_t field_count = 0;
	
	for (; fgetc(f) != '\n' && field_count < MAX_FIELDS; field_count++) {
		fscanf(f, "%*[^:]: %u", (uint32_t*) ranges[field_count][0] + 0);
		fscanf(f, "-%u or",     (uint32_t*) ranges[field_count][0] + 1);
		fscanf(f, "%u-",        (uint32_t*) ranges[field_count][1] + 0);
		fscanf(f, "%u\n",       (uint32_t*) ranges[field_count][1] + 1);

		// printf("[[%u %u], [%u %u]]\n", ranges[field_count][0][0], ranges[field_count][0][1],ranges[field_count][1][0], ranges[field_count][1][1]);
	}

	// parse my ticket

	uint32_t my_ticket[MAX_FIELDS]; /// TODO check out VLA's
	fscanf(f, "%*[^:]");

	for (field_count = 0; fgetc(f) != '\n' && field_count < MAX_FIELDS; field_count++) {
		fscanf(f, "%u", my_ticket + field_count);
	}

	// parse other tickets

	uint32_t ticket_count = 0;
	uint32_t tickets[MAX_TICKETS][MAX_FIELDS];
	
	fscanf(f, "%*[^:]\n");

	for (; !feof(f) && ticket_count < MAX_TICKETS; ticket_count++) for (uint32_t i = 0; i < field_count; i++) {
		fgetc(f);
		fscanf(f, "%u", tickets[ticket_count] + i);
	}

	// part 1

	uint32_t error_rate = 0;

	uint32_t valid_ticket_count = 0;
	uint32_t valid_tickets[MAX_TICKETS];

	for (uint32_t i = 0; i < ticket_count; i++) { // iterate through tickets
		uint32_t old_error_rate = error_rate;

		for (uint32_t j = 0; j < field_count; j++) { // iterate through ticket fields
			uint32_t field = tickets[i][j];
			error_rate += field;

			for (uint32_t k = 0; k < field_count; k++) /* iterate through ranges */ if (check_range(field, k)) {
				error_rate -= field;
				break;
			}
		}

		if (error_rate == old_error_rate) {
			valid_tickets[valid_ticket_count++] = i;
		}
	}

	printf("part 1: %u\n", error_rate);

	// part 2

	struct {
		uint32_t bit_count;
		uint32_t mask;
	} candidates[MAX_FIELDS];

	for (uint32_t i = 0; i < field_count; i++) { // iterate through ranges
		candidates[i].mask = (1 << field_count) - 1;

		for (uint32_t j = 0; j < valid_ticket_count; j++) { // iterate through valid tickets
			uint32_t mask = 0;

			printf("%u\n", tickets[valid_tickets[j]][0]);

			for (uint32_t k = 0; k < field_count; k++) { // iterate through ticket fields
				uint32_t field = tickets[valid_tickets[j]][k];
				mask |= check_range(field, i) << k;
			}

			candidates[i].mask &= mask;
		}

		asm("popcnt %1, %0" : "=r" (candidates[i].bit_count) : "r" (candidates[i].mask));
		printf("candidate: r = %u, b = %u, m = %u\n", i, candidates[i].bit_count, candidates[i].mask);

		if (i == 17) exit(1);
	}

	uint32_t keys[MAX_FIELDS];
	uint32_t bit_counts[MAX_FIELDS];

	for (uint32_t i = 0; i < field_count; i++) {
		bit_counts[i] = candidates[i].bit_count;
	}

	for (uint32_t i = 0; i < field_count; i++) {
		uint32_t min_bit_count = -1u;
		uint32_t min_field;

		for (uint32_t j = 0; j < field_count; j++) {
			uint32_t bit_count = bit_counts[j];
			
			if (bit_count < min_bit_count) {
				min_bit_count = bit_count;
				min_field = j;
			}
		}

		bit_counts[min_field] = -1u;
		keys[i] = min_field;
	}

	uint32_t verdict[MAX_FIELDS];

	for (uint32_t i = 0; i < field_count; i++) {
		uint32_t key = keys[i];

		//printf("candidate %u: %u\n", key, candidates[key].mask);

		uint32_t mask = candidates[key].mask;
		asm("bsr %1, %0" : "=r" (verdict[key]) : "r" (mask));
		// printf("%u %u\n", key, verdict[key]);

		for (uint32_t j = 0; j < field_count; j++) {
			//candidates[j].mask ^= mask;
		}
	}

	for (uint32_t i = 0; i < field_count; i++) {
		// printf("%u %u\n", verdict[i], my_ticket[verdict[i]]);
	}
}