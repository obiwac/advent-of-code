#include <stdio.h>
#include <fcntl.h>

int main(void) {
	char a[9999];
	int n[9999];
	int c = 0;

	for (; !feof(f); c++) {
		fscanf(f, "%s %d", a + c, n + c);
	}

	int x = 0, y = 0;

	for (int i = 0; i < c; i++) {
		x += n[i]*(a[i]=='f')-n[i]*(a[i]=='b');
		y += n[i]*(a[i]=='d')-n[i]*(a[i]=='u');
	}
	printf("%d\n", x * y);
}