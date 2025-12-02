#include<stdio.h>
#include<stdlib.h>
int fun(int);
int main(void)
{
	int n;
	scanf("%d",&n);
	printf("fun(%d)=%d\n",n,fun(n));

	return 0;
}

int fun(int n)
{
	
	if(n>0) {
		return(n*fun(n-1));
	}

	else {
	     return 1;
	}

}

