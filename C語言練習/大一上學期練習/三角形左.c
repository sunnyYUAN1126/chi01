#include<stdio.h>
#include<stdlib.h>
int fun3(char,int);
int  main(void)
{


        int i,nn=4;
	for(i=1;i<=nn;i++)
	{
		fun3(' ',nn-i+1);
		fun3('*',i);
	
		printf("\n");
	}
 
        fun3('*',nn+1);
        printf("\n");
	
        for(i=1;i<=nn;i++)
	{
		fun3(' ',i);
		fun3('*',nn-i+1);
		printf("\n");
	}
}


int fun3(char ch,int nn)
{
	int i;
	for(i=1;i<=nn;i++)
	{
		printf("%c",ch);
	}
}

