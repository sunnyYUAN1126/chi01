#include<stdio.h>
#include<stdlib.h>
int main(void)
{
	int arr[10][10];
	int i,j;
	
	for(i=1;i<10;i++)
	{
		for(j=1;j<10;j++)
		{
			*(*(arr+i)+j)=i*j;
			printf("%3d",*(*(arr+i)+j));
		}printf("\n");
	}
}













