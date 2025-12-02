#include<stdio.h>
#include<stdlib.h>
int main(void)
{
	int i,j,n,m; 
	scanf("%d %d",&n,&m);
	int arr[n][m];
	for(i=1;i<=n;i++)
	{
              
		for(j=1;j<=m;j++)
		{
			
			arr[i][j]=i*j;
			printf(" [%d][%d]=%d\t",i,j,arr[i][j] );
		
		}
		printf("\n");
	}
	while(1)
	{
		printf("輸入幾成幾:");
		scanf("%d %d",&i,&j);
		printf("%d\n",arr[i][j]);
	}
	return 0;
}


