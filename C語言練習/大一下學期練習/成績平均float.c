#include<stdio.h>
#include<stdlib.h>
int main(void)
{
	int i,n,all,arr[10];
	for(i=0;i<10;i++)
	{
		printf("輸入成績:");
		scanf("%d",&arr[i]);
		if(arr[i]==0){
			break;
		}
		all+=arr[i];
	}
	printf("平均成績=%f\n",(float)all/i);
}

