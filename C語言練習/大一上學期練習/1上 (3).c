#include<stdio.h>
#include<stdlib.h>
int main(void)
{
	float temper[12], sum=0,average;
	int i;
	for(i=0;i<12;i++)
	{
		printf("%d月平均溫度:",i+1);
		scanf("%f",&temper[i]);
		sum=sum+temper[i];
	}
		average=sum/12;
		printf("===================\n");
		printf("年平均溫度:%f\n",average);

		return 0;
	}
