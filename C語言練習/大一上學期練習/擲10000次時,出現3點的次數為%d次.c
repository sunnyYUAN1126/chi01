#include<stdio.h>
#include<stdlib.h>
int main(void)
{
	int i, count=0, d;
	for(i=1; i<=10000; i++)
	{ if((d=(rand()%6+1))==3 )  
         count++;  }
	     
             printf("i=%5d, count=%5d\n",i,count);
	     printf("擲10000次時,出現3點的次數為%d次\n",count);
	     printf("機率為%.3f\n",(float)count/10000);

	     return 0;
	     }



