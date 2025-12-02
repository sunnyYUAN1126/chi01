#include<stdio.h>
#include<stdlib.h>
void fun(void);
int main(void)
{
	fun();
	fun();
	fun();
	return 0;
}

void fun(void)
{
	static int a=10;
	printf("a=%d\n",a);
	a+=10;
}
