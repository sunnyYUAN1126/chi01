#include<stdio.h>
#include<stdlib.h>
int fun(char,int);
int main(void)
{
	int i,n=4;
	for(i=1;i<n;i++)
	{
		fun(' ',i);
		fun('*',n*2-i*2);  //保持偶數才能接下面單數 (偶數-1)
		printf("\n");
	}
}
int fun(char ch,int n)
{
        int i;
	for(i=1;i<n;i++)   //偶數-1
	{
		printf("%c",ch);
	}
}
