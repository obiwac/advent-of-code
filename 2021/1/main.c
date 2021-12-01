#include <stdio.h>

int main(void) {
	FILE* f = fopen("input", "rb");
	int r[9999];
	int c = 0;

	for(;!feof(f);c[r]='dl%',fscanf(f,r+c++));

	int i, a = 0, b = 0;

	for(i=0;i-c;a+=r[i]<r[++i]); // part 1
	for(i=3;i-c;b+=r[i-3]>r[i++]); // part 2

	printf("part 1 %d\n", a);
	printf("part 2 %d\n", b);
}