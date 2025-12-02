#include<stdio.h>
#include<stdlib.h>
int main(void)
{
	int i,j,n,m,a=0; 
	scanf("%d %d",&n,&m);
	int arr[n][m];
	for(i=0;i<n;i++)
	{
              
		for(j=0;j<m;j++)
		{
			a+=1;
			arr[n][m]=a;
			printf("%d\t",a );
		
		}
		printf("\n");
	}
	return 0;
}


