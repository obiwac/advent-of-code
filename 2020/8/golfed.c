#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>

void main(void) {
	FILE* f = fopen("input", "r");

	// parse instructions

	int c=1,r[9999];
	l:{char a[9]={'%','s'-c%2*15};
	fscanf(f,a);
	memcpy(r+c,a,9);}
	if(++c>0&&!(fgetc(f)>>8))goto l;

	// part 1

	int a,i=2,e[999];
	for(;i<c/2;i+=c*e[++i]){
		e[i]++;
		char o=*(r+i*2);
		if(o-'n')*(o^97?&i:&a)+=*(r+i*2+1);
	}

	printf("part 1: %d\n", a);
}