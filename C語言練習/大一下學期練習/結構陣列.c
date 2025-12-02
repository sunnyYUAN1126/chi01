#include<stdio.h>
#include<stdlib.h>
int main(void)
{
	int i;
	struct date
	{
		int a;
		char arr[10];
	}stry[2];

	for( i=0;i<2;i++)
	{
		scanf("%d",&stry[i].a);
		//printf("%d\n",stry[i].a);
		scanf("%s",&stry[i].arr);
		printf("%d\n",stry[i].a);
		printf("%s\n",stry[i].arr);
		fflush(stdin);
	}

}



