#include<stdio.h>
#include<stdlib.h>
int main(void)
{
	int arr[10][11]={0};
	int i,j;
	int a,b;
	printf(" 0123456789\n");

	
	for(i=0;i<10;i++){
		printf("%d",i);
		for(j=1;j<11;j++){
			
			arr[i][j]=' ';
			printf("%c",arr[i][j]);
		}printf("\n");
	}
	
	printf("\n");
	scanf("%d %d",&a,&b);
	b+=1;
	printf(" 0123456789\n");
	for(i=0;i<10;i++){
                printf("%d",i);
                for(j=1;j<11;j++){
			
			arr[i][j]=' ';
			if(arr[a][b]!=0){
				arr[a][b]='W';}
                        printf("%c",arr[i][j]);
                }printf("\n");
	}
}
