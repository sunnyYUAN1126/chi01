#include<stdio.h>
#include<stdlib.h>
int main(void)
{
	int i,b=0;
	for(i=1;i<=10000;i++)
	{
		if( (rand()%6)+1==3 )
		{
			b++;
		}
	}
		printf("%d\n",b);
		printf("%.3f\n",(float)b/10000);
	
}
