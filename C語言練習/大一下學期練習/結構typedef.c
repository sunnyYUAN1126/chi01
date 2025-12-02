#include<stdio.h>
#include<stdlib.h>
struct date
{
	int a;
	char arr[10];
};
typedef struct date aaa;
int fun(aaa  *);
int main(void)
{
	aaa stry={77,"gfgf"};
	fun(&stry);
}
int fun(aaa *bby)
{
	printf("%d,%s\n",bby->a,bby->arr);
}
	










