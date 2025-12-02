#include<stdio.h>
#include<stdlib.h>
int main(void)
{
	int arr[4][6];
	for(int i=0;i<4;i++)
	{
		for(int j=0;j<6;j++)
		{
         	arr[i][j]=0;
		arr[i][0]=i;
		arr[0][j]=j;
	
		printf("%3d",arr[i][j]);
		}printf("\n");
	}
}
