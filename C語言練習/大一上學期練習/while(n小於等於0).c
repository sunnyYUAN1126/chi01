#include<stdio.h>
#include<stdlib.h>
int main(void)
{
	int i;
	printf("輸入數字(n>0):\n");
	scanf("%d",&i);

//	for不能用喔

	while(i<=0)
	{
		printf("輸入n>0:");
		scanf("%d",&i);
	}

	if(i>0)
	{
		printf("你輸入的數字為%d\n",i);
	}
}
