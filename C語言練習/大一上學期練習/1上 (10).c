#include<stdio.h>
#include<stdlib.h>
int fun(int);
int x=3;

int main(void)
{
	
	printf("x=%d\n",x);
        fun(9);
	printf("x=%d\n",x);

	return 0;
}

int fun(int x)
{
	printf("x=%d\n",x);
}
