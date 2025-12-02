#include<stdio.h>
#include<stdlib.h>
int main(void)
{
	int arr[10][11]={0};
	int i,j;

	printf(" 0123456789\n");
	for(i=0;i<10;i++){
		for(j=0;j<11;j++){
			arr[i][0]=i;
			printf("%d",arr[i][j]);
		}printf("\n");
	}

	for(i=1;i<10;i++){
		for(j=1;j<11;j++){
			arr[i][j]=' ';
			printf("%c",arr[i][j]);
		}printf("\n");
	}
}




