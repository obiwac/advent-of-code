#include <stdio.h>

int main(void) {
	FILE* f = fopen("input", "rb");

	char a[9999];
	int n[9999];
	int c = 0;

	for (; !feof(f); c++) {
		fscanf(f, "%s %d", a + c, n + c);
	}

	// actual code

	
}