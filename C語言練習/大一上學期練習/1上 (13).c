#include<stdio.h>
#include<stdlib.h>
int fun(int a);
int main(void)
{
	int a;
	int b=fun(a);
	printf("%d\n",b);
}

int fun(int b) {
	b=10;
	printf("%d\n",b);

	return 11;
}
