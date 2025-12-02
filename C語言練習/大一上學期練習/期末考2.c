#include<stdio.h>
#include<stdlib.h>
int main(void)
{
	int i,a,b,c;
	int ii,all;
        scanf("%d",&a);
	for(i=1;i<=a;i++)
	{
	scanf("%d %d",&b,&c);	
        all+=b*c;
	printf("b*c=%d\n",all);
	}
}

