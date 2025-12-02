#include<stdio.h>
#include<stdlib.h>
int main(void)
{
	int arr[2][3];
	printf("輸入arr[2][3]:\n");
	for(int i=0;i<2;i++)
	{
		for(int j=0;j<3;j++)
		{
			scanf("%d",&arr[i][j]);
		}
	}
	for(int ii=0;ii<2;ii++)
	{
		for(int jj=0;jj<3;jj++)
		{
		printf("%3d",arr[ii][jj]);
		}printf("\n");
	}

}
