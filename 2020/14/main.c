#include <stdio.h>
#include <stdint.h>
#include <string.h>

typedef struct {
	uint64_t addresses[1 << 17];
	uint64_t memory[1 << 17];

	uint64_t address_counter;
} memory_space_t;

static void set_memory(memory_space_t* memory, uint64_t address, uint64_t mask_floating, uint64_t value) { // 4795970362286
	uint64_t bit_count;
	asm("popcnt %1, %0\n" : "=r" (bit_count) : "r" (mask_floating));
	
	for (uint64_t i = 0; i < 1 << bit_count; i++) {
		uint64_t current_floating;
		asm("pdep %2, %1, %0\n" : "=r" (current_floating) : "r" (i), "r" (mask_floating));

		uint64_t current_address = address | current_floating;

		for (uint64_t j = 0; j < memory->address_counter; j++) {
			if (memory->addresses[j] == current_address) {
				memory->memory[j] = value;
				goto end;
			}
		}

		memory->addresses[memory->address_counter] = current_address;
		memory->memory[memory->address_counter++] = value;

		end:;
	}
}

void main(void) {
	FILE* f = fopen("input", "rb");

	uint64_t mask_value_part1, mask_part1;
	uint64_t mask_part2, mask_floating_part2;

	uint64_t memory_part1[1 << 16] = { 0 };

	memory_space_t memory_part2;
	memset(&memory_part2, 0, sizeof(memory_part2));

	for (; !feof(f);) {
		char instruction[99];
		fscanf(f, "%[^\[X10]s", instruction);

		if (instruction[1] ^ 'a') { // mem instruction
			uint64_t address;
			fscanf(f, "[%lu", &address);

			uint64_t value;
			fscanf(f, "] = %lu\n", &value);

			//printf("mem[%u] = %lu\n", address, value);

			uint64_t value_part1 = value;
			value_part1 &= mask_part1;
			value_part1 |= mask_value_part1;
			memory_part1[address] = value_part1;

			address |= mask_part2;
			address &= ~mask_floating_part2;
			set_memory(&memory_part2, address, mask_floating_part2, value);
			//exit(1);

		} else { // mask instruction
			mask_value_part1 = mask_part1 = 0;
			mask_part2 = mask_floating_part2 = 0;

			for (char c, i = 35; (c = fgetc(f)) != '\n'; i--) {
				if (c ^ 'X') mask_value_part1 |= (uint64_t) !(c ^ '1') << i;
				else mask_part1 |= 1ul << i;

				if (c ^ 'X') mask_part2 |= (uint64_t) !(c ^ '1') << i;
				else mask_floating_part2 |= 1ul << i;
			}

			//printf("mask = 0x%lx, 0x%lx\n", mask_value_part1, mask_part1);
		}
	}

	uint64_t sum_part1 = 0;
	for (int i = 0; i < 1 << 16; i++) {
		sum_part1 += memory_part1[i];
	}

	printf("part 1: %lu\n", sum_part1);

	uint64_t sum_part2 = 0;
	for (int i = 0; i < memory_part2.address_counter; i++) {
		sum_part2 += memory_part2.memory[i];
	}

	printf("part 2: %lu\n", sum_part2);
}