#include<stdio.h>
#include<stdlib.h>
int main(void)
{
	int i=1,sum=0;
	while(sum<=100)
	{
		sum+=i;
		printf("i=%3d,sum=%3d\n", i, sum);
		i++;
	}
	printf("***i=%3d,sum=%3d\n",i,sum);
	printf("必須累加到%d\n",i-1);
	for(i=1,sum=0;sum<=100; i++)
	{
		sum+=i;
		printf("i=%3d,sum=%3d\n",i,sum);
	}
	printf("***i=%3d,sum=%3d\n",i,sum);
	return 0;
}

