#include <stdio.h>
#include <stdint.h>
#include <sys/param.h>
#include <string.h>

#define CUBE_SIZE 32
#define CUBE(x, y, z) (x) + CUBE_SIZE / 2][(y) + CUBE_SIZE / 2][(z) + CUBE_SIZE / 2

uint32_t part1(FILE* f) {
	uint8_t cubes[CUBE_SIZE][CUBE_SIZE][CUBE_SIZE] = { 0 };
	int32_t x = 0, y = 0, z = 0;

	int32_t min_x = -1, min_y = -1, min_z = -1;
	int32_t max_x = 0, max_y = 0, max_z = 0;

	for (; !feof(f); x++) {
		char c = fgetc(f);

		if (c == '\n') y++, x = -1;
		else if (c == '#') cubes[CUBE(x, y, 0)] = 1;
	}

	max_x = 1 + x - 1;
	max_y = 1 + y;
	max_z = 1;

	// part 1
	
	uint8_t prev_cubes[CUBE_SIZE][CUBE_SIZE][CUBE_SIZE];
	uint32_t sum;

	for (uint32_t cycle = 0; cycle < 6; cycle++) {
		memcpy(prev_cubes, cubes, sizeof(cubes));
		sum = 0;

		for (x = min_x; x <= max_x; x++) {
			for (y = min_y; y <= max_y; y++) {
				for (z = min_z; z <= max_z; z++) {
					uint8_t active = prev_cubes[CUBE(x, y, z)];
					int32_t neighbours = -active;

					for (int32_t i = 0; i < 3 * 3 * 3; i++) {
						neighbours += prev_cubes[CUBE(x + i / 9 - 1, y + i / 3 % 3 - 1, z + i % 3 - 1)];
					}

					if (active) cubes[CUBE(x, y, z)] = neighbours == 2 || neighbours == 3;
					else cubes[CUBE(x, y, z)] = neighbours == 3;

					sum += cubes[CUBE(x, y, z)];
				}
			}
		}

		min_x--, min_y--, min_z--;
		max_x++, max_y++, max_z++;
	}

	return sum;
}

#define TESSERACT_SIZE 32
#define TESSERACT(x, y, z, w) (x) + TESSERACT_SIZE / 2][(y) + TESSERACT_SIZE / 2][(z) + TESSERACT_SIZE / 2][(w) + TESSERACT_SIZE / 2

uint32_t part2(FILE* f) {
	uint8_t tesseracts[TESSERACT_SIZE][TESSERACT_SIZE][TESSERACT_SIZE][TESSERACT_SIZE] = { 0 };
	int32_t x = 0, y = 0, z = 0, w = 0;

	int32_t min_x = -1, min_y = -1, min_z = -1, min_w = -1;
	int32_t max_x = 0, max_y = 0, max_z = 0, max_w = 0;

	for (; !feof(f); x++) {
		char c = fgetc(f);

		if (c == '\n') y++, x = -1;
		else if (c == '#') tesseracts[TESSERACT(x, y, 0, 0)] = 1;
	}

	max_x = 1 + x - 1;
	max_y = 1 + y;
	max_z = 1;
	max_w = 1;

	// part 1
	
	uint8_t prev_tesseracts[TESSERACT_SIZE][TESSERACT_SIZE][TESSERACT_SIZE][TESSERACT_SIZE];
	uint32_t sum;
	
	for (uint32_t cycle = 0; cycle < 6; cycle++) {
		memcpy(prev_tesseracts, tesseracts, sizeof(tesseracts));
		sum = 0;

		for (x = min_x; x <= max_x; x++) {
			for (y = min_y; y <= max_y; y++) {
				for (z = min_z; z <= max_z; z++) {
					for (w = min_w; w <= max_w; w++) {
						printf("%d %d %d %d\n", x, y, z, w);

						uint8_t active = prev_tesseracts[TESSERACT(x, y, z, w)];
						int32_t neighbours = -active;

						for (int32_t i = 0; i < 3 * 3 * 3 * 3; i++) {
							neighbours += prev_tesseracts[TESSERACT(x + i / 27 - 1, y + i / 9 % 3 - 1, z + i / 3 % 3 - 1, w + i % 3 - 1)];
						}

						if (active) tesseracts[TESSERACT(x, y, z, w)] = neighbours == 2 || neighbours == 3;
						else tesseracts[TESSERACT(x, y, z, w)] = neighbours == 3;

						sum += tesseracts[TESSERACT(x, y, z, w)];
					}
				}
			}
		}

		min_x--, min_y--, min_z--, min_w--;
		max_x++, max_y++, max_z++, max_w++;
	}

	return sum;
}

void main(void) {
	FILE* f = fopen("input", "rb");
	printf("part 1: %u\n", part1(f));

	rewind(f);
	printf("part 2: %u\n", part2(f));

	fclose(f);
}