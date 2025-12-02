#include<stdio.h>
#include<stdlib.h>
int fun();
int fun2(int a,int ib);
int main(void)
{
	fun();
	int b=1;
	int a=fun2(10,b);
	printf("%d",a);
}

int fun() {
	printf("123\n");
}

int fun2(int a,int b) {
	a=a+10;
	b=b+5;
	printf("%d %d\n",a,b);

	return 100;
}

