#include<stdio.h>
#include<stdlib.h>
int main(void)
{
	int i, nn=4;
	for(i=1;i<=nn;i++)
	{	
	        int a;
      		for(a=0;a<=nn-i;a++)
		{
			printf("*");
		}
			printf("\n");	
		
	}	
return 0;
}


