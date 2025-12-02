#include<stdio.h>
#include<stdlib.h>
int main(void)
{
	int a;
	for(a=1;a<=10;a++)
	{
		if(a%9==0)
		{ break; }

		if(a%2==0)
		{ continue;}

		printf("a=%d\n",a);
	}

	printf("跳離迴圈,a=%d\n",a);
        
	return 0;
}

