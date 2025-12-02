#include<stdio.h>
#include<stdlib.h>
int main(void)
{
	int a,b,c;
	printf("輸入3整數:");
	scanf("%d %d %d",&a,&b,&c);
         
	if( (a==b) && (a==c) && (b==c) )
	{ printf("正三角形\n"); }

	else if( ((a==b)+a>c)	|| ((b==c)+b>a) || ((c==a)+c>b) )
	{ printf("等腰三角形\n"); }

	else if( (a*a+b*b==c*c) || (a*a+c*c==b*b) || (c*c+b*b==a*a) )
	{ printf("不等邊三角形\n");   }

	else 
	{  printf("不是三角形\n"); }

	return 0;

}



