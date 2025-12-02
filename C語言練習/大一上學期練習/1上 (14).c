#include<stdio.h>
#include<stdlib.h>
int fun(int);
int x=3;

int main(void)
{
	int a=4,b=6;
	printf("x=%d,a=%d,b=%d\n",x,a,b);
	fun(9);
	printf("x=%d,a=%d,b=%d\n",x,a,b);

	return 0;
}

int fun(int z)
{
	int a=5,b=7;
	 printf("x=%d,a=%d,b=%d\n",x,a,b);
	 x=z;
	 a=11,b=13;
	 printf("x=%d,a=%d,b=%d\n",x,a,b);

	 return 0;
}


