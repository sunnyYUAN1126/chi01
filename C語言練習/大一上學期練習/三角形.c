#include<stdio.h>
#include<stdlib.h>
int main(void)
{
	int a,s,d;
	printf("輸入3數字\n");
	scanf("%d %d %d",&a,&s,&d);
	if((a+s>d) && (a+d>s) && (s+d>a))
	{
		if((a==s) && (a==d) )
		{ printf("正\n"); }

		else if( (a==s) || (a==d) || (s==d) )
		{ printf("等腰\n");  }

		else 
		{ printf("不等邊\n"); }
	}

	else
	{  printf("不是\n"); }

	return 0;
}

