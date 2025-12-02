#include<stdio.h>
#include<stdlib.h>
int add(int n1,int n2);
int main(void)
{
	int sum,a=5,b=3;
	sum=add(a,b);
	printf("%d+%d=%d\n",a,b,a+b);

	return 0;
}

int add(int n1,int n2)
{
	int a;
	a=n1+n2;

	return a;
}


