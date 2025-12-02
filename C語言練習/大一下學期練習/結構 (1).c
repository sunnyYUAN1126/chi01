#include<stdio.h>
#include<stdlib.h>
int main(void)
{
	struct date
	{
		int acc;
		char bcc[10];
	}stry;

	gets(stry.bcc);
	scanf("%d",&stry.acc);

	puts(stry.bcc);
	printf("%d\n",stry.acc);
}


