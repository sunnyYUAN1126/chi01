#include<stdio.h>
#include<stdlib.h>
int main(void)
{
	int i,a,b,mix,max;
	int arr[5];
	for(i=0;i<5;i++)
	{
		printf("輸入數字(共5個):");
		scanf("%d",&a);
                arr[i]=a;
	}
	printf("arr[5]    =");
	for(i=0;i<5;i++)
	{

		printf("%2d",arr[i]);
	}
	printf("\n");
	
	printf("arr[5]相反=");
	for(i=4;i>=0;i--)
	{
		arr[5]=i;
		printf("%2d",arr[i]);
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

	
	printf("刪除第幾個數字:");
        scanf("%d",&b);
	for(i=0;i<5;i++)
	{
      
		if(i==(b-1))
		{
		printf("");
		continue;
		}		
		printf("2%d",arr[i]); 

	}	


}
