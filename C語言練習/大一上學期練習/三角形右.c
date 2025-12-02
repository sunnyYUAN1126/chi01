#include<stdio.h>
#include<stdlib.h>
void fun1(int);
void fun2(int);
int i,a;
int main(void)
{
	int nn=4;
	fun1(nn);
	fun2(nn);
	return 0;
}

void fun1(int nn)
{
	for(i=1;i<=nn;i++)
	{
	        for(a=1;a<=i;a++)
		{
			printf("*");
		}
		printf("\n");
	}
}

void fun2(int nn)
{
	for(i=1;i<=nn;i++)
	{
		for(a=1;a<=nn-i+1;a++)
		{
			printf("*");
		}
		printf("\n");
	}
}

