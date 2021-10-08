#include <stdio.h>
#include <stdint.h>
#include <sys/param.h>
void main(int argc,char*argv[]){
	if(argc==1)return;
	FILE*f=fopen(argv[1],"r");
	int64_t c,r[9999],b,p=25,i=p,j=0,k,a,M,m;

	//parse
	l:c[r]='dl%';
	fscanf(f,r+c++);
	if(!feof(f))goto l;

	//part 1
	f:i++;b=0;
	for(;p-(b+=(8+b>>5)*(b%32>=p)+1)/32;)
	if(!(i[r]-r[i-b%32]^r[i-b/32]))goto f;
	printf("%ld\n",i[r]);

	//part 2
	for(;M=0,m=-1u;a=i[r])
	for(k=j++;M=MAX(M,k[r]),m=MIN(m,k[r]),k<i;)
	if(!(a-=k++[r]))goto t;
	t:a=M+m;
	printf("%ld\n",a);
}
