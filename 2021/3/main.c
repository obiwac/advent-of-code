#include <stdio.h>

int main(void) {
	FILE* f = fopen("input", "rb");

	unsigned a[9999];
	int sz, c = 0;

	for (; !feof(f); c++) {
		int accum = 0;

		sz = 0;
		for (char x; fscanf(f, "%c", &x) + 1 && x != '\n'; sz++) {
			accum <<= 1;
			accum += x - 0x30;
		}

		a[c] = accum;
	}

	// part 1

	unsigned gamma = 0;

	for (int i = 0; i < sz; i++) {
		unsigned mask = 1 << (sz - i - 1);
		unsigned ones = 0;

		for (int j = 0; ones += !!(a[j] & mask), j < c; j++);
		gamma |= mask * (ones > c / 2);
	}
	
	printf("part1 %d\n", gamma * (~gamma & (1 << sz) - 1));

	// part 2
	// this is hell

	unsigned gen = 0, scrub = 0;

	unsigned gen_excl[9999] = { 0 };
	unsigned scrub_excl[9999] = { 0 };

	unsigned valid = 2;

	for (int i = 0; i < sz && valid > 1; i++) {
		unsigned mask = 1 << (sz - i - 1);
		unsigned ones = 0, cnt = 0;

		for (int j = 0; cnt += !!(a[j] ^ gen_excl[j]), ones += !!((a[j] ^ gen_excl[j]) & mask), j < c; j++);
		for (int j = 0; gen_excl[j] |= a[j] * ((ones < (cnt + 1) / 2) ^ !(a[j] & mask)), j < c; j++);

		valid = 0;
		
		for (int i = 0; i < c; i++) {
			if (!gen_excl[i]) {
				gen = a[i];
				valid++;
			}
		}
	}

	valid = 2;

	for (int i = 0; i < sz && valid > 1; i++) {
		unsigned mask = 1 << (sz - i - 1);
		unsigned ones = 0, cnt = 0;

		for (int j = 0; cnt += !!(a[j] ^ scrub_excl[j]), ones += !!((a[j] ^ scrub_excl[j]) & mask), j < c; j++);
		for (int j = 0; scrub_excl[j] |= a[j] * ((ones >= (cnt + 1) / 2) ^ !(a[j] & mask)), j < c; j++);

		valid = 0;

		for (int i = 0; i < c; i++) {
			if (!scrub_excl[i]) {
				scrub = a[i];
				valid++;
			}
		}
	}

	printf("part2 %d\n", gen * scrub);
}