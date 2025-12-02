#include<stdio.h>
#include<stdlib.h>
int main(void)
{
	int n,i=1,sum=0;
	/*do
	{ printf("請輸入n值(n>0):");
	  fflush(stdout);
	  scanf("%d",&n); }
	while(n<=0); */

	printf("請輸入n值(n>0):");
	 fflush(stdout);
         scanf("%d",&n); 
	 while(n<=0)
         printf("請輸入n值(n>0):");
	 scanf("%d",&n);
       


	do
	{ sum+=i++;}
	while(i<=n);
	printf("1+2+3...+%d=%d, i=%d\n",n,sum,i);

	return 0;
}
