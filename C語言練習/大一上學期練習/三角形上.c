#include<stdio.h>
#include<stdlib.h>
int fun(char ,int);
int main(void)
{
	int i,n=5;
	for(i=1;i<n;i++)
	{
		fun(' ',n-i);
                fun('*',i*2);
	        printf("\n");
	}
}

int fun(char ch,int n)
{
	int i;
	for(i=1;i<n;i++)    // ex: i=1,i<6 (3*2=6) ,有1到5個
	{
		printf("%c",ch);
	}
}
