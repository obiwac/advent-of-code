#include <stdio.h>
#include <stdint.h>
#include <string.h>

static void bin(const char* msg, uint64_t x) {
	printf("%s", msg);
	for (int i = 35; i >= 0; i--) printf("%ld", (x >> i) & 1ul);
	printf("\n");
}

typedef struct {
	uint64_t addresses[1 << 16];
	uint64_t memory[1 << 16];

	uint16_t address_counter;
} memory_space_t;

int in = 0;

static void write_memory(memory_space_t* memory, uint64_t address, uint64_t value) {
	//printf("writing %lu at address %lu ...\n", value, memory->address_counter);

	for (uint16_t i = 0; i < 1 << 16; i++) {
		if (memory->addresses[i] == address) {
			in++;
			memory->memory[i] = value;
			return;
		}
	}

	memory->addresses[memory->address_counter] = address;
	memory->memory[memory->address_counter] = value;

	memory->address_counter++;
}

static void set_memory(memory_space_t* memory, uint64_t address, uint64_t mask_floating, uint64_t value) {
	if (!mask_floating) {
		//printf("%lu\n", address);
		//bin("", address);
		write_memory(memory, address, value);
		return;
	}
	
	uint64_t bit_index;
	asm("bsr %1, %0\n" : "=r" (bit_index) : "r" (mask_floating));

	uint64_t next = 1ul << bit_index;

	set_memory(memory, address, mask_floating & ~next, value);
	set_memory(memory, address | next, mask_floating & ~next, value);
}

void main(void) { // 4795970362286
	FILE* f = fopen("input", "rb");

	uint64_t mask_value_part1, mask_part1;
	uint64_t mask_part2, mask_floating_part2;

	memory_space_t memory_part1;
	memset(&memory_part1, 0, sizeof(memory_part1));

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
			//write_memory(&memory_part1, address, value_part1);

			address |= mask_part2;
			address &= ~mask_floating_part2;
			set_memory(&memory_part2, address, mask_floating_part2, value);

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

	printf("in: %u\n", in);

	uint64_t sum_part1 = 0;
	for (int i = 0; i < memory_part1.address_counter; i++) {
		sum_part1 += memory_part1.memory[i];
	}

	printf("part 1: %lu\n", sum_part1);

	uint64_t sum_part2 = 0;
	for (int i = 0; i < memory_part2.address_counter; i++) {
		sum_part2 += memory_part2.memory[i];
	}

	printf("part 2: %lu\n", sum_part2);
}