#include<stdio.h>
#include<stdlib.h>
int fun1(int);
int fun2(int);
int main(void)
{
	int i;
	fun1(i);
	printf("\n");
	fun2(i);
}

int fun1(int i)
{
	for(i=1;i<=10;i++)
	{		
		if(i%5==0){
			break; }
		printf("i=%d\n",i);
	}
	printf("i=%d跳出\n",i);
}

int fun2(int i)
{
	for(i=1;i<=10;i++)
	{
	     // printf("i=%d\n",i); 會顯示出來	
		if(i%5==0){
			continue;}
		printf("i=%d\n",i);
	}
	printf("i=%d跳出\n",i);
}

