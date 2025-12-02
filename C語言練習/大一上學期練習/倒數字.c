#include<stdio.h>
#include<stdlib.h>
int  main(void) 
{
	while(1)
	{
	int a,b;
	while(a<=0)
	{
		printf("輸入數字:");
		scanf("%d",&a);
	}

	printf("倒數字:");
	while(a!=0)
	{
		b=a%10;
		a/=10;
		printf("%d",b);
	}
	printf("\n\n");
	}
}


