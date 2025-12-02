#include<stdio.h>
#include<stdlib.h>
void fun(int c,int d);
int main()
{
	int x,y;
	printf("2數字: ");
	scanf("%d %d",&x,&y);
	fun(x,y);


}



void fun(int c,int d)
{
	int a,b;
	for(a=1 ;a<=c ;a++)
	{
		for(b=1; b<=d ;b++)
		{
		printf("%d*%d=%d\t",a,b,a*b);
		}
		printf("\n");
       }
	
}
