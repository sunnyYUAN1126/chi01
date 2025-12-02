#include<stdio.h>
#include<stdlib.h>
int fun(int *);
int main(void)
{
	int a=9,*ptr;
	ptr=&a;
	fun(&a);
	fun(ptr);
}
int fun(int *ptr)
{
	printf("%p,%d\n",ptr,*ptr);
}












