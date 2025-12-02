#include<stdio.h>
#include<stdlib.h>
int main(void)
{
	int a1,a2,a3,a4,a5;
	int i,mix,max;
	printf("輸入5數字:");
	scanf("%d %d %d %d %d",&a1,&a2,&a3,&a4,&a5);
        int arr[5]={a1,a2,a3,a4,a5};
	
	
	for(i=4;i>=0;i--)
	{
		arr[5]=i;
		printf("%3d",arr[i]);
	}
	printf("\n");

	mix=arr[0];
	max=arr[0];
	for(i=0;i<5;i++)
	{
		if(arr[i]>max)
		{  max=arr[i]; }

		if(arr[i]<mix)
		{  mix=arr[i]; }
	}
	printf("最大值%d\n",max);
	printf("最小值%d\n",mix);
}
